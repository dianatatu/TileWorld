import json
from Queue import Queue
from threading import Thread, Lock
import time

from resources.utils import display_cell


class Environment(Thread):

    def __init__(self, t, T, grid, agents):
        Thread.__init__(self)
        self.name = 'environment'
        self.t = t
        self.T = T
        self.grid = grid
        self.agents = agents
        self.points = {}
        self.queue = Queue()
        self.queue_lock = Lock()

    def run(self):
        while self.T > 0:
            self.display_grid(self.grid)
            message = self.check_mailbox()
            if message:
                if message['type'] == 'request_entire_state':
                    self.respond_entire_state(message['from'])
                elif message['type'] == 'request_action':
                    self.perform_action(message['action'], message['from'])
                self.T = self.T - self.t
            else:
                self.T = self.T - 1
            self.T = self.T-1
            time.sleep(1)

        self.send_the_end()


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
        queue.put(message)
        queue_lock.release()

    def respond_entire_state(self, requester):
        message = {'type': 'response_entire_state'}
        message.update({'grid': self.grid})
        self.send(requester, message)

    def perform_action(self, action, requester):
        if action['type'] == 'go_to':
            self.perform_go_to_action(action, requester)

    def perform_go_to_action(self, action, requester):
        from_x, from_y = self.localize(requester)
        to_x, to_y = action['x'], action['y']

        is_valid = ( (abs(to_x-from_x) == 1 and to_y==from_y) or
                     (abs(to_y-from_y) == 1 and to_x==from_x) )
        is_safe = self.grid['cells'][to_x][to_y]['h'] == 0
        if is_valid and is_safe:
            agent = [agent for agent in self.agents if agent.name==requester][0]
            agent.x, agent.y = to_x, to_y
            self.grid['cells'][from_x][from_y]['agents'].remove((agent.name,
                                                                 from_x, from_y,
                                                                 agent.color))
            self.grid['cells'][to_x][to_y]['agents'].append((agent.name,
                                                             agent.x, agent.y,
                                                             agent.color))
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'OK'})
        else:
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'FAIL'})

    def send_the_end(self):
        message = {'type': 'the_end'}
        for agent in self.agents:
            self.send(agent.name, message)


############################# DISPLAY #################################

    def display_grid(self, grid):
        self.display_lock.acquire()
        print '--------------------------------'
        for i in range(0, grid['H']):
            for j in range(0, grid['W']):
                display_cell(grid['cells'][i][j], self.agents)
            print ''
        print '--------------------------------'
        self.display_lock.release()

    def _safe_print(self, message):
        self.display_lock.acquire()
        print "[%s] %s" % (self.name, message)
        self.display_lock.release()

############################# UTILS #################################

    def localize(self, requester):
        """Return the agent position within the grid.""" 
        for i in range(0, self.grid['H']):
            for j in range(0, self.grid['W']):
                for agent in self.grid['cells'][i][j]['agents']:
                    if agent[0] == requester:
                        return (i, j)

        self._safe_print("[E] Agent not found!")
        return None
