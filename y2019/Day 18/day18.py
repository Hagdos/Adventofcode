import time
import itertools

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


# f = open('cavetest2.txt')
f = open('cave.txt')
cave = []
for line in f:
    cave.append(line.strip())
    
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

distancetokey = {}
blockedbykey = {}
for k in keys:
    distancetokey[k], blockedbykey[k] = distanceto(keys[k], 0, {}, {}, set())
distancetostart, blockedbystart = distanceto(start, 0, {}, {}, set())

# =============================================================================
# Debugging and trial-shit
# =============================================================================

firstavailable = set()
for k in keys:
    if not blockedbystart[keys[k]]:
        firstavailable.add(k)
# for l in lower:
#     print(l, blockedbystart[lower[l]])
    # for b in blockedbystart[lower[l]]:
    #     if b.lower() in firstavailable:
    #         print(l, blockedbystart[lower[l]])
    
print(firstavailable)


# =============================================================================
# Possible routes
# =============================================================================

s = time.time()

routes = itertools.permutations(firstavailable, len(firstavailable))

lengths = []
for r in routes:
    length = 0
    for i, k in enumerate(r):
        if i == 1:
            length += distancetostart[keys[k]]
        else:
            length += distancetokey[k][keys[r[i-1]]]
    lengths.append(length)
    
print(time.time()-s)
    


# print(routes)
        




# set.discard()





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

