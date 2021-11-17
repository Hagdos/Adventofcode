def magnitude(vector):
    length = 0
    for v in vector:
        length += v*v
    return length**0.5


data = open('2017/Day 20/input.txt').read().splitlines()

data = [x.split(', ') for x in data]

positions = [x[0][3:-1].split(',') for x in data]
speeds = [x[1][3:-1].split(',') for x in data]
accelerations = [x[2][3:-1].split(',') for x in data]

positions = [[int(i) for i in j] for j in positions]
speeds = [[int(i) for i in j] for j in speeds]
accelerations = [[int(i) for i in j] for j in accelerations]

lowestacc = 100000
for i, a in enumerate(accelerations):
    if magnitude(a) < lowestacc:
        lowestacc = magnitude(a)
        ans1 = i

print("The answer to part 1:", ans1)
