from collections import defaultdict, Counter
import random


def mergeNodes(connections, nodeA, nodeB):

    nodesizes[nodeA] += nodesizes[nodeB]

    for n in connections[nodeB]:
        if n != nodeA:
            connections[n][nodeA] += connections[n][nodeB]
            connections[n][nodeB] = 0
            connections[nodeA][n] = connections[n][nodeA]

    del connections[nodeA][nodeB]
    for n in connections[nodeA]:
        del connections[n][nodeB]

    connections.pop(nodeB)

    return None

def findCut(connections):
    todo = []

    while len(connections) > 2:

        if todo:
            partA, partB = todo.pop()
        else:
            partA = random.choice(list(connections.keys()))
            partB = random.choice(list(connections[partA].keys()))

        if partA not in connections or partB not in connections:
            continue

        mergeNodes(connections, partA, partB)

        for pB in connections[partA]:
            if connections[partA][pB] >= 4:
                todo.append((partA, pB))

    nodeA, connectionsA = connections.popitem()
    nodeB, connectionsB = connections.popitem()

    assert connectionsA[nodeB] == connectionsB[nodeA]

    if connectionsA[nodeB] == 3:
        print('The answer to part 1: ', nodesizes[nodeA]*nodesizes[nodeB])
        return nodesizes[nodeA]*nodesizes[nodeB]

    return None



file = open('input.txt').readlines()
data = [x.strip().split(': ') for x in file]

while True:
    connections = defaultdict(Counter)
    nodesizes = dict()

    for line in data:
        part1 = line[0]
        for part in line[1].split(' '):
            connections[part1][part] = 1
            connections[part][part1] = 1
            nodesizes[part] = 1
        nodesizes[part1] = 1

    if findCut(connections):
        break
