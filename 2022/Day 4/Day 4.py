def allWithinRange(range, numbers):
    for n in numbers:
        if not(n >= min(range) and n <= max(range)):
            return False

    return True


def anyWithinRange(range, numbers):
    for n in numbers:
        if n >= min(range) and n <= max(range):
            return True
    return False


file = open('2022/Day 4/input.txt').readlines()

list = [[list(map(int, y.split('-'))) for y in x.strip().split(',')] for x in file]

ans1 = ans2 = 0
START = 0
END = 1

for pair in list:
    if allWithinRange(pair[1], pair[0]) or allWithinRange(pair[0], pair[1]):
        ans1 += 1

    if anyWithinRange(pair[0], pair[1]) or anyWithinRange(pair[1], pair[0]):
        ans2 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
