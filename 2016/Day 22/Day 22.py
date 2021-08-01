class Node:
    def __init__(self, position, size, used, available):
        self.position = position
        self.size = size
        self.used = used
        self.available = available
        neighbours = []
        for dx in [-1, 1]:
            if 0 <= position[0] + dx <= 37:
                neighbours.append((position[0] + dx, position[1]))
        for dy in [-1, 1]:
            if 0 <= position[1] + dy <= 25:
                neighbours.append((position[0], position[1] + dy))
        self.neighbours = set(neighbours)
            
        
    def __repr__(self):
        return "Node " + str(self.position)

import time

start = time.time()
file = open('input.txt').readlines()

nodes = {}
minsize = 500
maxsize = 0

for line in file[2:]:
    data = line.strip().split()
    name = data[0].split('-')
    position = (int(name[1][1:]), int(name[2][1:]))
    size = int(data[1][:-1])

    used = int(data[2][:-1])
    if 0 < size < minsize:
        minsize = size
    if 400 > size > maxsize:
        maxsize = size
    available = int(data[3][:-1])
    
    nodes[position] = (Node(position, size, used, available))    
    
# print(nodes)

pairs = []

for nodeA in nodes.values():
    if nodeA.used > 0:
        for nodeB in nodes.values():
            if nodeA is not nodeB:
                if nodeA.used <= nodeB.available:
                    pairs.append((nodeA, nodeB))


print("The answer to part 1:", len(pairs))

# Data block size is between 64 and 73, or >400
# Storage size is between 85 and 94, or >400
# All blocks with >400 size have less than 20 available.

# Summary: All node > 400 can be ignored. These form a line from x=6 to x=37, y=12.
# Aside from those; each node can handle any nodes' data, but never more than 2 nodes' data.
# The only empty node is (16, 23)

# Shortest path:
# 11 moves to get the empty block at (5, 23), to circumvent the line
# 23 moves to get the empty block at (5, 0)
# 32 moves to get the empty block at (37, 0), first step of the relevant data.
# It takes 5 steps to move the data one block further left; and it needs to move another 36 steps.
# So 36*5 = 180
# 180 + 32 + 23 + 11 = 246