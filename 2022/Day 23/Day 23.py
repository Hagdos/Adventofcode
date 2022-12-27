def printElves(elves, size):
    for r in range(size[0][0], size[0][1]):
        line = [str(r)  ]
        for c in range(size[1][0], size[1][1]):
            if (r, c) in elves:
                line.append('#')
            else:
                line.append('.')

        print(''.join(line))
    print()


# Returns True if there's a neighbouring elf. Starts at top left and goes clockwise.
# Returns top left elf at the end too to make life easier.
def checkNeighbours(elf, elves):
    r, c = elf
    neighbours = [False]*8
    for i, (dr, dc) in enumerate(((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))):
        if (r+dr, c+dc) in elves:
            neighbours[i] = True

    neighbours.append(neighbours[0])
    return neighbours

# (Rows, columns) Order = N S W E
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
dToN = {0: 0, # North
        1: 4, # South
        2: 6, # West
        3: 2} # East

file = open('input.txt').readlines()
elves = set()

r = 0
for line in file:
    c = 0
    for char in line.strip():
        if char == '#':
            elves.add((r, c))
        c += 1
    r += 1


for roundCounter in range(10000):
    # Play a round
    nextelves = {e: () for e in elves}
    prevelves = dict()

    for e in nextelves:
        n = None

        neighbours = checkNeighbours(e, elves)

        # Determine next step for each elf
        # First check for no elves, don't move if there are no elves around
        if any(neighbours):
            # Then check each direction
            for i in range(4):
                # Direction-counter; dep on the roundnumber
                # Correct order is north, south, west, east (0, 1, 2, 3)
                d = (roundCounter+i)%4
                s = dToN[d]
                if not any(neighbours[s:s+3]):
                    n = tuple(e[j]+directions[d][j] for j in range(2))

                    # If there's already an elve stepping there, set them both back
                    # There can never be more than two elves stepping in the same direction
                    if n in prevelves:
                        nextelves[prevelves[n]] = prevelves[n]
                        n = e
                    break

        if not n:
            n = e

        prevelves[n] = e
        nextelves[e] = n

    newelves = set(nextelves.values())

    if newelves == elves:
        print('The answer to part 2: ', roundCounter+1)
        break

    elves = newelves

    # print(f'Round:  {roundCounter+1}')
    # printElves(elves, [[0, 12], [0, 13]])

    if roundCounter == 9:
        minr = minc = 1
        maxr = maxc = 1

        for e in elves:
            minr = min(minr, e[0])
            maxr = max(maxr, e[0])
            minc = min(minc, e[1])
            maxc = max(maxc, e[1])

        ans1 = (maxr - minr + 1) * (maxc - minc + 1) - len(elves)

# print(nextelves)

        print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans2)

# 4448 is too high
# 3902 is too low