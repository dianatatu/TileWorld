from Queue import Queue
import time
from threading import Thread, Lock

from resources.constants import REWARD, BONUS
from resources import utils


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
        self.plan = []
        self.can_request_entire_state = True
        self.waiting_for_response = False

    def run(self):
        self.request_entire_state()
        can_request_entire_state = False

        while True:
            message = self.check_mailbox()

            # I've got mail!
            if message:
                if message['type'] == 'the_end':
                    break
                if message['type'] == 'response_entire_state':
                    self._safe_print("I have the entire state!")
                    self.grid = message['grid']
                if message['type'] == 'response_action':
                    self.waiting_for_response = False
                    if message['status'] == 'OK':
                        self.perform_action(message['action'])
                    else:
                        self._safe_print("Action was refused by environment.")

            # No mail for me!
            else:
                if not self.grid:
                    continue
                elif self.plan:
                    if not self.waiting_for_response:
                        self.go_on_with_my_plan()
                else:
                    self.plan = self.get_most_efficient_plan()
#                    self._safe_print("My plan: %r" % self.plan)
                    self.go_on_with_my_plan()


########################### COMMUNICATION ###########################

    def check_mailbox(self):
        self.queue_lock.acquire()
        message = None
        if not self.queue.empty():
            message = self.queue.get()
        self.queue_lock.release()
        return message

    def send(self, to, message):
        queue, queue_lock = self.queue_system[to]
        queue_lock.acquire()
        # Sign message.
        message.update({'from': self.name})
        # Send message.
        queue.put(message)
        queue_lock.release()

    def request_entire_state(self):
        self._safe_print("Requesting entire state")
        self.send('environment', {'type': 'request_entire_state'})

    def request_move(self, action):
        self._safe_print("Requesting action: %r" % action)
        self.send('environment', {'type': 'request_action',
                                  'action': action})

########################### ACTIONS ###########################

    def perform_action(self, action):
        if action['type'] == 'go_to':
            self.go_to(action['x'], action['y'])

    def pickup(self, tile):
        if self.carry_tile:
            self._safe_print("Agent already has picked up a tile")
            return
        self.carry_tile = tile

    def drop(self, tile):
        if not self.carry_tile:
            self._safe_print("Agent has no picked up tile")
            return
        self.carry_tile = None

    def go_to(self, x, y):
        self.x = x
        self.y = y

    def go_on_with_my_plan(self):
        next_move = self.plan.pop(0)
        self.request_move(next_move)
        self.waiting_for_response = True

########################## UTILS ##############################

    def __unicode__(self):
        return '<%s, (%s,%s) -> %s>' % (self.name, self.x, self.y, self.color)

    def get_most_efficient_plan(self):
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

        min_cost = {'value': 9999, 'hole': None, 'tile': None}
        for tile in tiles:
            for hole in holes:
                cost = 0
                # go to tile
                path = self.get_shortest_path(self.x, self.y, tile[0], tile[1])
                cost -= len(path)
                # pick tile
                cost -= 1
                # go near hole and drop tile
                cost -= len(self.get_shortest_near_path(path[len(path)-1][0],
                                                        path[len(path)-1][1],
                                                        hole[0], hole[1]))
                cost += hole[2]
                if cost < min_cost['value']:
                    min_cost['value'] = cost
                    min_cost['tile'] = tile
                    min_cost['hole'] = (hole[0], hole[1])

#        if min_cost['value'] <= 0:
#            return None

        plan = []
        # go to the closest
        tile_path = self.get_shortest_path(self.x, self.y,
                                           min_cost['tile'][0],
                                           min_cost['tile'][1])
        for move in tile_path:
            plan.append({'type': 'go_to',
                         'x': move[0],
                         'y': move[1]})

        plan.append({'type': 'pick',
                     'x': min_cost['tile'][0],
                     'y': min_cost['tile'][1]})

        hole_path = self.get_shortest_near_path(tile_path[len(tile_path)-1][0],
                                                tile_path[len(tile_path)-1][1],
                                                min_cost['hole'][0],
                                                min_cost['hole'][1])

        for move in hole_path:
            plan.append({'type': 'go_to',
                         'x': move[0],
                         'y': move[1]})

        plan.append({'type': 'drop',
                     'x': min_cost['hole'][0],
                     'y': min_cost['hole'][1]})

        return plan

    def _safe_print(self, message):
        self.display_lock.acquire()
        print "[%s] %s" % (self.name, message)
        self.display_lock.release()

    def get_shortest_path(self, from_x, from_y, to_x, to_y):
        return utils.bfs(from_x, from_y, to_x, to_y, self.grid)

    def get_shortest_near_path(self, from_x, from_y, to_x, to_y):
        return utils.near_bfs(from_x, from_y, to_x, to_y, self.grid)