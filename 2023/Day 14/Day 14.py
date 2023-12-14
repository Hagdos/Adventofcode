import time

def moveNorth(rocks, cubes):
    # rocks.sort() #The rocks should be moved in the right order, and that's not the order of the list.
    # Sort is very costly. Better solution: Move north until cube or wall, then move south until no more rock.
    for i, (r,c) in enumerate(rocks):
        rstart = r
        while r-1 >= 0 and (r-1,c) not in cubes:
            r -= 1
        while (r,c) in rocks and r != rstart:
            r += 1
        rocks[i] = (r,c)
    return rocks

def rotatePlatform(rocks, cubes, size):
    for items in [rocks, cubes]:
        for i, (r,c) in enumerate(items):
            nc = size-r-1
            nr = c
            items[i] = (nr, nc)

    return rocks, cubes


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
cycles = 100000
prevrocks = []

start = time.time()
seen = set()

for i in range(cycles):
    for _ in range(4):

        # printPlatform(rocks, cubes, size)
        rocks = moveNorth(rocks, cubes)
        rocks, cubes = rotatePlatform(rocks, cubes, size)

    t = tuple(rocks)

    print(f'Cycle #: {i}, {time.time()-start}, Score: {countScore(rocks, size)}')
    if t in seen:
        break
    seen.add(t)


    # if i > 80000:
    # printPlatform(rocks, cubes, size)



print('The answer to part 1: ', countScore(rocks, size))
print('The answer to part 2: ', ans2)
