def unvisited_position(marked):
    for row in marked:
        for i in row:
            for j in i:
                if j[0] == ' ':
                    return True
    return False

def possible_move(positions, labyrinth, marked):
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    moves = []
    pairs = { 'L':'R','R':'L', 'U':'D', 'D':'U' }

    for position in positions:
        for k, v in directions.iteritems():
            current_X = position['current'][0]
            current_Y = position['current'][1]

            if labyrinth[position['current'][0] + v[0]][position['current'][1] + v[1]] == ' ':
                moves.append({'direction': k,
                              'current': [position['current'][0] + v[0], position['current'][1] + v[1]],
                              'previous': position['current'] })
            elif marked[current_X][current_Y] in ['1','0'] and marked[current_X + v[0]][current_Y + v[1]] in ['1','0']:
                if int(marked[current_X + v[0]][current_Y + v[1]]) == 0 and int(marked[current_X][current_Y]) == 1:
                    return  { 'found': position,
                                'from_start': {'direction': k,'position': [current_X, current_Y] },
                              'from_dest': {'direction': '', 'position': [current_X + v[0], current_Y + v[1]]} }

                elif int(marked[current_X + v[0]][current_Y + v[1]]) == 1 and int(marked[current_X][current_Y]) == 0:
                    return {'found': position,
                            'from_dest': {'direction': pairs[k], 'position': [current_X, current_Y]},
                            'from_start': {'direction': '', 'position': [current_X + v[0], current_Y + v[1]]} }

    if moves == []:
        return {'found': position, }
    return moves

def mark_steps(possible_move, marked, labyrinth, symbol='1'):
    for step in possible_move:
        moves = possible_move(possible_move, labyrinth)

        for move in moves:
            position = move['current']
            marked[position[0]] = marked[position[0]][:position[1]] + symbol + marked[position[0]][position[1] + 1:]


def labyrinth2(start, dest, labyrinth):
    paths = []

    directions = {'U': (-1, 0), 'R': (0 , 1), 'D': (1, 0), 'L': (0, -1)}

    # S1
    steps_from_start = [{'direction': '', 'current': start, 'previous': start}]
    step_from_dest = [{'direction': '', 'current': dest, 'previous': dest}]
    current_step_from_start = {'direction': '', 'current': start, 'previous': start}
    current_step_from_dest = {'direction': '', 'current': dest, 'previous': dest}

    meet_point = {}
    meet_point = {}

    paths_from_start = []
    paths_from_dest = []
    marked = labyrinth
    marked[start[0]] = marked[start[0]][:start[1]] + '1' + marked[start[0]][start[1] + 1:]
    marked[dest[0]] = marked[dest[0]][:dest[1]] + '0' + marked[dest[0]][dest[1] + 1:]
    possible_steps_from_start = [current_step_from_start]
    possible_steps_from_dest = [current_step_from_dest]

    # S2

    while unvisited_position(marked):
        moves = possible_move(possible_steps_from_start, labyrinth, marked)
        for step in possible_steps_from_start:
            if 'found' in moves:
                meet_point = moves
                break
            else:
                for move in moves:
                    position = move['current']
                    marked[position[0]] = marked[position[0]][:position[1]] + '1' + marked[position[0]][position[1] + 1:]

        if 'found' in moves:
            break

        possible_steps_from_start = moves
        paths_from_start += possible_steps_from_start
        moves = possible_move(possible_steps_from_dest, labyrinth, marked)

        for step in possible_steps_from_dest:
            if 'found' in moves:
                meet_point = moves
                break
            else:
                for move in moves:
                    position = move['current']
                    marked[position[0]] = marked[position[0]][:position[1]] + '0' + marked[position[0]][

                                                                                        position[1] + 1:]
        if 'found' in moves:
            break

        possible_steps_from_dest = moves
        paths_from_dest += possible_steps_from_dest

    # S3: get sequence of commands
    sequence = ''
    opposite_direction = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}
    step = meet_point['from_start']['position']
    sequence += meet_point['from_start']['direction']

    while step != start:
        for position in paths_from_start:
            if step == position['current']:
                sequence += position['direction']
                step = position['previous']

    sequence = sequence[::-1]
    step = meet_point['from_dest']['position']
    sequence += meet_point['from_dest']['direction']

    while step != dest:
        for position in paths_from_dest:
            if step == position['current']:
                sequence += opposite_direction[position['direction']]
                step = position['previous']

    return sequence

def find_start_dest(labyrinth):
    points = []

    for row_idx,row in enumerate(labyrinth):
        if 'S' in row:
            points.append([row_idx, row.find('S')])
        if 'F'  in row:
            points.append([row_idx, row.find('F')])

    return points


if __name__ == '__main__':
    print find_start_dest(
               ["***************",
                "*S    * * *   *",
                "*** *** * *** *",
                "* *     *     *",
                "* * * *** *****",
                "*   * *       *",
                "* * *** * * ***",
                "* *     * *  F*",
                "***************"])

    print labyrinth2([1,1],[5,5],
                     ["*******",
                    "*S    *",
                    "*** * *",
                    "*   * *",
                    "* *****",
                    "*    F*",
                    "*******"]) == 'RRDDLLDDRRRR'

    print labyrinth2([1,1],[3,1],
                     ["***",
                     "*S*",
                     "* *",
                     "*F*",
                     "***"]) == 'DD'

    print labyrinth2([1,1],[1,3],
                     ["*****",
                     "*S F*",
                     "*****"]) == 'RR'

    print labyrinth2([1,1],[9,17],
                     ["*******************",
                      "*S    *   *     * *",
                      "*** *** *** ***** *",
                      "* * *     *       *",
                      "* * * * ***** * * *",
                      "* * * * *     * * *",
                      "* * *** * * ***** *",
                      "* *   * * *     * *",
                      "* * *** * ***** ***",
                      "*           *    F*",
                      "*******************"]) == 'RRDDDDDDDDRRRRRRUUUURRDDRRRRDDRR'

    print labyrinth2([1,1],[7,13],
               ["***************",
                "*S    * * *   *",
                "*** *** * *** *",
                "* *     *     *",
                "* * * *** *****",
                "*   * *       *",
                "* * *** * * ***",
                "* *     * *  F*",
                "***************"]) == 'RRDDDDDDRRRRUURRRRDDRR'
