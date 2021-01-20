import time

def distanceto(point, d, alreadyfound, blockedby, inpath):
    if point in upper.keys():
        inpath.add(upper[point])
    blockedby[point] = inpath
    alreadyfound[point] = d
    d += 1
    for n in neighbours[point]:
        if n in alreadyfound.keys():
            if alreadyfound[n] > d:
                alreadyfound, blockedby = distanceto(n, d, alreadyfound, blockedby, inpath.copy())
        else:
            alreadyfound, blockedby = distanceto(n,d,alreadyfound, blockedby, inpath.copy())
    return alreadyfound, blockedby


# f = open('cavetest2.txt')
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
            upper[(x,y)] = c
        elif c == '@':
            start = (x,y)
        n = set()
        if c != '#':
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if cave[y+dy][x+dx] != '#':
                    n.add((x+dx, y+dy))
            neighbours[(x,y)] = n

distancetolower = {}
blockedbylower = {}
for l in lower:
    distancetolower[l], blockedbylower[l] = distanceto(lower[l], 0, {}, {}, set())
distancetostart, blockedbystart = distanceto(start, 0, {}, {}, set())

# =============================================================================
# Debugging and trial-shit
# =============================================================================

# for line in cave:
#     print(line)

firstavailable = set()
for l in lower:
    # print(l, distancetostart[lower[l]])
    if not blockedbystart[lower[l]]:
        firstavailable.add(l)
for l in lower:
    for b in blockedbystart[lower[l]]:
        if b.lower() in firstavailable:
            print(l, blockedbystart[lower[l]])
    
print(firstavailable)

# =============================================================================
# Print map kinda thingy
# =============================================================================
# newcave = []
# for y,line in enumerate(cave):
#     newcave.append(list(line))
#     for x,_ in enumerate(line):
#         if (x,y) in distancetostart.keys():
#             newcave[y][x] = str(distancetostart[(x,y)])[-1]
#     newcave[y] = ''.join(newcave[y])
            
# print(cave)
# print(newcave)

