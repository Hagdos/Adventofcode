import numpy as np

def printPattern(pattern):
    for row in pattern:
        print(''.join(row))

def findMirror(pattern):
    for r in range(len(pattern)-1):
        found = True
        for dr in range(min(r+1, len(pattern)-r-1)):
            if np.any(pattern[r-dr] != pattern[r+dr+1]):
                found = False
                break
        if found:
            return r+1
    return 0

def findMirror2(pattern):
    for r in range(len(pattern)-1):
        found = True
        smudges = 0
        for dr in range(min(r+1, len(pattern)-r-1)):
            if np.count_nonzero(pattern[r-dr] != pattern[r+dr+1]) > 1:
                found = False
                break
            elif np.count_nonzero(pattern[r-dr] != pattern[r+dr+1]) == 1 and smudges == 0:
                smudges = 1


        if found and smudges == 1:
            return r+1
    return 0

file = open('input.txt')
ans1 = ans2 = 0

patterns = []
pattern = []
for line in file:
    if line == '\n':
        patterns.append(np.array(pattern)) # Copy?
        pattern = []
    else:
        pattern.append([c for c in line.strip()])
patterns.append(np.array(pattern))


for pattern in patterns:
    # print(pattern)
    # horizontal = findMirror(pattern)*100
    # if horizontal:
    #     ans1 += horizontal
    # else:
    #     ans1 += findMirror(np.rot90(pattern, -1))
    ans1 += findMirror(pattern)*100 + findMirror(np.rot90(pattern, -1))

    # horizontal = findMirror2(pattern)*100
    # if horizontal:
    #     ans2 += horizontal
    # else:
    #     ans2 += findMirror2(np.rot90(pattern, -1))
    ans2 += findMirror2(pattern)*100 + findMirror2(np.rot90(pattern, -1))


# ans1 += findMirror(patterns[3])

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

# 26900 is too low
# 27203