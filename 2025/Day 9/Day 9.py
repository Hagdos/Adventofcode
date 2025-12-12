import pyperclip
import os
import sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

def translate_corner(d):
    return (cdict[d[0]], rdict[d[1]])

def check_square(d1, d2):
    cmin = min(cdict[d1[0]], cdict[d2[0]])
    cmax = max(cdict[d1[0]], cdict[d2[0]])

    rmin = min(rdict[d1[1]], rdict[d2[1]])
    rmax = max(rdict[d1[1]], rdict[d2[1]])

    for c in range(cmin, cmax+1):
        i = 0
        while edges[c][i] <= rmin:
            i += 1
            if i >= len(edges[c]): # This can be optimized for sure; something with for edges[c]...
                return False
        if not edges[c][i] >= rmax:
            return False
        
    return True

file = open('2025/Day 9/input.txt').readlines()

data = [tuple(int(i) for i in x.strip().split(',')) for x in file]
# print(data)
ans1 = ans2 = 0
squares = []
midpoints = set()

rows = set()
columns = set()

for i, d1 in enumerate(data):
    columns.add(d1[0])
    rows.add(d1[1])

    for d2 in data[i:]:
        size = (abs(d2[0]-d1[0])+1)*(abs(d2[1]-d1[1])+1)
        ans1 = max(ans1, size)
        squares.append((size, d1, d2))

for i, d1 in enumerate(data[:-1]):
    d2 = data[i+1]
    midpoint = tuple([(d1[0]+d2[0])//2, (d1[1]+d2[1])//2])
    midpoints.add(midpoint)

squares.sort()
columns = sorted(list(columns))
rows = sorted(list(rows))
corners = sorted(data)

cdict = {}
rdict = {}
for i, c in enumerate(columns):
    cdict[columns[i]] = i
    rdict[rows[i]] = i

# grid = Tiles.Tiles(size=(len(rows), len(columns)))
# for d in data:
#     grid.set_tile((rdict[d[1]], cdict[d[0]]), '#')
# print(grid)


edgerows = set()
edges = []
for c, column in enumerate(columns):
    newedges = (corners[c*2][1], corners[c*2+1][1])
    for n in newedges:
        n = rdict[n]
        if n in edgerows:
            edgerows.remove(n)
        else:
            edgerows.add(n)

    edges.append(sorted(edgerows))

ans1, d1, d2 = squares.pop(-1)

while not check_square(d1, d2):
    ans2, d1, d2 = squares.pop(-1)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
pyperclip.copy(ans2)

# (29, 153) (217, 123)