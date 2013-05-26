from Queue import Queue
import time
from threading import Thread, Lock
import uuid

from termcolor import cprint

from resources.constants import REWARD, BONUS
from resources import utils

REWARD_PERCENT = 0.75
NEGOCIATION_TIME = 6


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
        self.can_request_entire_state = True
        self.waiting_for_response = False
        self.their_proposals = []
        self.my_proposals = []


    def run(self):
        """Main loop of action."""
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
                    if len(self.plans) == 0:
                        self.plans = self.get_available_plans()
                        self.current_plan = self.plans.pop(0)
                        self.make_proposals()
                    if len(self.their_proposals) > 0:
                        self.investigate_proposals()
                    self.can_request_entire_state = True

                elif message['type'] == 'response_action':
                    self.waiting_for_response = False
                    if message['status'] == 'OK':
                        self.perform_action(message['action'])
                    else:
                        self._safe_print("Action was refused by environment.")
                        self.request_entire_state()
                        self.can_request_entire_state = False

                elif message['type'] == 'response_transfer_points':
                    if message['status'] == 'OK':
                        self._safe_print("I transferred %r points to %r"
                                         % (message['value'], message['to']))
                    else:
                        self._safe_print("I couldn't transfer %r points to %r"
                                         % (message['value'], message['to']))

                elif message['type'] == 'proposal':
                    self._safe_print("Received proposal %r from %r"
                                     % (message['proposal']['id'], message['from']))
                    if self.grid:
                        self._safe_print("Investigating ...")
                        self.investigate_proposal(message['proposal'],
                                                  message['from'])
                    else:
                        self.their_proposals.append(message)
                        self._safe_print("I have no knowledge about the grid. "
                                         "Postponing proposal.")

                elif message['type'] == 'accept_proposal':
                    self._safe_print(":) %r accepted proposal %r"
                                     % (message['from'], message['proposal']))
                    self.shake_hands(message)
                    self.remove_plan(message['proposal']['id'])

                elif message['type'] == 'refuse_proposal':
                    self._safe_print(":( %r refused proposal %r"
                                     % (message['from'], message['proposal']))

                elif message['type'] == 'shake_hands':
                    self._safe_print("Shake hands on %r with %r for %r points."
                                     % (message['proposal']['proposal']['id'],
                                        message['from'],
                                        message['proposal']['proposal']['reward']))
                    self.plans.insert(0, self.get_plan(self.current_plan['actions'][len(self.current_plan['actions'])-1]['x'],
                                                       self.current_plan['actions'][len(self.current_plan['actions'])-1]['y'],
                                                       message['proposal']['proposal']['tile'],
                                                       message['proposal']['proposal']['hole'],
                                                       message['proposal']['proposal']['color']))

            # No mail for me!
            else:
                if not self.grid:
                    continue
                if len(self.current_plan) > 0 or len(self.plans) > 0:
                    if not self.waiting_for_response:
                        self.go_on_with_my_plan()
                else:
                    if len(self.plans) > 0:
                        self.make_proposals()
                    else:
                        if self.can_request_entire_state:
                            self.request_entire_state()
                            self.can_request_entire_state = False

########################### C O M M U N I C A T I O N #########################

    def check_mailbox(self):
        """Checks if some other agent sent a message."""
        self.queue_lock.acquire()
        message = None
        if not self.queue.empty():
            message = self.queue.get()
        self.queue_lock.release()
        return message

    def send(self, message, to=None):
        """Sends mail to other agents. If no destination provided, by default,
        the message is sent to each agent (except 'environment' agent).
        """
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
        """Sends a proposal message containing an offer."""
        self.send({'type': 'proposal', 'proposal': proposal})

    def request_entire_state(self):
        """Sends a request for the entire state to engironment agent."""
        self._safe_print("Requesting entire state")
        self.send({'type': 'request_entire_state'}, to='environment')

    def request_move(self, action):
        self._safe_print("Requesting action: %r" % action)
        self.send({'type': 'request_action', 'action': action}, to='environment')

########################### A C T I O N S ###########################

    def perform_action(self, action):
        """Move agent according to the accepted request by the environment
        agent. Possible moves: go_to, pick, drop.
        """
        if action['type'] == 'go_to':
            self.go_to(action['x'], action['y'])
        elif action['type'] == 'pick':
            self.pickup(action['color'])
        elif action['type'] == 'drop':
            self.drop(action['points'])

    def pickup(self, color):
        """Picks up a tile from the current cell."""
        if self.carry_tile:
            self._safe_print("Agent already has picked up a tile")
            return
        self.carry_tile = color

    def drop(self, points):
        """Drops the carrying tile in the current cell."""
        if not self.carry_tile:
            self._safe_print("Agent has no picked up tile")
            return
        self.carry_tile = None

    def go_to(self, x, y):
        """Move agent to (x, y) cell."""
        self.x = x
        self.y = y

    def go_on_with_my_plan(self):
        """Get next action from the current performing plan."""
        if len(self.current_plan['actions']) == 0:
            if len(self.plans) == 0:
                return
            self.current_plan = self.plans.pop(0)
            self.current_plan = self.get_plan(self.x, self.y, 
                                              self.current_plan['tile'],
                                              self.current_plan['hole'],
                                              self.current_plan['color'])
            self._safe_print("My new plan: %r" % self.current_plan)
        next_move = self.current_plan['actions'].pop(0)
        self.request_move(next_move)
        self.waiting_for_response = True

########################## N E G O C I A T I N G ##############################

    def make_proposals(self):
        """Compose a proposal for other agents."""
        for plan in self.plans:
            proposal = {}
            proposal['id'] = plan['id']
            proposal['reward'] = int(plan['reward'] * REWARD_PERCENT)
            proposal['tile'] = plan['tile']
            proposal['hole'] = plan['hole'][:-1]
            proposal['initiator'] = self.name
            proposal['color'] = self.color
            self.send_proposal(proposal)
            self.my_proposals.append(proposal)

    def investigate_proposals(self):
        """Investigates all pending proposals. These proposals could not be
        investigated when received because there was no knowledge about the
        grid environment.
        """
        for message in self.their_proposals:
            self.investigate_proposal(message['proposal'], message['from'])

    def investigate_proposal(self, proposal, requester):
        """Investigates the actual cost and reward of the received proposal.
        Decides whether accept the proposal or not. This proposal is thought
        to be executed after finishing the current action plan.
        """ 
        proposed_reward = proposal['reward']
        tile = proposal['tile']
        hole = proposal['hole']

        from_x = self.current_plan['actions'][len(self.current_plan['actions'])-1]['x']
        from_y = self.current_plan['actions'][len(self.current_plan['actions'])-1]['y']

        my_cost = len(self.get_shortest_path(from_x, from_y, tile[0], tile[1]))
        my_cost = my_cost + 1
        my_cost = my_cost + len(self.get_shortest_near_path(tile[0], tile[1],
                                                            hole[0], hole[1]))
        my_cost = my_cost + 1
        actual_reward = proposed_reward - my_cost
        if actual_reward > 0:
            self._safe_print("Accept proposal %r from %r. Actual reward = %d-%d = %d"
                             % (proposal['id'], requester, proposed_reward, my_cost, actual_reward))
            self.accept_proposal(proposal, requester)
        else:
            self._safe_print("Refusing proposal %r from %r. Actual reward = %d-%d = %d"
                              % (requester, proposal['id'], proposed_reward, my_cost, actual_reward))
            self.refuse_proposal(proposal, requester)

    def accept_proposal(self, proposal, requester):
        """Sends message to agent and inform him that the proposal has been
        accepted.
        """
        message = {'type': 'accept_proposal',
                   'proposal': proposal}
        self.send(message, requester)

    def refuse_proposal(self, proposal, requester):
        """Sends message to agent and inform him that the proposal has been
        refused.
        """
        message = {'type': 'refuse_proposal',
                   'proposal': proposal}
        self.send(message, requester)

    def shake_hands(self, proposal):
        """The last step of the 'three-way handshake' after accepting a
        proposal and before adding the proposal to agent's next steps.
        """
        #self._safe_print("Sending shake hands on %r to %r of color %r" % (proposal['proposal']['id'], proposal['from'], proposal['proposal']['color']))
        self.send({'type': 'shake_hands', 'proposal': proposal},
                  proposal['from'])
        self.send({'type': 'transfer_points',
                   'value': proposal['proposal']['reward'],
                   'to': proposal['from']},
                  'environment')

    def remove_plan(self, id):
        """If one action plan was accepted by other agent, remove it from the
        current pending plans."""
        for plan in self.plans:
            if plan['id'] == id:
                self.plans.remove(plan)
                break

################################# U T I L S ##################################

    def __unicode__(self):
        return '<%s, (%s,%s) -> %s>' % (self.name, self.x, self.y, self.color)

    def get_plan(self, from_x, from_y, tile, hole, color):
        """Forms a plan of unit actions that pick a tile and drops it in a
        specified hole.
        """
        actions = []
        # go to the closest cell near hole
        tile_path = self.get_shortest_path(from_x, self.y, tile[0], tile[1])
        for move in tile_path:
            actions.append({'type': 'go_to',
                            'x': move[0],
                            'y': move[1]})

        actions.append({'type': 'pick',
                        'x': tile[0],
                        'y': tile[1],
                        'color': color})

        hole_path = self.get_shortest_near_path(tile_path[len(tile_path)-1][0],
                                                tile_path[len(tile_path)-1][1],
                                                hole[0], hole[1])

        for move in hole_path:
            actions.append({'type': 'go_to',
                            'x': move[0],
                            'y': move[1]})

        actions.append({'type': 'drop',
                        'x': hole[0],
                        'y': hole[1],
                        'color': color})

        return {
            'id': uuid.uuid4(),
            'actions': actions,
            'tile': tile,
            'hole': hole,
            'color': color
        }


    def get_available_plans(self):
        """Inspects the environment grid and obtain all action plans available
        in order to collect all tiles and fill in all holes.
        """
        tiles = []
        holes = []
        for i in range(0, self.grid['H']):
            for j in range(0, self.grid['W']):
                for tile_color in self.grid['cells'][i][j]['tiles']:
                    if tile_color == self.color:
                        tiles.append((i,j))
                if self.grid['cells'][i][j]['color'] == self.color:
                    if self.grid['cells'][i][j]['h'] < -1:
                        holes.append((i, j, 5+REWARD))
                    elif self.grid['cells'][i][j]['h'] == -1:
                        holes.append((i, j, 5*REWARD+BONUS))
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
                    'hole': hole,
                    'color': self.color
                }

                plans.append(plan)

        if max_gain['value'] < 0:
            return {'actions': []}

        return plans

    def _safe_print(self, message):
        """Logs message to standard output. Uses a lock to prevent dithering
        messages from agents.
        """
        self.display_lock.acquire()
        cprint('[%s] %s: %s' % (int(time.time()), self.name, message), self.color, end='\n')
        self.display_lock.release()

    def get_shortest_path(self, from_x, from_y, to_x, to_y):
        """Returns the shortest path between 2 grid cells."""
        return utils.bfs(from_x, from_y, to_x, to_y, self.grid)

    def get_shortest_near_path(self, from_x, from_y, to_x, to_y):
        """Returns the shortest path between a cell grid and a neighbour of
        another cell. Used when searching for a way to pick a tile and drop it
        from a cell that is close to the hole."""
        return utils.near_bfs(from_x, from_y, to_x, to_y, self.grid)
