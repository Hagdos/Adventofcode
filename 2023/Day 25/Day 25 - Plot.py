import collections
import matplotlib.pyplot as plt
import random
import time


def checkConnections(part):
    seen = set([part])
    todo = [part]

    while todo:
        part = todo.pop()
        for newpart in connections[part]:
            if newpart not in seen:
                seen.add(newpart)
                todo.append(newpart)
    return len(seen)


def scatterplot(locations):

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(*zip(*locations.values()))
    plt.show()

def moveCloser(locations):
    for part in locations:
        x = y =0
        for p2 in connections[part]:
            dx, dy = locations[p2]
            x += dx
            y += dy

        locations[part] = (x/len(connections[part]), y/len(connections[part]))
    return locations

def scaleLocations(locations):
    x = [t[0] for t in locations.values()]
    y = [t[1] for t in locations.values()]
    scalex = 2/(max(x) - min(x))
    scaley = 2/(max(y) - min(y))

    for p in locations:
        locations[p] = (locations[p][0]*scalex, locations[p][1]*scaley)

    return locations


file = open('input.txt').readlines()

data = [x.strip().split() for x in file]

connections = collections.defaultdict(list)

for line in data:
    part1 = line[0][:-1]
    connections[part1] += line[1:]
    for part in line[1:]:
        connections[part].append(part1)

locations = dict()
for part in connections:
    x = random.random()*2-1
    y = random.random()*2-1

    locations[part] = (x,y)

for _ in range(20):
    scatterplot(locations)
    moveCloser(locations)
    scaleLocations(locations)
    time.sleep(0.5)


scatterplot(locations)


# three = [('fxn', 'ptq'), ('fbd', 'lzd'), ('kcn', 'szl')]

# for c in three:
#     connections[c[0]].remove(c[1])
#     connections[c[1]].remove(c[0])


print('The answer to part 1: ', checkConnections('szh')*checkConnections('nhl'))
