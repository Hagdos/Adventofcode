from operator import add


def step(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def moveTail(head, tail):
    dx = head[0]-tail[0]
    dy = head[1]-tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        tail[1] += step(dy)
        tail[0] += step(dx)
    return tail


def solvePuzzle(ropelength):

    knots = [[0, 0] for _ in range(ropelength)]

    taillocations = set()
    direction = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for dir, steps in instructions:
        for _ in range(int(steps)):
            knots[0] = list(map(add, knots[0], direction[dir]))
            for i in range(1, len(knots)):
                knots[i] = moveTail(knots[i-1], knots[i])

            taillocations.add(tuple(knots[-1]))

    return len(taillocations)


file = open('2022/Day 9/input.txt').readlines()
instructions = [x.strip().split(' ') for x in file]

print('The answer to part 1: ', solvePuzzle(2))
print('The answer to part 2: ', solvePuzzle(10))
