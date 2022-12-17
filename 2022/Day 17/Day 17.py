# Definition time!:
# The bottom left corner within the walls is 0, 0 (r, c); with r=0 the floor
# The bottom left corner of each shape is also 0, 0 (even if it's empty)

# ####
SHAPE1 = ((0,0), (0, 1), (0, 2), (0, 3))

# .#.
# ###
# .#.
SHAPE2 = ((2, 1), (1, 0), (1, 1), (1, 2), (0, 1))

# ..#
# ..#
# ###
SHAPE3 = ((2, 2), (1, 2), (0, 0), (0, 1), (0, 2))

# #
# #
# #
# #
SHAPE4 = ((3, 0), (2, 0), (1, 0), (0, 0))

# ##
# ##
SHAPE5 = ((1, 0), (1, 1), (0, 0), (0, 1))

SHAPES = (SHAPE1, SHAPE2, SHAPE3, SHAPE4, SHAPE5)


def initshapegen(SHAPES):
    counter = 0
    while(True):
        s = SHAPES[counter]
        counter += 1
        counter %= 5
        yield s


def initjetsgen(filename):
    commands = open(filename).read().strip()
    # commands = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    # print(len(commands))
    counter = 0
    while True:
        if commands[counter] == '>':
            yield (0, 1), counter
        elif commands[counter] == '<':
            yield (0, -1), counter
        else:
            raise ValueError
        counter += 1
        counter %= len(commands)


def moveShape(shape, direction, solidpoints):
    newshape = set()
    for loc in shape:
        newshape.add((loc[0]+direction[0], loc[1]+direction[1]))

    newshape=tuple(newshape)

    if checkCollision(newshape, solidpoints):
        return shape

    return newshape


def moveShapeSafe(shape, direction):
    newshape = set()
    for loc in shape:
        newshape.add((loc[0]+direction[0], loc[1]+direction[1]))

    newshape=tuple(newshape)

    return newshape


def topRows(solidpoints, highestpoint):
    spoints = set()
    for point in solidpoints:
        if point[0] >= highestpoint-5:
            spoints.add((point[0]-highestpoint, point[1]))

    return spoints


def checkCollision(shape, solidpoints):
    for point in shape:
        if point in solidpoints:
            return True
        if not 0 <= point[1] < 7:
            return True

    return False


def landShape(shape, highestpoint, solidpoints):
    for point in shape:
        solidpoints.add(point)
        highestpoint = max(highestpoint, point[0])
    return highestpoint


def printChute(solidpoints, shape, highestpoint):
    for r in range(highestpoint + 5, -2, -1):
        line = []
        for c in range(7):
            if (r, c) in shape:
                line.append('@')
            elif (r, c) in solidpoints:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))
    print()
    input()



def solve(filename, n):

    # Add the floor
    solidpoints = {(0, y) for y in range(7)}
    highestpoint = 0

    shapesgen = initshapegen(SHAPES)
    jetsgen = initjetsgen(filename)
    seen = dict()

    repetition = False

    blocks = 0
    dheight = 0
    while blocks<n:

        shape = moveShape(next(shapesgen), (highestpoint+4, 2), solidpoints)

        while(True):
            # printChute(solidpoints, shape, highestpoint)
            jet, counter = next(jetsgen)
            if counter == 0:
                s = moveShapeSafe(shape, (-highestpoint, 0))
                lines = tuple(topRows(solidpoints, highestpoint))
                state = tuple((s, lines))

                if state in seen:
                    dblocks = blocks - seen[state][0]
                    dheight = highestpoint - seen[state][1]
                    repetition = True

                    repetitions = (n - blocks)//dblocks
                    dheight *= repetitions
                    blocks += dblocks*repetitions

                seen[state] = (blocks, highestpoint)


            shape = moveShape(shape, jet, solidpoints)

            s = shape
            shape = moveShape(shape, (-1, 0), solidpoints)

            if shape == s:
                highestpoint = landShape(shape, highestpoint, solidpoints)
                break
        blocks += 1

    return highestpoint+dheight

print(solve('input.txt', 2022))
print(solve('input.txt', 1000000000000))
