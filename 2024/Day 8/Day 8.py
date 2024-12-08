from collections import defaultdict


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def calcAntiNodes1(location1, location2):
    if location1 != location2:
        dx = location1[0] - location2[0]
        dy = location1[1] - location2[1]

        antinode1 = (location1[0]+dx, location1[1]+dy)
        antinode2 = (location2[0]-dx, location2[1]-dy)

        return {antinode1, antinode2}
    return None


def calcAntiNodes2(location1, location2):
    if location1 != location2:
        dx = location1[0] - location2[0]
        dy = location1[1] - location2[1]

        divisor = gcd(dx, dy)
        dx = dx // divisor
        dy = dy // divisor

        antinodes = {location1}
        location = location1

        while (0 <= location[0] < xrange and
               0 <= location[1] < yrange):
            antinodes.add(location)
            location = (location[0] + dx, location[1] + dy)

        location = location1

        while (0 <= location[0] < xrange and
               0 <= location[1] < yrange):
            antinodes.add(location)
            location = (location[0] - dx, location[1] - dy)

        return antinodes
    return None


file = open('input.txt').readlines()

data = [x.strip() for x in file]

ans1 = ans2 = 0

# Read input. Store into a dict with the character as the key and the locations
# as a set

antennaes = defaultdict(set)

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != '.':
            antennaes[char].add((x, y))

xrange = len(line)
yrange = len(data)

antinodes = set()

for frequency in antennaes:
    for location1 in antennaes[frequency]:
        for location2 in antennaes[frequency]:
            nodes = calcAntiNodes1(location1, location2)
            if nodes:
                antinodes.update(nodes)


for location in antinodes:
    if 0 <= location[0] < xrange and \
       0 <= location[1] < yrange:
        ans1 += 1


# Part 2
antinodes = set()

for frequency in antennaes:
    for location1 in antennaes[frequency]:
        for location2 in antennaes[frequency]:
            nodes = calcAntiNodes2(location1, location2)
            if nodes:
                antinodes.update(nodes)


ans2 = len(antinodes)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
