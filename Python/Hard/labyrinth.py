import numpy as np
from fractions import gcd

def maze(labyrinth, start, dest):
    direction = {
        'U':(-1,0),
        'R':(0,1),
        'D':(1,0),
        'L':(0,-1)
    }
    solution = []

    def move(labyrinth, dest, steps, current_position):
        if (current_position['x'] > len(labyrinth) - 1 or current_position['x'] < 0) \
            or (current_position['y'] > len(labyrinth[0]) - 1 or current_position['y'] < 0) \
            or labyrinth[current_position['x']][current_position['y']] == '*' \
            or labyrinth[current_position['x']][current_position['y']] == 'x':
            return False
        elif (current_position['x'], current_position['y']) == dest:
            solution = steps
            for i in labyrinth:
                print i
            return True
        labyrinth[current_position['x']][current_position['y']] = 'x'

        if move(labyrinth, dest, steps, {'x': current_position['x'] + direction['U'][0], 'y': current_position['y'] + direction['U'][1]}) == True:
            steps.append('U')
            return True
        elif move(labyrinth, dest, steps, {'x':current_position['x'] + direction['R'][0], 'y': current_position['y'] + direction['R'][1]}) == True:
            del steps[-1]
            steps.append('R')
            return True
        elif move(labyrinth, dest, steps, {'x': current_position['x'] + direction['D'][0], 'y': current_position['y'] + direction['D'][1]}) == True:
            del steps[-1]
            steps.append('D')
            return True
        elif move(labyrinth, dest, steps, {'x': current_position['x'] + direction['L'][0], 'y': current_position['y'] + direction['L'][1]}) == True:
            del steps[-1]
            steps.append('L')
            return True
        #/get stuck in a corner, then move back 1 step
        labyrinth[current_position['x']][current_position['y']] = '.'
        return False

    move(labyrinth, dest, [], {'x': start[0], 'y': start[1]})

def bfs(labyrinth, start, dest):
    direction = {'L':(0,-1),
                 'U':(-1,0),
                 'D':(1,0),
                 'R':(0,1)}
    clockwise = {0:'U', 1: 'R', 2: 'D', 3: 'L'}

    if start[0] == dest[0] and start[1] == dest[1]:
        labyrinth[start[0]][start[1]][0] = 'x'
        return 0

    if labyrinth[start[0]][start[1]][0] == '*':
        return 0
    else:
        if labyrinth[start[0]][start[1]][0] == '.':
            labyrinth[start[0]][start[1]][0] = 'x'
        else:
            return 0

    for i in xrange(4):
        if start[1] + direction[clockwise[i]][1] >= 0 and start[1] + direction[clockwise[i]][1] < len(labyrinth[1]) \
            and start[0] + direction[clockwise[i]][0] >= 0 and start[0] + direction[clockwise[i]][0] < len(labyrinth):
            bfs(labyrinth, [start[0] + direction[clockwise[i]][0],start[1] + direction[clockwise[i]][1]], dest)
        else:
            continue

class mod:
    steps = 0

class Node:
    row = 0
    column = 0
    sequence = []
    deltaX = 0
    deltaY = 0

def estimate_sequence_length(maze, current_node):
    length = 0
    landing_row = current_node.row + current_node['mod']['steps']*current_node['mod']['row']
    landing_column = current_node.column + current_node['mod']['steps']*current_node['mode']['column']
    sight_disc_score = 0
    loop_close_x = current_node['mod']['column']
    loop_close_y = current_node['mod']['row']

    if current_node.state >= 3:
        length = current_node.sequence.length
        loop_close_x -= current_node.deltaX
        loop_close_y -= current_node.deltaY

    if current_node.state <= 3:
        sight_disc = current_node['aim']['sight_disc']

        if landing_row >= 0 and landing_row < sight_disc.length and landing_column >= 0:
            sight_disc_score = sight_disc[landing_row][landing_column]
        else:
            sight_disc_score = None

        if sight_disc_score == None:
            sight_disc_score = abs(landing_row - maze['dest']['row']) \
            + abs(landing_column - maze['dest']['column'])

        if current_node.state == 3:
            if sight_disc_score == 0:
                current_node.state = 4
                current_node['mod']['steps'] -= 1

        if current_node.state <= 3:
            loop_close_x += landing_column - maze['dest']['column']
            loop_close_y += landing_row - maze['dest']['row']

        current_node['estimate'] = length + sight_disc_score + abs(loop_close_x) \
        + abs(loop_close_y)

    return current_node

def wall_test(maze, current_node):
    steps = current_node['mod']['steps']
    walls = maze.walls

    for i in xrange(steps):
        row = current_node['row'] + i*current_node['mod']['row']
        column = current_node['column'] + i*current_node['mod']['column']

        if row < 0 or row >= walls.length \
                or column < 0 or column >= walls['row'].length \
                or walls[row][column] == '*':
            return True

    return False

def explode_node(maze, current_node):
    DIRECTIONS = "RDLU"
    result = []

    if current_node['state']== 0:
        sight_disc = maze['walls']
        row = maze['dest']['row']
        column = maze['dest']['column']
        sight_disc[row][column] = 0

        result.append({'state':1,
                       'aim': {
                           'row': row,
                           'column': column,
                           'distance' : 0,
                           'sight_disc': sight_disc
                       },
                       'estimate': 0
        })
        return

    if current_node['state'] == 1: #phase 1
        dx = 1
        dy = 0
        for i in xrange(3):
            row = current_node['aim']['row'] + dy
            column = current_node['aim']['column'] + dx
            tmp = dx
            dx = -dy
            dy = tmp
            distance = current_node['aim']['distance'] + 1
            sight_disc = current_node['aim']['sight_disc']
            candidate = {
                'row': row,
                'column': column,
                mod: {
                    'row': 0,
                    'column': 0,
                    'steps': 0
                }
            }

            if wall_test(maze, candidate) == False:
                visited = sight_disc['row']['column']

                if visited != None:
                    continue

                sight_disc['row']['column'] = distance
                result.append({'state': 1, 'aim': {
                    'row': row,
                    'column': column,
                    'distance': distance,
                    'sight_disc': sight_disc
                    },
                'estimate': distance
                })

            aim = current_node['aim']
            start = maze['start']
            delta_x = aim['column'] - start['column']
            delta_y = aim['row'] - start['row']
            steps = gcd(delta_x, delta_y)
            dir_x = delta_x / steps
            dir_y = delta_y / steps

        for factor in xrange(1, steps + 1):
            result.append(estimate_sequence_length(maze,
           {'state': 3,
            'aim': aim,
            'mod': {
                'row': factor * dir_y,
                'column': factor * dir_x,
                'steps': steps / factor,
            },
            'row' : start['row'],
            'column': start['column'],
            'sequence': '',
            'delta_x': 0,
            'delta_y': 0,
            'visited': [],
            'estimate': None
            }))

        if current_node['state'] == 4:
            row = current_node['row']
            column = current_node['column']
            visited = current_node['visited']
            visState = visited[current_node['state']]
            visRow = visState['row']
            visCell = visRow['column']
            length = current_node['sequence'].length

            if visCell != None and visCell <= length:
                return

            dx = 1
            dy = 0

            for i in range(4):
                tmp = dx
                dx = -dy
                dy = tmp
                candidate = {
                    'state': current_node['state'],
                    'aim': current_node['aim'],
                    'mod': current_node['mod'],
                    'row': row + dy,
                    'column': column + dx,
                    'sequence': current_node['sequence'] + DIRECTIONS[i-1],
                    'delta_x': current_node['delta_x'] + dx,
                    'delta_y': current_node['delta_y'] + dy,
                    'visited': current_node['visited'],
                    'estimate': None
                }

                estimate_sequence_length(maze, candidate)

                if wall_test(maze, candidate) == False:
                    result.append(candidate)

    return



if __name__ == '__main__':
    labyrinth = []
    labyrinth.append([["."], ["."], ["."], ["."], ["."], ["."], ["."]])
    labyrinth.append([["."], ["."], ["."], ["*"], ["."], ["*"], ["."]])
    labyrinth.append([["*"],["."],["."],["."],["."],["*"],["."]])
    labyrinth.append([["."], ["."], ["."], ["."], ["."], ["."], ["."]])
    labyrinth.append([["."],["*"],["*"],["."],["."],["."],["."]])


    #maze(labyrinth, [3,6], [0,0])
    bfs(labyrinth,[0,0],[3,6])
    for i in labyrinth:
        x = ''
        for j in i:
            x += j[0]
        print x


