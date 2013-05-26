import sys
from threading import Lock
import time

from agents.environment import Environment
from agents.cognitive_agent import CognitiveAgent
from resources.constants import DEFAULT_INPUT_FILE
from resources.utils import parse_file, bfs


# check parameters
if len(sys.argv) > 2:
    print "Invalid arguments. Usage: tile_world.py [input_file]"
    sys.exit(0)

input_file = DEFAULT_INPUT_FILE
if len(sys.argv) == 2:
    input_file = sys.argv[1]

# read input_file
# N: the number of agents
# t: time that it takes to perform an operation on the environment
# T: total time of the simulation
# W, H: width and height of the grid
# colors: N colors of the agents
# pos: N zero-based integers - the initial positions of the agents
# obstacles: pairs of coordinates for obstacles
t, T, grid, agent_data = parse_file(input_file)

agents = []
for data in agent_data:
    agents.append(CognitiveAgent(data[0], data[1], data[2], data[3]))

N = len(agents)

threads = []

environment = Environment(t, T, grid, agents)

# lock printing to stdout
display_lock = Lock()
environment.display_lock = display_lock
for agent in agents:
    agent.display_lock = display_lock

# let all agents know about all each other's queues
queues = {}
queues[environment.name] = (environment.queue, environment.queue_lock)
for agent in agents:
    queues[agent.name] = (agent.queue, agent.queue_lock)

environment.queue_system = queues
for agent in agents:
    agent.queue_system = queues

# run cognitive agent on different threads
agent_threads = []
for agent in agents:
    threads.append(agent)
threads.append(environment)

# start all threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print "Done."
