def direction(a, b):
    if a != b:
        return int((a-b)/abs(a-b))
    return 0


def diff(a, b):
    return abs(a-b)


def checkSafety1(line):
    np = line[0]
    d = direction(line[1], line[0])

    for n in line[1:]:
        if not 0 < diff(n, np) <= 3 or not direction(n, np) == d:
            return False
        np = n

    return True


def checkSafety2faster(line):
    errors = 0
    np = line[0]
    d = direction(line[1], line[0])

    for i, n in enumerate(line[1:]):
        if not 0 < diff(n, np) <= 3 or not direction(n, np) == d:
            errors += 1
            if errors > 1:
                return False
            elif i == 0 or i == 1:
                if checkSafety1(line[1:]):
                    return True
                if checkSafety1([line[0]]+line[2:]):
                    return True
        else:
            np = n

    return True


def checkSafety2(line):
    if checkSafety1(line):
        return True
    for i in range(len(line)):
        if checkSafety1(line[:i]+line[i+1:]):
            return True
    return False


file = open('input.txt').readlines()

data = [[int(y) for y in x.strip().split()] for x in file]

ans1 = ans2 = 0

for line in data:
    if checkSafety1(line):
        ans1 += 1
    if checkSafety2(line):
        ans2 += 1
    # if checkSafety2faster(line):
    #     ans2 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
