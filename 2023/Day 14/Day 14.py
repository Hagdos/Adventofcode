import time

def moveNorth(rocks, cubes):
    newrocks = set()
    for i, (r,c) in enumerate(rocks):
        while r-1 >= 0 and (r-1,c) not in cubes:
            r -= 1
        while (r,c) in newrocks:
            r += 1
        newrocks.add((r,c))
    return newrocks

def rotatePlatform(rocks, cubes, size):
    newrocks = set()
    newcubes = set()
    while rocks:
        r, c = rocks.pop()
        nc = size-r-1
        nr = c
        newrocks.add((nr,nc))

    while cubes:
        r, c = cubes.pop()
        nc = size-r-1
        nr = c
        newcubes.add((nr,nc))

    return newrocks, newcubes


def printPlatform(rocks, cubes, size):
    print('Platform:')
    for r in range(size):
        line = []
        for c in range(size):
            if (r,c) in rocks:
                line.append('O')
            elif (r,c) in cubes:
                line.append('#')
            else:
                line.append(' ')
        print(''.join(line))
    print('\n')

def countScore(rocks, size):
    score = 0
    for r,c in rocks:
        score += size-r

    return score

def runcycle(rocks, cubes, size):
    for _ in range(4):

        # printPlatform(rocks, cubes, size)
        rocks = moveNorth(rocks, cubes)
        rocks, cubes = rotatePlatform(rocks, cubes, size)

    return rocks, cubes

file = open('input.txt').readlines()

data = [x.strip() for x in file]
ans1 = ans2 = 0

cubes = []
rocks = []

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == '#':
            cubes.append((r,c))
        if char == 'O':
            rocks.append((r,c))

size = len(data)
cycles = 1000000000
# cycles = 1000
prevrocks = []

cubes = set(cubes)
rocks = set(rocks)

start = time.time()
seen = dict()


rocks = moveNorth(rocks, cubes)
print('The answer to part 1: ', countScore(rocks, size))

for i in range(cycles):
    rocks, cubes = runcycle(rocks, cubes, size)

    print(f'Cycle #: {i}, {time.time()-start}, Score: {countScore(rocks, size)}')
    # start = time.time()

    # if i > 80000:
    # printPlatform(rocks, cubes, size)

    t = tuple(rocks)
    if t in seen.keys():
        break
    seen[t] = i


cyclelength = i-seen[t]
cyclesToGo = (cycles - i - 1)%cyclelength

for _ in range(cyclesToGo):
    rocks, cubes = runcycle(rocks, cubes, size)



print('The answer to part 2: ', countScore(rocks, size))
