import re

file = open('2018/Day 3/input.txt').readlines()
data = [[int(i) for i in re.split(' @ |,|: |x', x.strip('#\n'))] for x in file]

claimed = set()
double = set()

for _, x1, y1, dx, dy in data[:]:
    for x in range(x1, x1+dx):
        for y in range(y1, y1+dy):
            if (x, y) in claimed:
                double.add((x, y))
            else:
                claimed.add((x, y))

print(f'The answer to part 1: {len(double)}')

for ID, x1, y1, dx, dy in data:
    overlap = False
    for x in range(x1, x1+dx):
        for y in range(y1, y1+dy):
            if (x,y) in double:
                overlap = True
                break
        if overlap:
            break
    # print(overlap)
    if not overlap:
        print(f'The answer to part 2: {ID}')
        break
