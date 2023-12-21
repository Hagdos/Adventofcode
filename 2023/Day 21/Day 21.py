def dijkstra(start):
    visited = {start: 0}
    edge = [(start, 0)]

    while edge:
        node, distance = edge.pop(0)
        newnodes = findNeighbours(node)

        for new in newnodes:
            if new not in visited or distance+1 < visited[new]:
                visited[new] = distance+1
                edge.append((new, distance+1))

    return visited


def findNeighbours(location):
    r, c = location
    neighbours = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (r+dr, c+dc) not in rocks:
            if 0 <= r+dr < SIZE and 0 <= c+dc < SIZE:
                neighbours.append((r+dr, c+dc))
    return neighbours

def findNeighbours2(location):
    r, c = location
    neighbours = set()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (r+dr, c+dc) not in rocks:
            for dr2, dc2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (r+dr+dr2, c+dc+dc2) not in rocks:
                    neighbours.add((r+dr+dr2, c+dc+dc2))

    return neighbours

file = open('input.txt').readlines()

data = [x.strip() for x in file]
SIZE = len(data)

rocks = set()

for r, line in enumerate(data):
    for c, char in enumerate(line):
        if char == '#':
            rocks.add((r,c))
        elif char == 'S':
            start = (r,c)

positions = set([start])

# 26501365

for _ in range(64):
    newpositions = set()
    for p in positions:
        newpositions.update(findNeighbours(p))
    positions = newpositions


print('The answer to part 1: ', len(positions))

# Part 2

corners = [(0, 0), (0, SIZE-1), (SIZE-1, SIZE-1), (SIZE-1, 0)]      # Every opposing corner/wall is always 2 steps away
walls = [(0, 65), (65, 0), (SIZE-1, 65), (65, SIZE-1)]

distancemaps = {p: dijkstra(p) for p in corners+walls}

totalsteps = 26501365

for point in distancemaps[corners[0]]: # It doesn't matter which distancemaps, we just need all point that are not rocks
    for i in range(4):
        # Iterate over all walls and corners
        dpoint = distancemaps[walls[i]][point] # Distance point2wall
        spoint = distancemaps[walls[i-2]][start] # Distance start2wall (opposite)


# print('The answer to part 2: ', len(visited))

# Checkable answers:
# 64 steps = 3748
# 65 steps = 3787


# There is a free path along the border, as well as along the middle (r = 65 and c = 65)
# Height == width = 131

# For each point in the map, calculate the distance to each corner and to the middle of each side.
    # This may be easier the other way around; calc the distance from the corner and middle to each side.

# For each point in the map, count in how many maps it is reachable in each direction.
# It's reachable if totalsteps <= start2side + side2point + nmaps*131 AND start2side + side2point + nmaps*131 is odd
# nmaps is the amount of nmaps in between. 0 is the map directly adjacent (including corners)

# For the sides, every nmaps that fulfills the requirements is +1 reachable garden (don't forget to include the 0)
# For the corners every nmaps that fulfills the requiremetns is +nmaps+1 reachable garden


# Part 2 ideas: If i can get there in range-2*n steps, I can get there in range steps (by going back and forth between neighbours)
# If I can get there in an even number of steps, I can never ever get there in an odd number of steps (end goal)

# So what I can do is increase the stepsize to 2, and don't look at already visited nodes.

# To check rocks outside the original graph, use (r+dr)%rowlength (probably + 2 or something for the edges inbetween)