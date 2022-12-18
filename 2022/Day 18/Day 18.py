NEIGHBOURS = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))


def findNeighbours(cube):
    for n in NEIGHBOURS:
        neighbour = tuple(cube[d]+n[d] for d in range(3))

        if all(-1 <= neighbour[dim] <= 22 for dim in range(3)):
            yield neighbour


def readInput(filename):
    file = open(filename).readlines()
    cubes = tuple(tuple(int(z) for z in x.strip().split(','))  for x in file)
    return cubes


def solvePart1(filename):
    cubes = readInput(filename)
    ans1 = 0

    for cube1 in cubes:
        for cube2 in findNeighbours(cube1):
            if cube2 not in cubes:
                ans1 += 1

    return ans1

def solvePart2(filename):
    cubes = readInput('input.txt')
    maxx = maxy = maxz = 0
    ans2 = 0
    for c in cubes:
        maxx = max(c[0], maxx)
        maxy = max(c[1], maxy)
        maxz = max(c[2], maxz)

    # Breadth-first search; which surfaces can we reach?

    start = (0, 0, 0)
    visited = set()
    queue = [start]

    while queue:
        cube = queue.pop()
        new = findNeighbours(cube)

        for n in new:
            if n in cubes:
                ans2 += 1
            elif n not in visited:
                queue.append(n)
                visited.add(n)
    return ans2

print('The answer to part 1: ', solvePart1('input.txt'))
print('The answer to part 2: ', solvePart2('input.txt'))