def printMap(rocks, sands):
    bottom = 0
    start = 1000
    end = 0
    for point in rocks:
        bottom = max(bottom, point[1])
        start = min(start, point[0])
        end = max(end, point[0])

    for row in range(bottom+1):
        line = []
        for column in range(start, end+1):
            if (column, row) in sands:
                # print('Sand')
                line.append('o')
            elif (column, row) in rocks:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))


def dropGrain(rocks, sands, bottom, grain=(500, 0)):
    while(True):
        if (grain[0], grain[1]+1) not in rocks:
            grain = (grain[0], grain[1]+1)
        elif (grain[0]-1, grain[1]+1) not in rocks:
            grain = (grain[0]-1, grain[1]+1)
        elif (grain[0]+1, grain[1]+1) not in rocks:
            grain = (grain[0]+1, grain[1]+1)
        else:
            return grain

        if grain[1] >= bottom:
            return grain


def readInput(filename):

    file = open(filename).readlines()
    data = [[tuple(int(z) for z in y.split(',')) for y in x.strip().split(' -> ')] for x in file]

    rocks = set()
    bottom = end = 0
    start = 1000
    for line in data:
        for point in line:
            bottom = max(bottom, point[1])
            start = min(start, point[0])
            end = max(end, point[0])

    for line in data:
        prev = line[0]
        for point in line[1:]:
            crange = sorted([prev[0], point[0]])
            rrange = sorted([prev[1], point[1]])

            for c in range(crange[0], crange[1]+1):
                for r in range(rrange[0], rrange[1]+1):
                    rock = (c, r)
                    rocks.add(rock)
            prev = point

    return rocks, bottom, start, end

# Part 2
rocks, bottom, start, end = readInput('2022/Day 14/input.txt')
bottom += 2
for c in range(start-bottom, end+bottom):
    rocks.add((c, bottom))

sands = set()
rest = (1, 1)
ans1 = ans2 = 0

while(rest[1] > 0):
    rest = dropGrain(rocks, sands, bottom)
    if rest[1] > bottom-2 and ans1 == 0:
        ans1 = ans2
    sands.add(rest)
    rocks.add(rest)
    ans2 += 1

printMap(rocks, sands)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
