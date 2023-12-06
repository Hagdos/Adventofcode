def mincubes(string):
    mincubes = {'red': 0,
                'blue': 0,
                'green': 0}
    hints = string.replace(',', ';').split('; ')

    for h in hints:
        # print(h)
        n, colour = h.split(' ')
        mincubes[colour] = max(int(n), mincubes[colour])

    return mincubes

def checkpossible(cubes, limits):
    for c in cubes:
        if cubes[c] > limits[c]:
            return False
    return True

file = open('input.txt').readlines()

data = [x.strip().split(": ") for x in file]
ans1 = ans2 = 0

limits  = {'red': 12,
           'blue': 14,
           'green': 13}

for line in data:
    game = int(line[0].split(" ")[1])
    cubes = mincubes(line[1])
    if checkpossible(cubes, limits):
        ans1 += game
    power = 1
    for c in cubes:
        power *= cubes[c]
    ans2 += power

print(mincubes(line[1]))


# print(data)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
