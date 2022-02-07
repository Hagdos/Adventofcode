import re

def printMap(xmin, xmax, ymin, ymax, locations):
    for y in range(ymin, ymax+1):
        line = str(y)
        for x in range(xmin, xmax+1):
            if (x, y) in locations:
                line += '█'
            else:
                line += ' '
        print(line)

    print()

file = open('input.txt').readlines()
lines = [x.strip() for x in file]

points = []

for line in lines:
    matches = re.findall(r'<(.{1,2}\d+),(.{1,2}\d+)>', line)

    p = [int(i) for i in matches[0]]
    v = [int(i) for i in matches[1]]

    points.append([p, v])

times = set()

for point in points:
    for dim in (0, 1):
        arrival = -point[0][dim]//point[1][dim]
        times.add(arrival)

b = min(times)
e = max(times)

for t in range(b, e):
    locations = set()
    for point in points:
        newpoint = []
        for dim in (0, 1):
            newpoint.append(point[0][dim]+point[1][dim]*t)

        locations.add(tuple(newpoint))

    xmin = min([x[0] for x in locations])
    xmax = max([x[0] for x in locations])
    ymin = min([x[1] for x in locations])
    ymax = max([x[1] for x in locations])

    if ymax - ymin < 20:
        print(t)
        printMap(xmin, xmax, ymin, ymax, locations)
