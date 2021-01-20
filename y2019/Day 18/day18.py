f = open('cave.txt')

cave = []
for line in f:
    cave.append(line.strip())
    
lower = {}
upper = {}
neighbours = {}
for y,line in enumerate(cave):
    for x,c in enumerate(line):
        if c.islower():
            lower[c] = (x,y)
        elif c.isupper():
            upper[c] = (x,y)
        n = set()
        if c != '#':
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if cave[y+dy][x+dx] != '#':
                    n.add((x+dx, y+dy))
            neighbours[(x,y)] = n

