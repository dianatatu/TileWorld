from Queue import Queue
import time
from threading import Thread, Lock
import uuid

from termcolor import cprint

from resources.constants import REWARD, BONUS
from resources import utils

REWARD_PERCENT = 0.75


class CognitiveAgent(Thread):

    def __init__(self, name, x, y, color):
        Thread.__init__(self)
        self.points = 0
        self.carry_tile = None
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.queue = Queue()
        self.queue_lock = Lock()
        self.grid = None
        self.plans = []
        self.plan = []
        self.can_request_entire_state = True
        self.waiting_for_response = False
        self.negociating = False
        self.pending_proposals = []

    def run(self):
        self.request_entire_state()
        can_request_entire_state = False

        while True:
            message = self.check_mailbox()

            # I've got mail!
            if message:
                if message['type'] == 'the_end':
                    break
                elif message['type'] == 'response_entire_state':
                    self._safe_print("I have the entire state!")
                    self.grid = message['grid']
                    self.can_request_entire_state = True
                    if len(self.pending_proposals) > 0:
                        self.investigate_proposals()

                elif message['type'] == 'response_action':
                    self.waiting_for_response = False
                    if message['status'] == 'OK':
                        self.perform_action(message['action'])
                    else:
                        self._safe_print("Action was refused by environment.")
                        self.request_entire_state()
                        self.can_request_entire_state = False
                elif message['type'] == 'proposal':
                    self._safe_print("Received proposal from %r: %r"
                                     % (message['from'], message['proposal']))
                    if self.grid:
                        self._safe_print("Investigating ...")
                        self.investigate_proposal(message['proposal'], message['from'])
                    else:
                        self.pending_proposals.append(message)
                        self._safe_print("I have no knowledge about the grid. "
                                         "Postponing proposal.")
                elif message['type'] == 'accept_proposal':
                    self._safe_print(":) %r accepted proposal %r"
                                     % (message['from'], message['proposal']))
                elif message['type'] == 'refine_proposal':
                    self._safe_print(":) %r want a refine on proposal %r"
                                     % (message['from'], message['proposal']))
                elif message['type'] == 'refuse_proposal':
                    self._safe_print(":( %r refused proposal %r"
                                     % (message['from'], message['proposal']))

            # No mail for me!
            else:
                if not self.grid or self.negociating:
                    continue
                if len(self.plans) > 0:
                    if not self.waiting_for_response:
                        self.go_on_with_my_plan()
                else:
                    self.plans = self.get_available_plans()
                    if len(self.plans) > 0:
                        self.negociating = True
                        self.make_proposals()
                    else:
                        if self.can_request_entire_state:
                            self.request_entire_state()
                            self.can_request_entire_state = False


########################### C O M M U N I C A T I O N #########################

    def check_mailbox(self):
        self.queue_lock.acquire()
        message = None
        if not self.queue.empty():
            message = self.queue.get()
        self.queue_lock.release()
        return message

    def send(self, message, to=None):
        if to:
            queue, queue_lock = self.queue_system[to]
            queue_lock.acquire()
            # Sign message.
            message.update({'from': self.name})
            # Send message.
            queue.put(message)
            queue_lock.release()
        else:
            for agent in self.queue_system.keys():
                if agent != 'environment' and agent != self.name:
                    self._safe_print("Sending proposal to %s: %r" % (agent, message))
                    queue, queue_lock = self.queue_system[agent]
                    queue_lock.acquire()
                    # Sign message.
                    message.update({'from': self.name})
                    # Send message.
                    queue.put(message)
                    queue_lock.release()

    def send_proposal(self, proposal):
        self.send({'type': 'proposal', 'proposal': proposal})

    def request_entire_state(self):
        self._safe_print("Requesting entire state")
        self.send({'type': 'request_entire_state'}, to='environment')

    def request_move(self, action):
        self._safe_print("Requesting action: %r" % action)
        self.send({'type': 'request_action', 'action': action}, to='environment')

########################### A C T I O N S ###########################

    def perform_action(self, action):
        if action['type'] == 'go_to':
            self.go_to(action['x'], action['y'])
        elif action['type'] == 'pick':
            self.pickup(action['color'])
        elif action['type'] == 'drop':
            self.drop(action['points'])

    def pickup(self, color):
        if self.carry_tile:
            self._safe_print("Agent already has picked up a tile")
            return
        self.carry_tile = color

    def drop(self, points):
        if not self.carry_tile:
            self._safe_print("Agent has no picked up tile")
            return
        self.carry_tile = None

    def go_to(self, x, y):
        self.x = x
        self.y = y

    def go_on_with_my_plan(self):
        next_move = self.plan['actions'].pop(0)
        self.request_move(next_move)
        self.waiting_for_response = True

########################## N E G O C I A T I N G ##############################

    def make_proposals(self):
        for plan in self.plans:
            proposal = {}
            proposal['id'] = plan['id']
            proposal['reward'] = int(plan['reward'] * REWARD_PERCENT)
            proposal['tile'] = plan['tile']
            proposal['hole'] = plan['hole'][:-1]
            self.send_proposal(proposal)

    def investigate_proposals(self):
        for message in self.pending_proposals:
            self.investigate_proposal(message['proposal'], message['from'])

    def investigate_proposal(self, proposal, requester):
        proposed_reward = proposal['reward']
        tile = proposal['tile']
        hole = proposal['hole']
        my_cost = len(self.get_shortest_path(self.x, self.y, tile[0], tile[1]))
        my_cost = my_cost + 1
        my_cost = my_cost + len(self.get_shortest_near_path(tile[0], tile[1],
                                                        hole[0], hole[1]))
        my_cost = my_cost + 1
        actual_reward = proposed_reward - my_cost
        if actual_reward > 0:
            self._safe_print("Accept proposal from %r. Actual reward = %d-%d = %d"
                             % (requester, proposed_reward, my_cost, actual_reward))
            self.accept_proposal(proposal, requester)
        elif actual_reward > 0 - int(REWARD_PERCENT * actual_reward):
            self._safe_print("Asking for a refine from %r" % requester)
            self.refine_proposal(proposal, requester)
        else:
            self._safe_print("Refusing proposal from %r. Actual reward = %d-%d = %d"
                              % (requester, proposed_reward, my_cost, actual_reward))
            self.refuse_proposal(proposal, requester)

    def accept_proposal(self, proposal, requester):
        message = {'type': 'accept_proposal',
                   'proposal': proposal}
        self.send(message, requester)

    def refine_proposal(self, proposal, requester):
        pass

    def refuse_proposal(self, proposal, requester):
        pass

################################# U T I L S ##################################

    def __unicode__(self):
        return '<%s, (%s,%s) -> %s>' % (self.name, self.x, self.y, self.color)

    def get_available_plans(self):
        tiles = []
        holes = []
        for i in range(0, self.grid['H']):
            for j in range(0, self.grid['W']):
                for tile_color in self.grid['cells'][i][j]['tiles']:
                    if tile_color == self.color:
                        tiles.append((i,j))
                if self.grid['cells'][i][j]['color'] == self.color:
                    if self.grid['cells'][i][j]['h'] < -1:
                        holes.append((i, j, REWARD))
                    elif self.grid['cells'][i][j]['h'] == -1:
                        holes.append((i, j, REWARD+BONUS))
        plans = []
        max_gain = {'value': -9999, 'hole': None, 'tile': None}
        for tile in tiles:
            for hole in holes:
                # go to tile
                path = self.get_shortest_path(self.x, self.y, tile[0], tile[1])
                minus = len(path)
                # pick tile
                minus += 1
                # go near hole and drop tile
                minus += len(self.get_shortest_near_path(path[len(path)-1][0],
                                                        path[len(path)-1][1],
                                                        hole[0], hole[1]))
                minus += 1
                plus = hole[2]
                gain = - minus + plus
                if gain > max_gain['value']:
                    max_gain['value'] = gain
                    max_gain['minus'] = minus
                    max_gain['plus'] = plus
                    max_gain['tile'] = tile
                    max_gain['hole'] = (hole[0], hole[1])

                actions = []
                # go to the closest cell near hole
                tile_path = self.get_shortest_path(self.x, self.y,
                                                   max_gain['tile'][0],
                                                   max_gain['tile'][1])
                for move in tile_path:
                    actions.append({'type': 'go_to',
                                    'x': move[0],
                                    'y': move[1]})

                actions.append({'type': 'pick',
                                'x': max_gain['tile'][0],
                                'y': max_gain['tile'][1],
                                'color': self.color})

                hole_path = self.get_shortest_near_path(tile_path[len(tile_path)-1][0],
                                                        tile_path[len(tile_path)-1][1],
                                                        max_gain['hole'][0],
                                                        max_gain['hole'][1])

                for move in hole_path:
                    actions.append({'type': 'go_to',
                                    'x': move[0],
                                    'y': move[1]})

                actions.append({'type': 'drop',
                                'x': max_gain['hole'][0],
                                'y': max_gain['hole'][1],
                                'color': self.color})

                plan = {
                    'id': uuid.uuid4(),
                    'utility': float(max_gain['plus']) / max_gain['minus'],
                    'actions': actions,
                    'cost': minus,
                    'reward': plus,
                    'tile': tile,
                    'hole': hole
                }
                plans.append(plan)

        if max_gain['value'] < 0:
            return {'actions': []}

        return plans

    def _safe_print(self, message):
        self.display_lock.acquire()
        cprint('%s: %s' % (self.name, message), self.color, end='\n')
        self.display_lock.release()

    def get_shortest_path(self, from_x, from_y, to_x, to_y):
        return utils.bfs(from_x, from_y, to_x, to_y, self.grid)

    def get_shortest_near_path(self, from_x, from_y, to_x, to_y):
        return utils.near_bfs(from_x, from_y, to_x, to_y, self.grid)
