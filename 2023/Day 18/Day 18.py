def move(location, direction):
    return ((location[0]+direction[0], location[1]+direction[1]))

def drawMap(dug, filename = "map.txt"):
    f = open(filename, "w")
    minr = minc = 0
    maxr = maxc = 0

    for d in dug:
        minr = min(minr, d[0])
        maxr = max(maxr, d[0])
        minc = min(minc, d[1])
        maxc = max(maxc, d[1])

    for r in range(minr, maxr+1):
        line = []
        for c in range(minc, maxc+1):

            if (r,c) == (0, 0):
                line.append('0')
            elif (r,c) in dug:
                line.append('#')
            else:
                line.append(' ')
        f.write(''.join(line))
        f.write('\n')
    f.close()
    return None


def floodfill(dug, origin=(0,0)):
    border = [origin]

    while border:
        location = border.pop()
        for d in direction.values():
            n = move(location, d)
            if n not in dug:
                dug.add(n)
                border.append(n)

    return dug


def readhex(hexcode):
    d = direction2[int(hexcode[-2])]
    distance = int(hexcode[2:-2], 16)

    return distance, d

file = open('input.txt').readlines()

instructions = [x.strip().split() for x in file]

ans1 = ans2 = 0

direction = {'U': (-1, 0),
             'D': (1, 0),
             'L': (0, -1),
             'R': (0, 1)}

direction2 = {3: (-1, 0),
              1: (1, 0),
              2: (0, -1),
              0: (0, 1)}

position = (0,0)
dug = set([position])

for command, length, colour in instructions:
    d = direction[command]
    for _ in range(int(length)):
        position = move(position, d)
        dug.add(position)

    length2, d2 = readhex(colour)

    print(length2/int(length), d, d2)


drawMap(dug)
# dug = floodfill(dug, (1, 1))


print('The answer to part 1: ', len(dug))
print('The answer to part 2: ', ans2)

# Rough idea:
    # First only store the corners, and make a list of rows that have corners.
    # Then iterate the instructions, and make a list of vertical wall units for the rows that have a corner (Only vertical! But including the corners)
    # Then for each row, calculate the width between vertical wall units, and multiply it with the height between rows