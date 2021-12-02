file = open('input.txt').readlines()

data = [x.strip().split() for x in file]

pos = 0
depth = 0
aim = 0

for line in data:
    if line[0] == 'down':
        # depth += int(line[1])
        aim += int(line[1])
    elif line[0] =='up':
        # depth -= int(line[1])
        aim -= int(line[1])
    elif line[0] =='forward':
        pos += int(line[1])
        depth += aim*int(line[1])

ans1 = ans2 = 0

print(data)

print('The answer to part 1: ', pos*depth)
print('The answer to part 2: ', ans2)
