def readInput(filename):

    file = open(filename).readlines()

    blizzards = [set() for _ in range(4)]

    for r, line in enumerate(file):
        for c, char in enumerate(line.strip()):
            if char in charToDirection:
                blizzards[charToDirection[char]].add((r, c))

    size = ((0, r), (0, c))

    return blizzards, size


def runMaze(blizzards, size, start, end):
    reachable = set()

    for roundCounter in range(1, 10000):
        reachable.add(start)
        # Move all blizzards
        newblizzards = [set() for _ in range(4)]
        for direction in range(4):
            for blizzard in blizzards[direction]:
                newblizzard = [blizzard[i] + directions[direction][i] for i in range(2)]
                if newblizzard[0] == size[0][0]:
                    newblizzard[0] = size[0][1]-1
                elif newblizzard[0] == size[0][1]:
                    newblizzard[0] = size[0][0]+1
                elif newblizzard[1] == size[1][0]:
                    newblizzard[1] = size[1][1]-1
                elif newblizzard[1] == size[1][1]:
                    newblizzard[1] = size[1][0]+1


                newblizzards[direction].add(tuple(newblizzard))
        blizzards = newblizzards


        # Find possible next steps
        allblizzards = set().union(*blizzards)
        newreachable = set()
        for spot in reachable:
            for n in [*directions, (0, 0)]:
                newspot = tuple((spot[i] + n[i] for i in range(2)))
                if newspot not in allblizzards:
                    if 0 < newspot[0] < size[0][1] and \
                       0 < newspot[1] < size[1][1]:
                        newreachable.add(newspot)
                if newspot == end:
                    return roundCounter, blizzards
                    break


        reachable = newreachable



UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

charToDirection = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}
#               UP      DOWN     LEFT   RIGHT
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


blizzards, size = readInput('input.txt')

start = (0, 1)
end = tuple((size[0][1], size[1][1]-1))

ans1, blizzards = runMaze(blizzards, size, start, end)
r, blizzards = runMaze(blizzards, size, end, start)
s, _ = runMaze(blizzards, size, start, end)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans1+r+s)
# Should be 308
