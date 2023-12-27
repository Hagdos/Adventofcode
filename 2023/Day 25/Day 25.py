import collections
import networkx as nx
import matplotlib.pyplot as plt


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

file = open('input.txt').readlines()

data = [x.strip().split() for x in file]
ans1 = ans2 = 0

connections = collections.defaultdict(list)
parts = set()

G = nx.Graph()
G.add_nodes_from(parts)

for line in data:
    part1 = line[0][:-1]
    connections[part1] += line[1:]
    for part in line[1:]:
        connections[part].append(part1)
        parts.add(part)
        G.add_edge(part1, part)
    parts.add(part1)


three = [('fxn', 'ptq'), ('fbd', 'lzd'), ('kcn', 'szl')]

G.remove_edges_from(three)

for c in three:
    connections[c[0]].remove(c[1])
    connections[c[1]].remove(c[0])

subax1 = plt.subplots(1, 1, figsize=(10, 10))
nx.draw(G, with_labels=True)
# nx.draw(G)

print('The answer to part 1: ', checkConnections('szh')*checkConnections('nhl'))
