def printMap(location, direction, tiles, walls, filename = 'map.txt'):

    file = open(filename, "w")
    file.write(f'Instruction: {i}\n')
    for row in range(int(max(t.real for t in tiles))+1):
        line = []
        for column in range(int(max(t.imag for t in tiles))+1):
            l = complex(row, column)
            if l == location:
                line.append('X')
            elif l in walls:
                line.append('#')
            elif l in tiles:
                line.append('.')
            else:
                line.append(' ')
        print(''.join(line))
        file.write(''.join(line))
        file.write('\n')
    print()

    return None



def readInput(filename='input.txt'):

    board, instructions = open(filename).read().split('\n\n')

    board = [b for b in board.split('\n')]

    tiles = set()
    walls = set()

    r = 0
    for line in board:
        r += 1
        c = 0
        for char in line:
            c += 1
            if char == '#' or char == '.':
                tiles.add(complex(r, c))
                if char == '#':
                    walls.add(complex(r, c))

    instructions = instructions.strip()
    i = []
    instr = []
    for char in instructions:
        if char.isnumeric():
            i.append(char)
        else:
            instr.append(int(''.join(i)))
            i = []
            instr.append(char)

    instr.append(int(''.join(i)))
    return tiles, walls, instr


# Sets the location way back on the other side on the board;
# and keeps stepping forward until a valid tile is found
def wrapAround(location, direction, tiles):
    size = max(max(t.real for t in tiles), max(t.imag for t in tiles))

    n = location - direction*size

    while n not in tiles:
        n += direction

    return n, direction


# Real part is the row
# Imag part is the column

# Finds the correct edge to jump to
def wrapAround2(location, direction, tiles):

    sides = {}
    sides['A'] = {0: tuple(complex(0, i) for i in range(51, 101)),
                  1: tuple(complex(i, 0) for i in range(151, 201)),
                  'direction': (-1, 0-1j)}

    sides['B'] = {0: tuple(complex(0, i) for i in range(101, 151)),
                  1: tuple(complex(201, i) for i in range(1, 51)),
                  'direction': (-1, 1)}

    sides['C'] = {0: tuple(complex(i, 50) for i in range(1, 51)),
                  1: tuple(complex(i, 0) for i in range(150, 100, -1)),
                  'direction': (0-1j, 0-1j)}

    sides['D'] = {0: tuple(complex(i, 151) for i in range(1, 51)),
                  1: tuple(complex(i, 101) for i in range(150, 100, -1)),
                  'direction': (0+1j, 0+1j)}

    sides['E'] = {0: tuple(complex(i, 50) for i in range(51, 101)),
                  1: tuple(complex(100, i) for i in range(1, 51)),
                  'direction': (0-1j, -1)}

    sides['F'] = {0: tuple(complex(51, i) for i in range(101, 151)),
                  1: tuple(complex(i, 101) for i in range(51, 101)),
                  'direction': (1, 0+1j)}

    sides['G'] = {0: tuple(complex(151, i) for i in range(51, 101)),
                  1: tuple(complex(i, 51) for i in range(151, 201)),
                  'direction': (1, 0+1j)}

    empty = location+direction

    count = 0

    for letter in sides:
        for s in sides[letter]:
            if empty in sides[letter][s] and direction == sides[letter]['direction'][s]:
                count += 1

                i = sides[letter][s].index(empty)
                n = sides[letter][(s+1)%2][i]

                direction = -sides[letter]['direction'][(s+1)%2]

    assert count == 1, f'{count, location, empty, direction}'
    n = n + direction

    return n, direction


def moveForward(location, direction, steps, tiles, walls, part):
    for _ in range(steps):
        n = location+direction
        if n not in tiles:
            if part == 1:
                n, newdirection = wrapAround(location, direction, tiles)
            elif part == 2:
                n, newdirection = wrapAround2(location, direction, tiles)

            if n not in walls:
                direction = newdirection

        if n in walls:
            return location, direction

        location = n

    return location, direction


def calcScore(location, direction):
    if direction == 0+1j:
        facing = 0 # Facing is 0 for right (>)
    elif direction == 1+0j:
        facing = 1  # 1 for down (v)
    elif direction == 0-1j:
        facing = 2  #  2 for left (<)
    elif direction == 0-1j:
        facing = 3  # and 3 for up (^).

    #The final password is the sum of 1000 times the row, 4 times the column, and the facing.

    return int(location.real*1000+location.imag*4+facing)



tiles, walls, instructions = readInput('input.txt')

# =============================================================================
# Part 1
# =============================================================================

# Vertical (rows) are the real part, Horizonal (columns), are the complex part
# Top-left corner = 1,1
location = 1+1j
direction = 0+1j
location, direction = wrapAround(location, direction, tiles)

for i in instructions:

    if isinstance(i, int):
        location, direction = moveForward(location, direction, i, tiles, walls, 1)
    elif i == 'R':
        direction *= -1j
    elif i == 'L':
        direction *= 1j
    else:
        raise ValueError

ans1 = calcScore(location, direction)
print('The answer to part 1: ', ans1)


# =============================================================================
# Part 2
# =============================================================================
location = 1+1j
direction = 0+1j
location, direction = wrapAround(location, direction, tiles)

for i in instructions:

    if isinstance(i, int):
        location, direction = moveForward(location, direction, i, tiles, walls, 2)
    elif i == 'R':
        direction *= -1j
    elif i == 'L':
        direction *= 1j
    else:
        raise ValueError

ans2 = calcScore(location, direction)
print('The answer to part 2: ', ans2)