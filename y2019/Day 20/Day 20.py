f = open('donut.txt')

cave = []
for line in f:
    cave.append(line.strip('\n'))
    
# # =============================================================================
# # Find location of all keys; doors; and map the neighbours of each node for the iteration
# # =============================================================================
# portals = {}
# neighbours = {}
# for y,line in enumerate(cave):
#     for x,c in enumerate(line):
#         if c == '.':
#             n = set()
#             for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 if cave[y+dy][x+dx] == '.':
#                     n.add((x+dx, y+dy))                 
#                 elif cave[y+dy][x+dx] == 'A' and cave[y+2*dy][x+2*dx] == 'A':
#                     start = (x, y)
#                 elif cave[y+dy][x+dx] == 'Z' and cave[y+2*dy][x+2*dx] == 'Z':
#                     end = (x, y)
#                 elif cave[y+dy][x+dx].isupper():
#                     # This if/elif checks if the portal is on the left/top, or on the right/bottom. If it's on the left/top; the order of letters has to be reversed.
#                     if dy+dx == -1:
#                         portal = (cave[y+2*dy][x+2*dx], cave[y+dy][x+dx])
#                     elif dy+dx == 1:
#                         portal = (cave[y+dy][x+dx], cave[y+2*dy][x+2*dx])
                    
#                     #If the portal has been found before; add that point as a neighbour; and add this point as a neighbour to the portal                    
#                     if portal in portals.keys():
#                         n.add(portals[portal])
#                         neighbours[portals[portal]].add((x,y))
#                         del portals[portal]
#                     #If it has not been found before; add it to the list of portals.
#                     else:
#                         portals[portal] = (x, y)
#             neighbours[(x,y)] = n

# # =============================================================================
# #  Find distance of all points to any starting point. Recursive function; returns a dictionary of all found points with their distance
# # =============================================================================

# def distanceto(point, distance = 0, alreadyfound = {}):
#     alreadyfound[point] = distance
#     distance += 1
#     try:
#         for n in neighbours[point]:
#             if n in alreadyfound.keys():
#                 if alreadyfound[n] > distance:
#                     alreadyfound = distanceto(n, distance, alreadyfound)
#             else:
#                 alreadyfound = distanceto(n,distance,alreadyfound)
#     except:
#         print(point)
#     return alreadyfound

# # distances = distanceto(start)
# # print("Answer to part 1:", distances[end])

# =============================================================================
#   ------------------   Part 2   ---------------------------
# =============================================================================

INNER = -1
OUTER = 1

#Define a class portals; with a name; a location and an orientation (inner or outer)
class Portal:
    def __init__(self, name, location, orientation):
        self.name = name
        self.location = location
        self.orientation = orientation
        self.mirror = None
        
    def __repr__(self):
        if self.orientation == INNER:
            return str(self.name) + ' INNER'
        else:
            return str(self.name) + ' OUTER'


# =============================================================================
# Find location of all keys; doors; and map the neighbours of each node for the iteration
# =============================================================================
portals = []
portalsLocations = {}
neighbours = {}

for y,line in enumerate(cave):
    for x,c in enumerate(line):
        if c == '.':
            n = set()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if cave[y+dy][x+dx] == '.':
                    n.add((x+dx, y+dy))                 
                # elif cave[y+dy][x+dx] == 'A' and cave[y+2*dy][x+2*dx] == 'A':
                #     start = (x, y)
                # elif cave[y+dy][x+dx] == 'Z' and cave[y+2*dy][x+2*dx] == 'Z':
                #     end = (x, y)
                elif cave[y+dy][x+dx].isupper():
                    # This if/elif checks if the portal is on the left/top, or on the right/bottom. If it's on the left/top; the order of letters has to be reversed.
                    # if dy+dx == -1:
                    #     portalname = (cave[y+2*dy][x+2*dx], cave[y+dy][x+dx])
                    # elif dy+dx == 1:
                    #     portalname = (cave[y+dy][x+dx], cave[y+2*dy][x+2*dx])
                    if dy+dx == -1:
                        portalname = cave[y+2*dy][x+2*dx] + cave[y+dy][x+dx]
                    elif dy+dx == 1:
                        portalname = cave[y+dy][x+dx] + cave[y+2*dy][x+2*dx]
                    
                    if x == 2 or x == 114 or y == 2 or y == 122:
                        portals.append(Portal(portalname, (x,y), OUTER))
                    elif x == 32 or x == 84 or y == 32 or y == 92:
                        portals.append(Portal(portalname, (x,y), INNER))
                    
                    portalsLocations[(x,y)] = portals[-1]
                    
                    for p in portals[:-1]:
                        if p.name == portalname:
                            p.mirror = portals[-1]
                            portals[-1].mirror = p
                    
                    if portalname == 'AA':
                        start = portals[-1]
                    elif portalname == 'ZZ':
                        finish = portals[-1]
                
            neighbours[(x,y)] = n

# =============================================================================
# Find distances between all portals in one donut
# =============================================================================

def distanceto2(point, distance = 0, alreadyfound = {}, portalsFound = {}):
    alreadyfound[point] = distance
    distance += 1
    
    for neighbour in neighbours[point]:
        if neighbour not in alreadyfound.keys() or alreadyfound[neighbour] > distance:
            if neighbour in portalsLocations.keys():
                portalsFound[portalsLocations[neighbour]] = [distance, 0]     
            alreadyfound, portalsFound = distanceto2(neighbour, distance, alreadyfound, portalsFound)
    return alreadyfound, portalsFound


portalsDistance = {}
for p in portals:
    _, portalsDistance[p] = distanceto2(p.location, 0, {}, {}) 

# =============================================================================
# Combine single-length paths:
# =============================================================================

for portal in portals:
    while(len(portalsDistance[portal]) == 1):
        caveExit = list(portalsDistance[portal].keys())[0]
        if caveExit == start or caveExit == finish:
            break
        caveEntrance = caveExit.mirror
      
        currentDistance = portalsDistance[portal][caveExit][0]
        currentLevel = portalsDistance[portal][caveExit][1]
        
        nextSteps = portalsDistance[caveEntrance]
        for nextStep in nextSteps:
            if nextStep != start:
                if not (nextStep == finish and caveEntrance.orientation == INNER):   #TODO: Check if this is correct...
                    nextDistance = currentDistance + nextSteps[nextStep][0] + 1
                    nextLevel = currentLevel + nextSteps[nextStep][1] + nextStep.orientation
                    
                    portalsDistance[portal][nextStep] = [nextDistance, nextLevel]
        
        portalsDistance[portal].pop(caveExit)

# =============================================================================
# Check which portals are still valid, and remove the rest
# =============================================================================
exits = set([finish])
entrances = set([start])
for p in portals:
    for key in portalsDistance[p]:
        exits.add(key)
        if key.mirror:
            entrances.add(key.mirror)

for p in portals:
    if p not in entrances:
        portalsDistance.pop(p)

for p in entrances:
    print(p, portalsDistance[p])

# =============================================================================
# Find the shortest path from start to finish
# =============================================================================

#TODO Fix this for steps over multiple depths.
# paths = {}
# paths[(start,)] = [0, 0]
# finished = False
# for _ in range(10000):
#     #Determine best path
#     shortestPathLength = 2**16
#     for p in paths:
#         if paths[p][0] < shortestPathLength:
#             bestPath = p
#             shortestPathLength = paths[p][0]                #Is the shortest path really the best? Or the highest level?
#     if shortestPathLength == 2**16:
#         raise Exception("No best path found") 
    
#     #The next entrance is the mirror of the last step 
#     caveexit = bestPath[-1]
#     if caveexit.mirror:
#         entrance = caveexit.mirror
#     else:
#         print("No mirror found")
#         entrance = caveexit

    
#     nextSteps = portalsDistance[entrance]
#     currentLevel = paths[bestPath][1]
    
#     for nextStep in nextSteps:                                                  #Add all possible next paths
#         # if nextStep not in bestPath:                                            #If the next path is not already in the path (visiting a portal twice does not make sense)
#         if not (nextStep.orientation == OUTER and currentLevel == 0):       #Don't go up from the highest level
#             if nextStep == finish and currentLevel == 0:
#                 newLength = paths[bestPath][0] + portalsDistance[entrance][nextStep][0]
#                 print("Total length : ", newLength)
#                 finished = True
#             elif nextStep != finish and nextStep != start :                                      #Ignore the finish if not at the top level
#                 newPath = bestPath + (nextStep,)
#                 newLength = paths[bestPath][0] + portalsDistance[entrance][nextStep][0] + 1
#                 newLevel = currentLevel + nextStep.orientation
#                 paths[newPath] = [newLength, newLevel]
                 
#     if finished:
#         break        
    
#     paths.pop(bestPath)
    
    
# print("All paths")
# for q in paths:
#     print(q, paths[q])
# print("Next steps:")
# print(nextSteps)
# print()
        
           



    #544 is too low
    #554 is too low