# Return the manhattan distance between two points
def distance(p1, p2):
    distance = 0
    for dim in range(len(p1)):
        distance += abs(p1[dim] - p2[dim])

    return distance


def addPoint(constellation, points, point):
    constellation.add(point)
    points.discard(point)
    inrange = set()
    for np in points:
        if distance(np, point) <= 3:
            inrange.add(np)

    for np in inrange:
        addPoint(constellation, points, np)


points = open('2018/Day 25/input.txt').readlines()
points = set([tuple(int(i) for i in point.strip().split(',')) for point in points])

constellations = []

while points:
    constellation = set()
    addPoint(constellation, points, points.pop())
    constellations.append(constellation)

print(len(constellations))
