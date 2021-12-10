def findBasin(point, basin):
    for n in findNeighbours(point):
        x, y = n
        if n not in basin and m[x][y] != '9':
            basin.append(n)
            findBasin(n, basin)
    # return basin


def findNeighbours(point):
    x, y = point
    d = (-1, 1)
    n = []
    for dx in d:
        if 0 <= x+dx <= size-1:
            n.append((x+dx, y))
    for dy in d:
        if 0 <= y+dy <= size-1:
            n.append((x, y+dy))
    return(n)

file = open('input.txt').readlines()
m = [x.strip() for x in file]
ans1 = ans2 = 0

lows = []
    
size = len(m)
    
for x, line in enumerate(m):
    for y, c in enumerate(line):
        low = True
        for n in findNeighbours((x,y)):
            nx, ny = n
            if int(c) >= int(m[nx][ny]):
                low = False
                
        if low:
            ans1 += int(c) + 1
            lows.append((x, y))

basins = []
sizes = []

for low in lows:
    basin = []
    findBasin(low, basin)
    basins.append(basin)
    sizes.append(len(basin))

sizes.sort()
ans2 = sizes[-1]*sizes[-2]*sizes[-3]

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)