def findMirrors(inputfile='input.txt'):

    file = open('input.txt').readlines()
    data = [x.strip() for x in file]

    mirrors = dict()

    for r, line in enumerate(data):
        for c, char, in enumerate(line):
            if char in ['|', '-', '/', "\\"]:
                mirrors[(r,c)] = char

    sizer = len(data)
    sizec = len(data[0])

    return mirrors, (sizer, sizec)

def moveForward(location, direction):

    return ((location[0]+direction[0], location[1]+direction[1]), direction)

def nextSteps(location, direction, mirrors):
    if location in mirrors:
        if mirrors[location] == '|' and direction[1] in [-1, 1]:
            newdirections = [(-1, 0), (1, 0)]
            return [moveForward(location, direction) for direction in newdirections]
        elif mirrors[location] == '-' and direction[0] in [-1, 1]:
            newdirections = [(0, -1), (0, 1)]
            return [moveForward(location, direction) for direction in newdirections]
        elif mirrors[location] == '/':
            direction = (-direction[1], -direction[0])
            return [moveForward(location, direction)]
        elif mirrors[location] == '\\':
            direction = (direction[1], direction[0])
            return [moveForward(location, direction)]

    return [moveForward(location, direction)]

def countEnergized(path):
    energized = set()
    for location, direction in path:
        energized.add(location)

    return len(energized)

def traceLight(start, mirrors, size):
    beamends = [start]
    seen = set(beamends)
    energized = set()

    while beamends:
        location, direction = beamends.pop()
        newends = nextSteps(location, direction, mirrors)
        for n in newends:
            if n not in seen:
                if 0 <= n[0][0] < size[0] and 0 <= n[0][1] < size[1]:
                    beamends.append(n)
                    seen.add(n)

    return countEnergized(seen)



def Part1():
    mirrors, size = findMirrors('input.txt')

    location = (0, 0)
    direction = (0, 1)

    print('The answer to part 1: ', traceLight((location, direction), mirrors, size))


def Part2():
    mirrors, size = findMirrors('input.txt')
    ans2 = 0
    for r in range(size[0]):
        location = (r, 0)
        direction = (0, 1)
        ans2 = max(ans2, traceLight((location, direction), mirrors, size))

        location = (r, size[1])
        direction = (0, -1)
        ans2 = max(ans2, traceLight((location, direction), mirrors, size))


    for c in range(size[1]):
        location = (0, c)
        direction = (1, 0)
        ans2 = max(ans2, traceLight((location, direction), mirrors, size))


        location = (size[0], c)
        direction = (-1, 0)
        ans2 = max(ans2, traceLight((location, direction), mirrors, size))

    print('The answer to part 2: ', ans2)


Part1()
Part2()

