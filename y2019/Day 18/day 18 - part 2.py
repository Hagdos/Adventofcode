# =============================================================================
# Function that finds the distance from a starting point to all other points in the cave, returning dicts with distances to all locations and the doors they are blocked by
# =============================================================================
def distanceto(point, d, alreadyfound, blockedby, inpath, relevantkeys):
    if point in doors.keys():
        inpath.add(doors[point])
    if point in keys.values():
        for k in keys:
            if keys[k] == point:
                relevantkeys.add(k)
    blockedby[point] = inpath
    alreadyfound[point] = d
    d += 1
    for n in neighbours[point]:
        if n in alreadyfound.keys():
            if alreadyfound[n] > d:
                alreadyfound, blockedby, relevantkeys = distanceto(n, d, alreadyfound, blockedby, inpath.copy(), relevantkeys)
        else:
            alreadyfound, blockedby, relevantkeys = distanceto(n,d,alreadyfound, blockedby, inpath.copy(), relevantkeys)
    return alreadyfound, blockedby, relevantkeys

def findshortestpath(paths, relevantkeys, distancetostart):
    maxpathlength = len(relevantkeys)+1
    stop = False
    for i in range(40000):
        # Find the best path to continue on
        bestpath = 10**20    #Random "big" number
        for p in paths:
            #Best path is shortest path per key
            if len(p) == 1:
                ps = p
            elif paths[p]//(len(p)-1) < bestpath and len(p) < maxpathlength:
                bestpath = paths[p]//(len(p)-1)
                ps = p
        if bestpath == 2**16:
            print("No best path found")
            return paths
        
        #Add new paths
        for k in relevantkeys:
            if k not in ps:     
                addpath = True
                newpath = ps + tuple(k)
                if ps[-1] == '@':
                    newlength = paths[ps] + distancetostart[keys[k]]
                else:
                    newlength = paths[ps] + distancetokey[ps[-1]][keys[k]]
                for p in list(paths):
                    if newlength>paths[p] and all(keys in p for keys in newpath):
                        addpath = False
                        break
                    if paths[p]>newlength and all(keys in newpath for keys in p):
                        paths.pop(p)

                if addpath:
                    paths[newpath] = newlength
                    # if len(newpath) == maxpathlength:
                        # print("We reached all numbers!")
        paths.pop(ps)                
        if len(paths) == 1 and i>0:
            for p in paths:
                if len(p) == maxpathlength:
                    stop = True
        if stop:
            return paths



# =============================================================================
# Open file
# =============================================================================

f = open('cavept2.txt')
# f = open('cavetest5.txt')
cave = []
for line in f:
    cave.append(line.strip())

# =============================================================================
# Find location of all keys; doors; and map the neighbours of each node for the iteration
# =============================================================================
keys = {}
doors = {}
neighbours = {}
start = []
for y,line in enumerate(cave):
    for x,c in enumerate(line):
        if c.islower():
            keys[c] = (x,y)
        elif c.isupper():
            doors[(x,y)] = c
        elif c == '@':
            start.append((x,y))
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
distancetostart = [0]*4
blockedbystart = [0]*4
relevantkeys = [0]*4
for k in keys:
    distancetokey[k], blockedbykey[k], _ = distanceto(keys[k], 0, {}, {}, set(), set())
for i,s in enumerate(start):
    distancetostart[i], blockedbystart[i], relevantkeys[i] = distanceto(s, 0, {}, {}, set(), set())


paths = []
paths.append(dict())
paths[0][tuple('@')] = 0
paths.append(dict())
paths[1][tuple('@')] = 0
paths.append(dict())
paths[2][tuple('@')] = 0
# paths[2][('@', 'n')] = distancetostart[2][keys['n']]
paths.append(dict())
paths[3][tuple('@')] = 0
    

for i in range(len(start)):
    paths[i] = findshortestpath(paths[i], relevantkeys[i], distancetostart[i])

ans = 0
for i in paths:
    for p in i:
        # print(i[p])
        ans+= i[p]
    
print("Answer to part 2:", ans)

#1796 is too high
#part 3 seems to be right. Still to check 0, 1 and 2
    
for i,_ in enumerate(start):
    for k in relevantkeys[i]:
        print(k, blockedbystart[i][keys[k]])
    print()
        
#     print()
# for line in cave:
#     if 'v' in line:
#         line = line + " <- This line"
#     print(line)

    
# Shortest path on part 1: n e u i j w c z k s t o q b a y g f x h m d l v p r 
# n, e, u, i, j, w, c, z, k, s, t, o, q, b, a, y, g, f, x, h, m, d, l, v, p, r, 

#Start 3 has to start with n. This opens anything for start 2; which opens anything for start 1

#Between 3 and 4 is more difficult...:
    #Starting with n; and finding all in 1 and 2 opens the road to s and m. 
    #s is needed to reach x,y,f,a,g,h. Those are all needed to reach l
    #l is needed to reach p and v. p and v are needed to reach r
    
    
    # Possible paths for part 3: [n, s, etc, r], [n, m, s, etc, r]
    # Possible paths for part 4: [etc, p, v], [etc, v, p] (The second one is the only one that makes sense; so we could do a least path ending at v, and add the distance to p or do the least path to p)
    
#Technically; my search algorithm is pruning too quickly. Should only prune other paths that are longer or equal and have the same endpoint.