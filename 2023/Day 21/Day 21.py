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

distancefromstart = dijkstra(start)
ans1 = 0
for point in distancefromstart:
    if distancefromstart[point] <= 64:
        if not distancefromstart[point]%2:
            ans1 += 1

print('The answer to part 1: ', ans1)

# Part 2

corners = [(0, 0), (0, SIZE-1), (SIZE-1, SIZE-1), (SIZE-1, 0)]      # Every opposing corner/wall is always 2 steps away
walls = [(0, 65), (65, 0), (SIZE-1, 65), (65, SIZE-1)]

distancemaps = {p: dijkstra(p) for p in corners+walls}

totalsteps = 26501365
ans2 = 0
for point in distancemaps[corners[0]]: # It doesn't matter which distancemaps, we just need all point that are not rocks
    if distancefromstart[point]%2:
        ans2 += 1

    for i in range(4):
        # Iterate over all walls
        dpoint = distancemaps[walls[i]][point] # Distance point2wall
        spoint = distancemaps[walls[i-2]][start] # Distance start2wall (opposite)

        if dpoint % 2: # If odd
            ans2 += (totalsteps - dpoint - spoint - 1)//(2*SIZE) + 1
        else:
            ans2 += (totalsteps - dpoint - spoint - 1 + SIZE)//(2*SIZE)

        # Iterate over all corners
        dpoint = distancemaps[corners[i]][point] # Distance point2wall
        spoint = distancemaps[corners[i-2]][start] # Distance start2wall (opposite)

        if dpoint % 2: # If odd
            n = (totalsteps - dpoint - spoint - 2)//(2*SIZE) + 1
            ans2 += n**2
        else:
            n = (totalsteps - dpoint - spoint - 2 + SIZE)//(2*SIZE)
            ans2 += n*(n+1)


print('The answer to part 2: ', ans2)