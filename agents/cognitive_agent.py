from Queue import Queue
import time
from threading import Thread, Lock


class CognitiveAgent(Thread):

    def __init__(self, name, x, y, color):
        Thread.__init__(self)
        self.points = 0
        self.carry_tile = None
        self.name = 'agent%s' % name
        self.x = x
        self.y = y
        self.color = color
        self.queue = Queue()
        self.queue_lock = Lock()

    def __unicode__(self):
        return '<%s, (%s,%s) -> %s>' % (self.name, self.x, self.y, self.color)

    def run(self):
        self.request_entire_state()
#        # wait for entire state response
#        while True:
#            if self.queue_system.peek(self.name):
#                message = self.queue_system.fetch_from(self.name)
#                if message and message['type'] == 'response_entire_state':
#                    grid = message['grid']
#                    break
#
#        # get the most efficient plan
#        plans = self.get_most_efficient_plan(grid)

        while True:
            message = self.check_mailbox()
            if not message:
                continue
            if message['type'] == 'the_end':
                break
            if message['type'] == 'response_entire_state':
                self._safe_print("I have the entire state!")


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
        print "%s just put %r to %s" % (self.name, message, to)
        queue.put(message)
        queue_lock.release()

    def request_entire_state(self):
        self._safe_print("Requesting entire state")
        self.send('environment', {'type': 'request_entire_state'})


########################### ACTIONS ###########################

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


########################## UTILS ##############################

    def get_most_efficient_plan(self, grid):
        pass

    def _safe_print(self, message):
        self.display_lock.acquire()
        print "[%s] %s" % (self.name, message)
        self.display_lock.release()
