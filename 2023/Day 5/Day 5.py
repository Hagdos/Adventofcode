def list2ints(l):
    return [int(i) for i in l]


def findintinmap(mapname, seed):
    for m in maps[mapname]:
        if seed in range(m[1], m[1]+m[2]):
            return seed-m[1]+m[0]
    return seed


def findrangeinmap(mapname, start, end):
    newranges = []
    startfound = False
    for m in maps[mapname]:
        if start in range(m[1], m[1]+m[2]):
            startfound = True
            newstart = start-m[1]+m[0]
            if end in range(m[1], m[1]+m[2]):
                newend = end-m[1]+m[0]
                return [(newstart, newend)]
            else:
                newend = m[0]+m[2]-1
                newranges = findrangeinmap(mapname, m[1]+m[2], end)

                newranges.append((newstart, newend))
                return newranges

    # if start not in a range, check if end is
    if not startfound:
        for m in maps[mapname]:
            if end in range(m[1], m[1]+m[2]):
                newend = end-m[1]+m[0]
                newstart = m[0]
                newranges = findrangeinmap(mapname, start, m[1]-1)
                newranges.append((newstart, newend))
                return newranges

    # If end also not found, return the same range
    return [(start, end)]



file = open('input.txt')
ans1 = ans2 = 0

seeds = list2ints(file.readline().split(': ')[1].split())

line = file.readline().strip()
line = file.readline().strip()

maps = {}

while line:

    mapname = line.split()[0]
    maps[mapname] = []


    line = file.readline().strip().split()
    while line:
        numbers = list2ints(line)
        maps[mapname].append(numbers)

        line = file.readline().strip().split()

    line = file.readline().strip()


## Part 1
for seed in seeds:
    for key in maps.keys():
        seed = findintinmap(key, seed)


    if ans1:
        ans1 = min(ans1, seed)
    else:
        ans1 = seed

# ## Part 2
for start, length in zip(seeds[::2], seeds[1::2]):
    ranges = [(start, start+length)]

    for key in maps.keys():
        newranges = []
        for r in ranges:
            # print(r)
            newranges += findrangeinmap(key, r[0], r[1])
        ranges = newranges

    lowest = 0
    for r in ranges:
        if lowest:
            lowest = min(lowest, r[0])
        else:
            lowest = r[0]

    if ans2:
        ans2 = min(ans2, lowest)
    else:
        ans2 = lowest


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
