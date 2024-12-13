from collections import defaultdict


def neighbours(location):
    r, c = location
    neighbours = {}
    for dir, nlocation in enumerate([(r+1, c), (r, c+1), (r-1, c), (r, c-1)]):
        if nlocation in vegetables:
            neighbours[dir] = nlocation
        else:
            neighbours[dir] = None
    return neighbours


def checkSize(location, group):
    seen.add(location)
    groups[location] = group
    area = 1
    perimeter = 0

    for dir, n in neighbours(location).items():
        if vegetables[location] is not vegetables[n]:
            perimeter += 1

        if vegetables[location] is vegetables[n] and n not in seen:
            narea, nperimeter = checkSize(n, group)
            area += narea
            perimeter += nperimeter

    return area, perimeter


file = open('input.txt').readlines()

data = [x.strip() for x in file]
# print(data)
ans1 = ans2 = 0

vegetables = {None: None}

for r, line in enumerate(data):
    for c, char in enumerate(line):
        vegetables[(r, c)] = char

## Part 1

seen = {None}
groups = defaultdict(int)
groupsizes = {}

group = 1 # Group 0 is default value for groups; outside of area

for location in vegetables:
    if location not in seen:
        area, perimeter = checkSize(location, group)

        groupsizes[group] = area
        group += 1
        ans1 += area * perimeter


## Part 2

rrange = len(data)
crange = len(line)
fences = defaultdict(int)

prevborder = (0, 0)
for r in range(rrange+1):
    for c in range(crange):
        border = (groups[(r-1, c)], groups[(r, c)])

        if border != prevborder:  # If something changed
            if border[0] != border[1]:  # And we're actually looking at a fence
                if prevborder[0] == prevborder[1]:  # And there used to be no fence
                    fences[border[0]] += 1  # There is a new fence for both groups
                    fences[border[1]] += 1

                # If there used to be a fence too; only the side that changed
                # gets a new fence (this can still be both sides)
                else:
                    for i in range(2):
                        if border[i] != prevborder[i]:
                            fences[border[i]] += 1
        prevborder = border

prevborder = (0, 0)
for c in range(crange+1):
    for r in range(rrange):
        border = (groups[(r, c-1)], groups[(r, c)])

        if border != prevborder:  # Something changed
            if border[0] != border[1]:  # And we're actually looking at a fence
                if prevborder[0] == prevborder[1]:  # And there used to be no fence
                    fences[border[0]] += 1  # There is a new fence for both groups
                    fences[border[1]] += 1

                # If there used to be a fence too; only the side that changed
                # gets a new fence (this can still be both sides)
                else:
                    for i in range(2):
                        if border[i] != prevborder[i]:
                            fences[border[i]] += 1
        prevborder = border


for g in groupsizes:
    ans2 += groupsizes[g] * fences[g]

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)


