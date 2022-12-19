def calcdistance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def readInput(filename):
    file = open(filename).readlines()

    sensors = []
    beacons = []
    distances = []
    for line in file:
        line = line.strip().split()
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        distance = calcdistance(sensor, beacon)

        sensors.append(sensor)
        beacons.append(beacon)
        distances.append(distance)

    return sensors, beacons, distances


def calcRanges(sensors, distances, y):
    ranges = []
    for sensor, distance in zip(sensors, distances):
        linedist = abs(sensor[1] - y)
        xdist = distance - linedist
        if xdist > 0:
            range = [sensor[0]-xdist, sensor[0]+xdist]
            ranges.append(range)
    ranges.sort()
    return ranges


def solve1(sensors, beacons, distances, y=2000000):
    ranges = calcRanges(sensors, distances, y)

    ans1 = 0
    prevend = ranges[0][0]-1
    for range in ranges:
        start, end = range
        if start > prevend:
            ans1 += end-start+1
            prevend = end
        elif end > prevend:
            ans1 += end-prevend
            prevend = end

    for beacon in set(beacons):
        if beacon[1] == y:
            ans1 -= 1
    return ans1


def solve2(sensors, beacons, distances, size=4000000):
    for y in range(size):
        ranges = calcRanges(sensors, distances, y)
        prevend = ranges[0][0]
        for r in ranges:
            start, end = r
            if start > prevend:
                return (prevend+1)*size+y
            if end > prevend:
                prevend = end

    print('Didn\'t find anything')


sensors, beacons, distances = readInput('2022/Day 15/input.txt')

print('The answer to part 1: ', solve1(sensors, beacons, distances, y=2000000))
print('The answer to part 2: ', solve2(sensors, beacons, distances, size=4000000))
