def printmap(clay, water, rows):
    for row in range(miny, min(miny+rows, maxy+1)):
        line = ''
        for column in range(minx, maxx+1):
            if (column, row) in water:
                line += '~'
            elif (column, row) in fallingwater:
                line += '|'
            elif (column, row) in clay:
                line += '#'
            else:
                line += ' '
        print(line)
    print()


def checkSides(start, clay, water):
    layer = set()
    layer.add(start)
    new = []
    # Check left side
    left = start
    edge = False
    while not edge:
        left = (left[0]-1, left[1])
        below = (left[0], left[1]+1)
        if left in clay:
            edge = True
        elif below not in clay and below not in water:
            new.append(left)
            edge = True
        else:
            layer.add(left)

    # Check right side
    right = start
    edge = False
    while not edge:
        right = (right[0]+1, right[1])
        below = (right[0], right[1]+1)
        if right in clay:
            edge = True
        # elif right in water:
        #     edge = True
        elif below not in clay and below not in water:
            new.append(right)
            edge = True
        else:
            layer.add(right)

    if not new:
        water.update(layer)
        above = (start[0], start[1]-1)
        new = checkSides(above, clay, water)
    else:
        fallingwater.update(layer)

    return new


# Read input file, and create a set with all clay locations
def readInput(filename):
    file = open(filename).readlines()

    clay = set()
    for line in file:
        vein = dict()
        inputs = line.strip().split(', ')
        for i in inputs:
            c, v = i.split('=')
            vein[c] = [int(i) for i in v.split('..')]

        if len(vein['x']) == 1:
            for y in range(vein['y'][0], vein['y'][1]+1):
                clay.add((vein['x'][0], y))
        else:
            for x in range(vein['x'][0], vein['x'][1]+1):
                clay.add((x, vein['y'][0]))

    return clay


filename = '2018/Day 17/input.txt'
clay = readInput(filename)

minx, maxx = min([c[0] for c in clay]), max([c[0] for c in clay])
miny, maxy = min([c[1] for c in clay]), max([c[1] for c in clay])

# Create a source of water, and check the flow

front = [(500, miny)]
fallingwater = set()
water = set()

while front:
    f = front.pop()

    if f[1] == maxy+1:
        continue
    if f in fallingwater:
        continue
    fallingwater.add(f)

    lower = (f[0], f[1]+1)

    if lower in clay:
        new = checkSides(f, clay, water)
        front += new
    elif lower in water:
        new = checkSides(lower, clay, water)
        front += new
    else:
        front.append(lower)

printmap(clay, water, 20000)


print('The answer to part 2: ', len(water))

for w in fallingwater:
    water.add(w)

print('The answer to part 1: ', len(water))
