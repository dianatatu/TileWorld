from copy import copy
from Queue import Queue
from termcolor import cprint

from resources.cell import Cell
from resources.constants import NONE_COLOR, TD, OBSTACLE_HEIGHT, NONE_COLOR


def parse_file(input_file):
    """ Returns all necessary values parsed from the input file."""

    f = open(input_file, 'r')
    l = f.read().split()

    N, t, T, W, H = [int(x) for x in l[:5]]
    colors = l[5:5+N]
    pos = []
    for i in range(5+N, 5+3*N, 2):
        pos.append((int(l[i]), int(l[i+1])))

    # skip 'OBSTACLES' token
    index = 5+3*N+1
    obstacles = []
    while l[index] != 'TILES':
        obstacles.append((int(l[index]), int(l[index+1])))
        index = index + 2

    # skip 'TILES' token
    index = index + 1
    tiles = []
    while l[index] != 'HOLES':
        tiles.append((int(l[index]), l[index+1], int(l[index+2]), int(l[index+3])))
        index = index + 4

    # skip 'HOLES' token
    index = index + 1
    holes = []
    while index != len(l):
        holes.append((int(l[index]), l[index+1], int(l[index+2]), int(l[index+3])))
        index = index + 4

    f.close()

    agents = []
    for i in range(0, N):
        agents.append(("agent%s" % i, pos[i][0], pos[i][1], colors[i]))

    grid = {}
    grid['H'] = H
    grid['W'] = W
    grid['cells'] = []
    for i in range(0, W):
        grid['cells'].append([])
    for i in range(0, H):
        for j in range(0, W):
            h = get_height(i, j, obstacles, holes)
            color = get_color(i, j, holes)
            cell_tiles = get_tiles(i, j, tiles)
            cell_agents = get_agents(i, j, agents)
            grid['cells'][i].append(Cell(i, j, h, color, cell_tiles, cell_agents).__dict__)

    return (t, T, grid, agents)


def get_height(i, j, obstacles, holes):
    """Returns the height of the cell on line i and column j.

    If the cell is an obstacle, then its height will be OBSTACLE_HEIGHT.
    If the cell is a hole, then its height will be negative.
    Otherwise, the cell's height is 0.
    """
    for obs in obstacles:
        if obs[0] == i and obs[1] == j:
            return OBSTACLE_HEIGHT
    for hole in holes:
        if hole[2] == i and hole[3] == j:
            return 0-hole[0];
    return 0;


def get_color(i, j, holes):
    """Returns the color of the cell on line i and column j.

    If the cell is a hole, then its color will be set by the hole's color.
    Otherwise, the cell has no color.
    """
    for hole in holes:
        if hole[2] == i and hole[3] == j:
            return hole[1];
    return NONE_COLOR


def get_tiles(i, j, tiles):
    """Returns all tiles corresponding to a single cell from grid.
    (the one from line i and column j).
    """
    cell_tiles = []
    for tile in tiles:
        if tile[2] == i and tile[3] == j:
            for _ in range(0, tile[0]):
                cell_tiles.append(tile[1])
    return cell_tiles

def get_agents(i, j, agents):
    """Returns all agents situated on a (i, j) tile."""
    cell_agents = []
    for agent in agents:
        if agent[1] == i and agent[2] == j:
            cell_agents.append(agent)
    return cell_agents


############################# DISPLAY #################################

def display_cell(cell, agents):
    # display height
    if cell['color'] is not NONE_COLOR:
        if cell['h']<0:
            cprint('%d\t\t' % cell['h'], cell['color'], end='')
        if cell['h']==0:
            cprint(' %d\t\t' % cell['h'], cell['color'], end='')
        return
    if cell['h'] < 0:
        # hole
        print('%d' % cell['h']),
    elif cell['h'] == 0:
        # tile
        print(' %d' % cell['h']),
    else:
        # obstacle
        print(' #'),
    #display tiles
    if cell['tiles']:
        for tile in cell['tiles']:
            cprint('*', tile, end='')
    # display agent
    for agent in agents:
        if agent.x == cell['x'] and agent.y == cell['y']:
            cprint(',%d$' % agent.points, agent.color, end='')
            if agent.carry_tile:
                cprint('* ', agent.carry_tile, end='')
    print('\t\t'),

def bfs(start_x, start_y, stop_x, stop_y, grid):
    """A BFS traversal of a 2D grid. The agent stop when he reaches the stop
    cell."""
    q = Queue()
    temp_path = [(start_x, start_y)]
    q.put(temp_path)

    while not q.empty():
        tmp_path = q.get()
        last_node = tmp_path[len(tmp_path)-1]

        if last_node == (stop_x, stop_y):
            return tmp_path[1:]

        next = up(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = down(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = left(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = right(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

def near_bfs(start_x, start_y, stop_x, stop_y, grid):
    """A BFS traversal of a 2D grid. The agent stop when is near stop cell."""
    q = Queue()
    temp_path = [(start_x, start_y)]
    q.put(temp_path)

    while not q.empty():
        tmp_path = q.get()
        last_node = tmp_path[len(tmp_path)-1]

        if is_near(last_node, stop_x, stop_y):
            return tmp_path[1:]

        next = up(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = down(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = left(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

        next = right(last_node, grid)
        if next and next not in tmp_path:
            new_path = []
            new_path = tmp_path + [next]
            q.put(new_path)

def is_near(cell, x, y):
    if ( (abs(cell[0]-x) == 1 and cell[1]==y) or
         (abs(cell[1]-y) == 1 and cell[0]==x)):
            return True
    return False

def up(position, grid):
    if position[0]==0: return None
    next_x = position[0]-1
    next_y = position[1]

    if grid['cells'][next_x][next_y]['h'] != 0:
        return None
    return (next_x, next_y)

def down(position, grid):
    if position[0]==grid['H']-1: return None
    next_x = position[0]+1
    next_y = position[1]

    if grid['cells'][next_x][next_y]['h'] != 0:
        return None
    return (next_x, next_y)

def left(position, grid):
    if position[1]==0: return None
    next_x = position[0]
    next_y = position[1]-1

    if grid['cells'][next_x][next_y]['h'] != 0:
        return None
    return (next_x, next_y)

def right(position, grid):
    if position[1]==grid['W']-1: return None
    next_x = position[0]
    next_y = position[1]+1

    if grid['cells'][next_x][next_y]['h'] != 0:
        return None
    return (next_x, next_y)
