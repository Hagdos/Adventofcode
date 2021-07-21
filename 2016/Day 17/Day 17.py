import hashlib

passcode = 'vwbaicqe'

direction = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
step = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}

location = (0, 0)
path = ''

heads = [(location, path)]
fullpaths = []
vaultFound = False

while vaultFound is False and heads:
    shortestPath = 100000
    for i, head in enumerate(heads):
        if len(path) < shortestPath:
            shortestPath = len(path)
            index = i

    location, path = heads.pop(index)

    doors = hashlib.md5((passcode + path).encode()).hexdigest()[:4]

    for i, char in enumerate(doors):
        if char in ['b', 'c', 'd', 'e', 'f']:
            newLocation = tuple(x+y for x, y in zip(location, step[i]))
            if all(p in range(4) for p in newLocation):
                newPath = path + direction[i]
                heads.append((newLocation, newPath))
                if newLocation == (3, 3):
                    if vaultFound is False:
                        print('The answer to Part 1:', newPath)
                    fullpaths.append(heads.pop(-1))
                    vaultFound = True

longestPath = 0
for path in fullpaths:
    pathLength = len(path[1])
    if pathLength > longestPath:
        longestPath = pathLength

print('The answer to Part 2:', longestPath)
