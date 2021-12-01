file = open('input.txt').readlines()

data = [x.strip() for x in file]

ans1 = ans2 = 0

for d in range(1, len(data)):
    if int(data[d]) > int(data[d-1]):
        ans1 += 1

for d in range(3, len(data)):
    if int(data[d]) > int(data[d-3]):
        ans2 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
