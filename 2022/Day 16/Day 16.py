def readInput(filename):

    file = open(filename).readlines()
    data = [x.strip().split() for x in file]

    neighbours = dict()
    valveflows = dict()

    for line in data:
        name = line[1]
        flow = int(line[4].split('=')[1][:-1])
        tunnels = [t.strip(',') for t in line[9:]]

        neighbours[name] = {t:1 for t in tunnels}
        valveflows[name] = flow

    return neighbours, valveflows


def removeHalls(neighbours, valveflows):
    for location in list(neighbours):
        if valveflows[location] == 0 and location != 'AA':
            for n in neighbours[location]:
                for m in neighbours[location]:
                    if m != n:
                        neighbours[n][m] = neighbours[location][n] + neighbours[location][m]
                        neighbours[n].pop(location)
            neighbours.pop(location)
            valveflows.pop(location)

    return neighbours, valveflows


def findPaths(start):
    # create empty queues
    distance = dict()
    prev = dict()
    Queue = []
    for n in neighbours:
        distance[n] = 10000
        Queue.append(n)

    distance[start] = 0

    while(Queue):
        Queue.sort(key=lambda a: distance[a])
        node = Queue.pop(0)

        for n in neighbours[node]:
            if n in Queue:
                if distance[node]+neighbours[node][n] < distance[n]:
                    distance[n] = distance[node]+neighbours[node][n]

    distance.pop(start)
    if start != 'AA':
        distance.pop('AA')
    return distance


def nextSteps(path):
    p, time, pressure = path
    node = p[-1]
    options = []
    for n in neighbours[node]:
        if n not in p:
            new = createNewPath(path, n)
            if new:
                options.append(new)
    return options

def createNewPath(path, n):
    p, time, pressure = path
    time += neighbours[p[-1]][n]+1 # +1 to open valve
    p = p + [n]

    if time > totaltime:
        solutions.append([p, time, pressure])
        return None

    pressure+= valveflows[n]*(totaltime-time)
    return [p, time, pressure]


def checkPath(p1):
    for p2 in [*visited, *paths]:
        if p1[0][-1] == p2[0][-1]: # Same room
            if set(p1[0]) == set(p2[0]): # Same rooms already visited
                if p1[1] >= p2[1]: # With the same time or longer
                    if p1[2] <= p2[2]: # And also less pressure relieved
                        return False

    return True

neighbours, valveflows = readInput('input.txt')
neighbours, valveflows = removeHalls(neighbours, valveflows)
totaltime = 26

# Map shortest path from each node to each node. (N nodes)
for n in neighbours:
    neighbours[n] = findPaths(n)


# path, time, pressure
startpath = [['AA'], 0, 0]
paths = [startpath]
visited = []
solutions = []
c = 0

while(paths):
    c += 1

    path = paths.pop(0)
    visited.append(path)

    options = nextSteps(path)
    for o in options:
        # if checkPath(o): # Checkpath seems to make it run much much longer...
        paths.append(o)

ans1 = 0
for v in visited:
    if v[1] == ['AA', 'MC']:
        print(v)
    if v[2] > ans1:
        ans1 = max(ans1, v[2])
        winpath = v
print(f'The answer to part 1: {ans1}')
print(winpath)


# Part 2: Seems like it can be split: The winning path for 30/26 seems to be straight from AA to JY with all nodes in between.
# So the elephant should take the best path that doesn't involve these nodes.

# Run the same thing again; without the nodes in winpath.

for n in neighbours:
    for r in winpath[0]:
        if r in neighbours[n]:
            neighbours[n].pop(r)


startpath = [['AA'], 0, 0]
paths = [startpath]
visited = []
solutions = []
c = 0

while(paths):
    c += 1

    path = paths.pop(0) # Unsorted?
    visited.append(path)

    options = nextSteps(path)
    for o in options:
        # if checkPath(o): # Checkpath seems to make it run much much longer...
        paths.append(o)



ans2 = 0
for v in visited:
    if v[1] == ['AA', 'MC']:
        print(v)
    if v[2] > ans2:
        ans2 = max(ans2, v[2])
        winpath = v
print(f'The answer to part 2: {ans1+ans2}')
print(winpath)
