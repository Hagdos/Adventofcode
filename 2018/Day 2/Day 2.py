import string
import itertools

file = open('2018/Day 2/input.txt').readlines()
data = [x.strip() for x in file]

twos = threes = 0

for ID in data:
    two = three = 0
    for char in string.ascii_lowercase:
        if ID.count(char) == 2:
            two = 1
        elif ID.count(char) == 3:
            three = 1

    twos += two
    threes += three

print(f'The answer to part 1: {twos*threes}')

size = len(data[0])
ans2 = ''
for ID1, ID2 in itertools.combinations(data, 2):
    differences = 0
    for i in range(size):
        if ID1[i] != ID2[i]:
            differences += 1

    if differences == 1:
        for i in range(size):
            if ID1[i] == ID2[i]:
                ans2 += ID1[i]

        print(f'The answer to part 2: {ans2}')
