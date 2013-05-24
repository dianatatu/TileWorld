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
