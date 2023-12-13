def distanceBetweenPoints(p1, p2):
    r1 = min(p1[0], p2[0])
    r2 = max(p1[0], p2[0])
    c1 = min(p1[1], p2[1])
    c2 = max(p1[1], p2[1])

    distance1 = r2 - r1 + c2 - c1
    distance2 = distance1

    for r in emptyrows:
        if r1 < r < r2:
                distance1 += 1
                distance2 += 1000000-1

    for c in emptycolumns:
        if c1 < c < c2:
                distance1 += 1
                distance2 += 1000000-1

    return distance1, distance2

file = open('input.txt').readlines()

data = [x.strip() for x in file]

nonemptyrows = set()
nonemptycolumns = set()
galaxies = list()

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == '#':
            nonemptyrows.add(r)
            nonemptycolumns.add(c)
            galaxies.append((r,c))

emptyrows = {r for r in range(len(data)) if r not in nonemptyrows}
emptycolumns = {c for c in range(len(data[0])) if c not in nonemptycolumns}

ans1 = ans2 = 0
for s, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[s+1:]:
        d1, d2 = distanceBetweenPoints(galaxy1, galaxy2)
        ans1 += d1
        ans2 += d2


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)