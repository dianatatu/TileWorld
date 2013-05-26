import json
from Queue import Queue
from threading import Thread, Lock
import time

from resources.constants import REWARD, BONUS, TD
from resources.utils import display_cell


class Environment(Thread):

    def __init__(self, t, T, grid, agents):
        Thread.__init__(self)
        self.name = 'environment'
        self.t = t
        self.T = T
        self.grid = grid
        self.agents = agents
        self.queue = Queue()
        self.queue_lock = Lock()

    def run(self):
        """Main loop of action."""
        while self.T > 0:
            if self.T % TD == 0:
                self.display_grid(self.grid)
            message = self.check_mailbox()
            if message:
                if message['type'] == 'request_entire_state':
                    self.respond_entire_state(message['from'])
                elif message['type'] == 'request_action':
                    self.perform_action(message['action'], message['from'])
                elif message['type'] == 'pick':
                    self.perform_pick_action(message['action'], message['from'])
                elif message['type'] == 'drop':
                    self.perform_drop_action(message['action'], message['from'])
                elif message['type'] == 'transfer_points':
                    self.transfer_points(message['from'], message['to'], message['value'])
                self.T = self.T - self.t
            else:
                self.T = self.T - 1
            self.T = self.T-1
            time.sleep(1)

        self.send_the_end()


########################### C O M M U N I C A T I O N ########################

    def check_mailbox(self):
        """Checks if some other agent sent a message."""
        self.queue_lock.acquire()
        message = None
        if not self.queue.empty():
            message = self.queue.get()
        self.queue_lock.release()
        return message

    def send(self, to, message):
        """Sends mail to a specified agent."""
        queue, queue_lock = self.queue_system[to]
        queue_lock.acquire()
        queue.put(message)
        queue_lock.release()

    def respond_entire_state(self, requester):
        """Sends a message containg the entire current state of the grid."""
        message = {'type': 'response_entire_state'}
        message.update({'grid': self.grid})
        self.send(requester, message)

    def perform_action(self, action, requester):
        """Updates the environment grid according to an agent's move."""
        if action['type'] == 'go_to':
            self.perform_go_to_action(action, requester)
        elif action['type'] == 'pick':
            self.perform_pick_action(action, requester)
        elif action['type'] == 'drop':
            self.perform_drop_action(action, requester)

    def perform_go_to_action(self, action, requester):
        """Validates the received go_to move request. If valid, updates the
        environment grid according to a go_to agent's move.
        """
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

    def perform_pick_action(self, action, requester):
        """Validates the received pick request. If valid, updates the
        environment grid according to a pick agent's move.
        """
        from_x, from_y = self.localize(requester)
        agent = [agent for agent in self.agents if agent.name==requester][0]
        color = action['color']
        is_valid = (from_x == agent.x and from_y == agent.y and
                     self.exists_tile(from_x, from_y, color) and
                     not agent.carry_tile)
        if is_valid:
            self.grid['cells'][from_x][from_y]['tiles'].remove(color)
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'OK'})
        else:
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'FAIL'})

    def perform_drop_action(self, action, requester):
        """Validates the received drop request. If valid, updates the
        environment grid according to a drop agent's move.
        """
        from_x, from_y = self.localize(requester)
        agent = [agent for agent in self.agents if agent.name==requester][0]

        color = action['color']

        is_near = ( (abs(from_x-action['x'])==1 and from_y == action['y']) or
                     (abs(from_y-action['y'])==1 and from_x == action['x']) )
        has_tile = agent.carry_tile is not None
        colors_match = (agent.carry_tile ==
                        self.grid['cells'][action['x']][action['y']]['color'])
        is_hole = self.grid['cells'][action['x']][action['y']]['h'] < 0

        is_valid = is_near and has_tile and colors_match
        if is_valid:
            points = REWARD
            if self.grid['cells'][action['x']][action['y']]['h'] == -1:
                points = points + BONUS
            rewarder = [agent for agent in self.agents if 
                        agent.color == color][0]
            rewarder.points += points
            cell = self.grid['cells'][action['x']][action['y']] 
            cell['h'] = cell['h'] + 1
            action.update({'points': points})
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'OK'})
        else:
            action.update({'points': 0})
            self.send(requester, {'type': 'response_action',
                                  'action': action,
                                  'status': 'FAIL'})

    def transfer_points(self, from_agent, to_agent, value):
        """Tranfers points from one agent to another."""
        for agent in self.agents:
            if agent.name == from_agent:
                agent.points = agent.points - value
            if agent.name == to_agent:
                agent.points = agent.points + value
        self.send(from_agent, {'type': 'response_transfer_points',
                              'from': from_agent,
                              'value': value,
                              'to': to_agent,
                              'status': 'OK'})

    def send_the_end(self):
        """Sends a the_end message to all agents. This is the last message sent.
        """
        message = {'type': 'the_end'}
        for agent in self.agents:
            self.send(agent.name, message)


############################# D I S P L A Y #################################

    def display_grid(self, grid):
        """Displays the current state of the environment grid."""
        self.display_lock.acquire()
        print '--------------------------------'
        print "[T = %s]" % int(time.time())
        print '--------------------------------'
        for i in range(0, grid['H']):
            for j in range(0, grid['W']):
                display_cell(grid['cells'][i][j], self.agents)
            print ''
        print '--------------------------------'
        self.display_lock.release()

    def _safe_print(self, message):
        """Logs message to standard output. Uses a lock to prevent dithering
        messages from agents.
        """
        self.display_lock.acquire()
        print "[%s] %s" % (self.name, message)
        self.display_lock.release()

############################# U T I L S #################################

    def localize(self, requester):
        """Returns the agent position within the grid.""" 
        for i in range(0, self.grid['H']):
            for j in range(0, self.grid['W']):
                for agent in self.grid['cells'][i][j]['agents']:
                    if agent[0] == requester:
                        return (i, j)

        self._safe_print("[E] Agent not found!")
        return None

    def exists_tile(self, x, y, color):
        """Returns True if a tile with color=color exists on (x,y) cell within
        the grid.
        """
        for tile_color in self.grid['cells'][x][y]['tiles']:
            if tile_color == color:
                return True
        return False
