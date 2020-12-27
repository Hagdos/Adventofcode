f = open('wires.txt')

wires = []
for wire in f:
    wires.append(wire.strip().split(','))
    
    
def wirepath(wire):
    path = set()
    distance = {}
    x = 0
    y = 0
    dist = 0
    for instr in wire:

        direction = instr[0]
        length = int(instr[1:])
        
        if direction == 'U':
            dx, dy = (0, -1)
        if direction == 'D':
            dx, dy = (0, 1)
        if direction == 'L':
            dx, dy = (-1, 0)
        if direction == 'R':
            dx, dy = (1, 0)
        
        for i in range(length):
            x += dx
            y += dy
            dist += 1
            path.add((x,y))
            distance[(x,y)] = dist
    
    return path, distance

paths = []
distances = []
for wire in wires:
    p, d = wirepath(wire)
    paths.append(p)
    distances.append(d)

crossings = set()
for loc1 in paths[0]:
    if loc1 in paths[1]:
        crossings.add(loc1)

mdistmin = 1000000000
for c in crossings:
    mdist = abs(c[0])+abs(c[1])
    if mdist <mdistmin:
        mdistmin = mdist

print("Answer Part 1:", mdistmin)

mdistmin = 1000000000
for c in crossings:
    mdist = distances[0][c] + distances[1][c]
    if mdist <mdistmin:
        mdistmin = mdist
        
print("Answer Part 2:", mdistmin)