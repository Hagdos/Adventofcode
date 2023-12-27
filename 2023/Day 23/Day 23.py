def addLocations(l1, l2):
    return (l1[0]+l2[0], l1[1]+l2[1])

def checkTrail(location, trail):
    return trail[location[0]][location[1]]


def pathLength(trail, path, location, length, pt1):
    if location == (len(trail)-1, len(trail[-1])-2):
        return length

    nextsteps = []

    while len(nextsteps) <= 1:
        nextsteps = []
        for n in findNeighbours(trail, location, pt1):
            if n[0] not in path:
                nextsteps.append(n)


        if len(nextsteps) == 0:
            return 0

        if len(nextsteps) == 1:
            location = nextsteps[0][0]
            if location == (len(trail)-1, len(trail[-1])-2):
                return length+1
            path.add(location)
            length += nextsteps[0][1]


        if len(nextsteps) > 1:
            paths = []
            for n in nextsteps:
                newlocation = n[0]
                newpath = path.copy()
                newpath.add(newlocation)
                newlength = length + n[1]
                paths.append(pathLength(trail, newpath, n[0], newlength, pt1))
            return max(paths)

def findNeighbours(trail, location, pt1):
    slopes = {'<': (0, -1),
              '>': (0, 1),
              '^': (-1, 0),
              'v': (1, 0)}

    neighbours = []
    for step in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbourlocation = addLocations(location, step)
        if neighbourlocation[0] > 0:

            floor = checkTrail(neighbourlocation, trail)
            if pt1:
                if floor == '.':
                    neighbours.append((neighbourlocation, 1))
                elif floor in slopes:
                    if slopes[floor] == step:
                        neighbours.append((addLocations(neighbourlocation, step), 2))
            else:
                if floor == '.' or floor in slopes:
                    neighbours.append((neighbourlocation, 1))

    return neighbours


def findNeighbours2(trail, location):
    slopes = {'<': (0, -1),
              '>': (0, 1),
              '^': (-1, 0),
              'v': (1, 0)}

    neighbours = []
    for step in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbourlocation = addLocations(location, step)
        if neighbourlocation[0] >= 0:

            floor = checkTrail(neighbourlocation, trail)

            if floor == '.' or floor in slopes:
                neighbours.append(neighbourlocation)

    return neighbours

def findNextCrossings(trail, startcrossing):
    nextcrossings = dict()

    for firststep in findNeighbours2(trail, startcrossing):
        seen = {startcrossing, firststep}
        distance = 1

        location = firststep
        nextsteps = []
        while True:
            if location == (len(trail)-1, len(trail[-1])-2):
                nextcrossings[location] = distance
                break

            nextsteps = [n for n in findNeighbours2(trail, location) if n not in seen]

            if len(nextsteps) == 1:
                location = nextsteps[0]
                seen.add(location)
                distance += 1

            else:
                nextcrossings[location] = distance
                break

    return nextcrossings


def mapAllCrossings(trail, start):
    crossings = dict()
    todo = [start]

    while todo:
        crossing = todo.pop()
        crossings[crossing] = findNextCrossings(trail, crossing)

        for c in crossings[crossing]:
            if c not in crossings and c != (len(trail)-1, len(trail[-1])-2):
                todo.append(c)
    return crossings

def findLongestRoute(distances, path, length, location):
    if location == end:
        return length

    if location == (131, 137):
        return length + distances[(131, 137)][end]

    path.add(location)
    nextsteps = [n for n in distances[location] if n not in path]

    if nextsteps:
        return max([findLongestRoute(distances, path.copy(), length+distances[location][n], n) for n in nextsteps])
    return 0




file = open('input.txt').readlines()
trail = [x.strip() for x in file]
ans1 = ans2 = 0

start = (0, 1)
end = (len(trail)-1, len(trail[-1])-2)

distances = mapAllCrossings(trail, start)

ans2 = findLongestRoute(distances, set(), 0, start)

print('The answer to part 1: ', pathLength(trail, set([start]), start, 0, True))
print('The answer to part 2: ', ans2)