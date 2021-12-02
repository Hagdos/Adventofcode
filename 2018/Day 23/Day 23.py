file = open('2018/Day 23/input.txt').readlines()
data = [x.strip().split() for x in file]

ans1 = ans2 = 0
maxrange = 0
positions = []
ranges = []
for line in data:
    position = [int(i) for i in line[0].strip('pos=<,>').split(',')]
    range = int(line[1].strip('r='))
    if range > maxrange:
        maxrange = range
        bestposition = position

    positions.append(position)
    ranges.append(range)

ans1 = sum([sum([abs(i-j) for i, j in zip(position, bestposition)]) <= maxrange for position in positions])


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
