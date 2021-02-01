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


# =============================================================================
# Find location of all keys; doors; and map the neighbours of each node for the iteration
# =============================================================================
innerPortals = {}
outerPortals = {}
innerPortalsLocations = {}
outerPortalsLocations = {}
neighbours = {}
for y,line in enumerate(cave):
    for x,c in enumerate(line):
        if c == '.':
            n = set()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if cave[y+dy][x+dx] == '.':
                    n.add((x+dx, y+dy))                 
                elif cave[y+dy][x+dx] == 'A' and cave[y+2*dy][x+2*dx] == 'A':
                    start = (x, y)
                elif cave[y+dy][x+dx] == 'Z' and cave[y+2*dy][x+2*dx] == 'Z':
                    end = (x, y)
                elif cave[y+dy][x+dx].isupper():
                    # This if/elif checks if the portal is on the left/top, or on the right/bottom. If it's on the left/top; the order of letters has to be reversed.
                    if dy+dx == -1:
                        portal = (cave[y+2*dy][x+2*dx], cave[y+dy][x+dx])
                    elif dy+dx == 1:
                        portal = (cave[y+dy][x+dx], cave[y+2*dy][x+2*dx])
                    
                    if x == 2 or x == 114 or y == 2 or y == 122:
                        outerPortals[portal] = (x,y)
                        outerPortalsLocations[(x,y)] = portal
                    elif x == 32 or x == 84 or y == 32 or y == 92:
                        innerPortals[portal] = (x,y)
                        innerPortalsLocations[(x,y)] = portal
                    else:
                        print("Something went wrong 1")
            neighbours[(x,y)] = n


def distanceto2(point, distance = 0, depth = 0, alreadyfound = {}, foundPortals = []):
    alreadyfound[(point, depth)] = distance
    distance += 1
    # print(distance)
    for neighbour in neighbours[point]:
        if neighbour in innerPortalsLocations.keys() and depth < 4:
            n = outerPortals[innerPortalsLocations[neighbour]]
            depth += 1
            # alreadyfound, foundPortals = distanceto2(outerPortals[innerPortalsLocations[n]], distance, depth+1, alreadyfound, foundPortals)
        elif neighbour in outerPortalsLocations.keys() and depth > 0:
            n = innerPortals[outerPortalsLocations[neighbour]]
            depth -= 1
            # alreadyfound, foundPortals = distanceto2(innerPortals[outerPortalsLocations[n]], distance, depth-1, alreadyfound, foundPortals)
        else:
            n = neighbour
        
        if (n, depth) in alreadyfound.keys():
            if alreadyfound[(n, depth)] > distance:
                alreadyfound, foundPortals = distanceto2(n, distance, depth, alreadyfound, foundPortals)
        else:
            alreadyfound, foundPortals = distanceto2(n, distance, depth, alreadyfound, foundPortals)

    return alreadyfound, foundPortals

#TODO this doesn't work. A better path-finding algorith is needed; start with mapping distances between portals. Similar to day 18

foundPortals = []
distances, foundPortals = distanceto2(start)

print(distances[end])
