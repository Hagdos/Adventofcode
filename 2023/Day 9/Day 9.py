def differential(inputlist):
    return [b-a for a,b in zip(inputlist[:-1], inputlist[1:])]

def nextnumberrecursive(inputlist):
    if not any(inputlist):
        return 0
    else:
        return inputlist[-1]+nextnumberrecursive(differential(inputlist))

file = open('input.txt').readlines()

data = [[int(i) for i in x.strip().split()] for x in file]

ans1 = sum((nextnumberrecursive(l) for l in data))
ans2 = sum((nextnumberrecursive(list(reversed(l))) for l in data))

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
