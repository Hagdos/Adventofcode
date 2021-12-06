from collections import defaultdict

file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
ans1 = ans2 = 0

points = defaultdict(int)
points2 = defaultdict(int)

for line in data:
    start = [int(i) for i in line[0].split(',')]
    end = [int(i) for i in line[-1].split(',')]
    
    if start[0] == end[0]:
        x = start[0]
        s = min(start[1], end[1])
        e = max(start[1], end[1])
        for y in range(s, e+1):
            points[(x,y)] += 1
    elif start[1] == end[1]:
        y = start[1]
        s = min(start[0], end[0])
        e = max(start[0], end[0])
        for x in range(s, e+1):
            points[(x,y)] += 1
    else:
        sx = start[0]
        ex = end[0]
        if sx > ex:
            xrange = range(sx, ex-1, -1)
        else:
            xrange = range(sx, ex+1)
        sy = start[1]
        ey = end[1]
        if sy > ey:
            yrange = range(sy, ey-1, -1)
        else:
            yrange = range(sy, ey+1)
        for x,y in zip(xrange, yrange):

            points2[(x,y)] += 1


for point in points.values():
    if point >= 2:
        ans1 += 1

for point in points:
    points2[point] += points[point]
        
for point in points2.values():
    if point >= 2:
        ans2 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)


