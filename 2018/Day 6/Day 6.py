file = open('2018/Day 6/input.txt').readlines()
points = set(tuple(int(i) for i in x.strip().split(', ')) for x in file)

size = max([max(x) for x in points])

chart = dict()
ans2 = 0

for x in range(size+1):
    for y in range(size+1):
        mindistance = size*size
        sumdistance = 0
        for px, py in points:
            distance = abs(x-px) + abs(y-py)
            sumdistance += distance
            if distance < mindistance:
                mindistance = distance
                bestpoint = [(px, py)]
            elif distance == mindistance:
                bestpoint.append((px, py))
        if len(bestpoint) == 1:
            chart[(x, y)] = bestpoint[0]
        else:
            chart[(x, y)] = None
        if sumdistance < 10000:
            ans2 += 1

            # distances[(px, py)] = distance
        # chart[(x, y)] = distances

infinite = set()
for x in [0, size]:
    for y in range(size+1):
        infinite.add(chart[(x, y)])
        points.discard(chart[(x, y)])
for y in [0, size]:
    for x in range(size+1):
        infinite.add(chart[(x, y)])
        points.discard(chart[(x, y)])

groupsizes = {point: 0 for point in points}
for x in range(size + 1):
    for y in range(size + 1):
        if chart[(x, y)] in points:
            groupsizes[chart[(x, y)]] += 1

print(f'The answer to part 1: {max(groupsizes.values())}')
print(f'The answer to part 2: {ans2}')
