def rotateRight(dir):
    x, y = dir
    return (-y, x)


def stepForward(pos, dir, blocks):
    newpos = tuple(a+b for a, b in zip(pos, dir))
    if newpos not in blocks:
        return newpos, dir
    else:
        return pos, rotateRight(dir)


def checkLoop(pos, dir, blocks):

    visited = set()
    while 0 <= pos[0] < xrange and 0 <= pos[1] < yrange:
        newpos = tuple(a+b for a, b in zip(pos, dir))

        if newpos not in blocks:
            pos = newpos

        else:
            dir = rotateRight(dir)
            if (pos, dir) in visited:
                return 1
            visited.add((pos, dir))

    return 0


# Read input
file = open('input.txt').readlines()

data = [x.strip() for x in file]

ans1 = ans2 = 0
blocks = set()

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '#':
            blocks.add((x, y))
        elif char == '^':
            startpos = (x, y)

startdir = (0, -1)

xrange = len(line)
yrange = len(data)


# Move guard, part 1
dir = startdir
pos = startpos

visited = set()
while 0 <= pos[0] < xrange and 0 <= pos[1] < yrange:

    visited.add(pos)
    pos, dir = stepForward(pos, dir, blocks)

print('The answer to part 1: ', len(visited))


for newblock in visited:

    if newblock == startpos:
        continue

    dir = startdir
    pos = startpos

    allblocks = blocks.copy()
    allblocks.add(newblock)
    ans2 += checkLoop(pos, dir, allblocks)

print('The answer to part 2: ', ans2)