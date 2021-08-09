import itertools


# Return a list of neighbours that can be visited next
def checkNeighbours(location):
    x,y = location
    neighbours = []
    for d in [-1, 1]:
        if binLayout[y][x+d]:
            neighbours.append((x+d, y))
        if binLayout[y+d][x]:
            neighbours.append((x, y+d))
    return neighbours


# Breadth-first search of the entire layout; add the relevant points to the 
# list of distances
def calculateDistance(point, relevantPoints):
    steps = 0
    front = [(steps, point)]
    visited = [point]
    distances = {}
    
    while front:
        # Check which point in the front has the least steps, and use that point
        front.sort(reverse = True)
        steps, point = front.pop(-1)
        
        # Add all the not-visited neighbours of that point to the list of fronts
        for neighbour in checkNeighbours(point):
            if neighbour not in visited:
                visited.append(neighbour)
                front.append((steps+1, neighbour))
                # If the new neighbour is a relevant point; add it to the distances list
                if neighbour in relevantPoints.values():
                    distances[int(layout[neighbour[1]][neighbour[0]])] = steps+1
                    
                
    return distances


# Sum the distances between all points in a route list
def sumDistance(pointList, distances):
    totalDistance = 0
    for i in range(len(pointList)-1):
        totalDistance += distances[pointList[i]][pointList[i+1]]
        
    return(totalDistance)
    

# =============================================================================
# Read input
# =============================================================================

Pt2 = True

# Open file and create the layout
file = open('input.txt')
layout = [line.strip() for line in file]

# Create the list of relevant points
relevantPoints = {}
binLayout = []
for y, line in enumerate(layout):
    binLayout.append([])
    for x, char in enumerate(line):
        if char.isdigit():
            relevantPoints[int(char)] = (x,y)
            binLayout[-1].append(True)
        elif char == '.':
            binLayout[-1].append(True)
        elif char == '#':
            binLayout[-1].append(False)
        else:
            print("Error", char)
            
# =============================================================================
# Calculate distance between all points
# =============================================================================

distances = {}

for point in relevantPoints:
    distances[point] = calculateDistance(relevantPoints[point], relevantPoints)

# =============================================================================
# Calculate the distance of all routes
# =============================================================================

shortestDistance1 = 2**32
shortestDistance2 = 2**32

for path in itertools.permutations(range(1,8)):
    path1 = [0] + list(path)
    path2 = [0] + list(path) + [0]
    distance1 = sumDistance(path1, distances)
    distance2 = sumDistance(path2, distances)
    
    if distance1 < shortestDistance1:
        shortestDistance1 = distance1
        
    if distance2 < shortestDistance2:
        shortestDistance2 = distance2

print("The answer to part 2:", shortestDistance1)
print("The answer to part 2:", shortestDistance2)
