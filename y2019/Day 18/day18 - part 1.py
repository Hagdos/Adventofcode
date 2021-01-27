import time

# =============================================================================
# Function that finds the distance from a starting point to all other points in the cave, returning dicts with distances to all locations and the doors they are blocked by
# =============================================================================
def distanceto(point, d, alreadyfound, blockedby, inpath):
    if point in doors.keys():
        inpath.add(doors[point])
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


f = open('cavetest1.txt')
f = open('cave.txt')
cave = []
for line in f:
    cave.append(line.strip())
    
# =============================================================================
# Find location of all keys; doors; and map the neighbours of each node for the iteration
# =============================================================================
keys = {}
doors = {}
neighbours = {}
for y,line in enumerate(cave):
    for x,c in enumerate(line):
        if c.islower():
            keys[c] = (x,y)
        elif c.isupper():
            doors[(x,y)] = c
        elif c == '@':
            start = (x,y)
        n = set()
        if c != '#':
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if cave[y+dy][x+dx] != '#':
                    n.add((x+dx, y+dy))
            neighbours[(x,y)] = n

# =============================================================================
# Run distanceto-functions
# =============================================================================

distancetokey = {}
blockedbykey = {}
for k in keys:
    distancetokey[k], blockedbykey[k] = distanceto(keys[k], 0, {}, {}, set())
distancetostart, blockedbystart = distanceto(start, 0, {}, {}, set())

# =============================================================================
# Possible routes
# =============================================================================
paths = dict()
paths[tuple('@')] = 0
# for k in keys:
#     if not blockedbystart[keys[k]]:
#         paths[tuple(k)] = distancetostart[keys[k]]

# Find shortest current path.
s = time.time()
maxpathlength = len(keys)+1
stop = False

for i in range(500000):
    if not i%1000:
        print(i, len(paths))
    # print(paths)
    if len(paths) == 1 and i>0:
        for p in paths:
            if len(p) == maxpathlength:
                stop = True
    if stop:
        break

    bestpath = 10**20    #Random "big" number
    for p in paths:
        #Best path is shortest path per key. -1 is needed because otherwise it will favour short paths starting with @
        if len(p) == 1:
            ps = p
        elif paths[p]//(len(p)-1) < bestpath and len(p) < maxpathlength:
            bestpath = paths[p]//(len(p)-1)
            ps = p
    
    #Add new paths
    for k in keys:
        if k not in ps:     
            if not any(door.lower() not in ps for door in blockedbystart[keys[k]]):
                addpath = True
                newpath = ps + tuple(k)
                if ps[-1] == '@':
                    newlength = paths[ps] + distancetostart[keys[k]]
                else:
                    newlength = paths[ps] + distancetokey[ps[-1]][keys[k]]
                    
                for p in list(paths):
                    if p[-1] == k:
                        if newlength >=paths[p] and all(keys in p for keys in newpath):
                            addpath = False
                            break
                        elif paths[p]>=newlength and all(keys in newpath for keys in p):
                            paths.pop(p)
                            break
                # for p in list(paths):
                #     if newlength>=paths[p] and all(keys in p for keys in newpath):
                #         addpath = False
                #         break
                #     if paths[p]>=newlength and all(keys in newpath for keys in p):
                #         paths.pop(p)

                if addpath:
                    paths[newpath] = newlength
                    # if len(newpath) == maxpathlength:
                    #     print("We reached all numbers!")
                
    paths.pop(ps)
    
print(time.time()-s)
print("Answer to part 1:", paths[p])

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

