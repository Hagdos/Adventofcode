from queue import PriorityQueue
import time as t

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



def findPaths(start, neighbours):
    # create empty queues
    distance = dict()
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

# TODO Can be made faster by keeping only the non-zero valves in valveflows
def score(state, totaltime, valveflows):
    path, time, pressure = state
    maxflow = sum([valveflows[v] for v in valveflows if v not in path])
    score = pressure + maxflow * (totaltime-time-2)
    # -2, because it needs at least 1 min to get to the next valve; and 1 minute to open it
    return -score  # Negative; because priorityqueue puts the lowest value on top


def getnextstates(state, neighbours, valveflows, totaltime):
    path, time, pressure = state
    nextstates = []

    for n in neighbours[path[-1]]:
        if n not in path:
            nextstates.append(newstate(state, n, neighbours, valveflows, totaltime))

    return nextstates


def newstate(state, n, neighbours, valveflows, totaltime):
    path, time, pressure = state
    newpath = path + [n]
    time += neighbours[path[-1]][n]+1
    time = min(time, totaltime)
    pressure += valveflows[n] * (totaltime-time)

    return [newpath, time, pressure]



def solvePart1():
    neighbours, valveflows = readInput('input.txt')
    neighbours, valveflows = removeHalls(neighbours, valveflows)
    totaltime = 30

    # Map shortest path from each node to each node. (N nodes)
    for n in neighbours:
        neighbours[n] = findPaths(n, neighbours)

    q = PriorityQueue()

    path = ['AA']
    time = 0
    pressure = 0

    state = [path, time, pressure]

    q.put((score(state, totaltime, valveflows), state))
    while not q.empty():
        s, state = q.get()

        if state[1] >= totaltime:
            return state[2], state
            break

        nstates = getnextstates(state, neighbours, valveflows, totaltime)

        for n in nstates:
            q.put((score(n, totaltime, valveflows), n))

start = t.time()
print(f'The answer to part 1: {solvePart1()}')
print(f'Time spent: {t.time() - start}')


def score2(state1, state2, maxflow, totaltime):
    _, time1, pressure1, _ = state1
    _, time2, pressure2, _ = state2

    time = min(time1, time2)

    score = pressure1 + pressure2 + maxflow * (totaltime-time-1)
    return -score


def getnextstates2(state1, state2, neighbours, valveflows, totaltime):
    # state 1 has a lower time; so check neighbours of state 1
    path = state1[0]
    nextstates = []

    for n in neighbours[path[-1]]:
        if n not in path and n not in state2[0]:
            nextstate = newstate2(state1, n, neighbours, valveflows, totaltime)
            nextstates.append((nextstate, state2))
    return nextstates


def newstate2(state, n, neighbours, valveflows, totaltime):
    path, time, pressure, flow = state
    newpath = path + [n]
    deltatime = neighbours[path[-1]][n]+1

    if time + deltatime > totaltime:
        deltatime = totaltime - time

    time += deltatime
    pressure += flow * deltatime
    flow += valveflows[n]

    return [newpath, time, pressure, flow]




# # def solvePart2():
neighbours, valveflows = readInput('input.txt')
neighbours, valveflows = removeHalls(neighbours, valveflows)
maxflow = sum(valveflows.values())
totaltime = 26

# Map shortest path from each node to each node. (N nodes)
for n in neighbours:
    neighbours[n] = findPaths(n, neighbours)


q = PriorityQueue()

path = ['AA']
time = 0
pressure = 0
flow = 0

visited = []

state1 = [path, time, pressure, flow]
state2 = state1.copy()


q.put((score2(state1, state2, maxflow, totaltime), state1, state2))
while not q.empty():
    s, state1, state2 = q.get()

    if state1[1] >= totaltime and state2[1] >= totaltime:
        # return state1[2] + state2[2]
        print(state1[2] + state2[2])
        break

    if state1[1] > state2[1]:
        nstates = getnextstates2(state2, state1, neighbours, valveflows, totaltime)
    else:
        nstates = getnextstates2(state1, state2, neighbours, valveflows, totaltime)

    for n1, n2 in nstates:
        # if (n1, n2) not in visited:
        q.put((score2(n1, n2, maxflow, totaltime), n1, n2))
            # visited.append((n1, n2))


# print(f'The answer to part 2: {solvePart2()}')

# 2705

#Alternative solution: The solution from part 1; but at t = endtime -> t = 0, path.append('AA'), continue until t=26 again
# Maybe can be fixed by using endtime * 2 in some spots?
# But then how to handle the score properly?

# Alternative solution: Find all paths that finish within 26 seconds. Find the best 2 paths that do not overlap.

# Current solution does finish. In about 10.000 years...