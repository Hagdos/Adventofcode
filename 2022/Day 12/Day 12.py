def createMap(inputfile):
    file = open(inputfile).readlines()
    data = [x.strip() for x in file]
    map = [[0]*len(data[0]) for _ in range(len(data))]
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
                char = 'a'
            elif char == 'E':
                goal = (r, c)
                char = 'z'
            map[r][c] = ord(char)-ord('a')

    return map, start, goal


def printMap(map, location, goal):
    map[location[0]][location[1]] = ord(' ')-ord('a')
    map[goal[0]][goal[1]] = ord('■')-ord('a')
    for row in map:
        print(''.join([chr(c+ord('a')) for c in row]))
    print('\n')


def checkNeighbours(map, loc):
    rowwidth = len(map[0])
    columnheight = len(map)
    height = map[loc[0]][loc[1]]
    validneighbours = set()
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= loc[0]+dr < columnheight and 0 <= loc[1]+dc < rowwidth:
            if map[loc[0]+dr][loc[1]+dc] <= height+1:
                validneighbours.add((loc[0]+dr, loc[1]+dc))

    return validneighbours


def checkNeighbours2(map, loc):
    rowwidth = len(map[0])
    columnheight = len(map)
    height = map[loc[0]][loc[1]]
    validneighbours = set()
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= loc[0]+dr < columnheight and 0 <= loc[1]+dc < rowwidth:
            if map[loc[0]+dr][loc[1]+dc] >= height-1:
                validneighbours.add((loc[0]+dr, loc[1]+dc))

    return validneighbours


def findPathLength(map, start, goal):
    location = start
    steps = 0
    options = [(steps, location)]
    found = False
    visited = set([start])
    while not(found) and options:
        steps, location = options.pop()
        newLocations = checkNeighbours(map, location)
        steps += 1
        for loc in newLocations:
            if loc == goal:
                return steps

            if loc not in visited:
                visited.add(loc)
                options.append((steps, loc))

        options.sort(key=lambda a: a[0], reverse=True)

    return 10000  # no path found


def findBestPath(map, start):
    location = start
    steps = 0
    options = [(steps, location)]
    found = False
    visited = set([start])
    while not(found):
        steps, location = options.pop()
        newLocations = checkNeighbours2(map, location)
        steps += 1
        for loc in newLocations:
            if map[loc[0]][loc[1]] == 0:
                return steps
            if loc not in visited:
                visited.add(loc)
                options.append((steps, loc))

        options.sort(key=lambda a: a[0], reverse=True)


map, start, goal = createMap('2022/Day 12/input.txt')
print('The answer to part 1: ', findPathLength(map, start, goal))
print('The answer to part 2: ', findBestPath(map, goal))

startingpoints = set()
for r, row in enumerate(map):
    for c, char in enumerate(row):
        if char == 0:
            startingpoints.add((r, c))

best = 1000
for start in startingpoints:
    length = findPathLength(map, start, goal)
    # print(start, length)
    if length < best:
        best = length
        bestpoint = start

print('The long answer to part 2: ', best)
