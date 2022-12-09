import numpy as np

file = open('2022/Day 8/input.txt').readlines()
forest = [[int(y) for y in x.strip()] for x in file]
forest = np.array(forest)
ans2 = 0

width = len(forest[0])
height = len(forest)

visible = [[False for _ in range(width)] for _ in range(height)]
visible = np.array(visible)

# Check from the top
for y in range(height):
    for x in range(width):
        north = list(reversed(forest[0:y, x]))
        south = forest[y+1:, x]
        west = list(reversed(forest[y, 0:x]))
        east = forest[y, x+1:]
        # Part 1
        if y == 0 or y == height-1 or x == 0 or x == width-1:
            visible[y, x] = True
        else:
            if forest[y, x] > max(north) or \
               forest[y, x] > max(south) or \
               forest[y, x] > max(east) or \
               forest[y, x] > max(west):
                visible[y, x] = True

        # Part 2
        scenicscore = 1
        for direction in [north, south, west, east]:
            visibletrees = 0
            for tree in direction:
                if tree < forest[y, x]:
                    visibletrees += 1
                else:
                    visibletrees += 1
                    break
            scenicscore *= visibletrees
        ans2 = max(ans2, scenicscore)

print('The answer to part 1: ', len(visible[visible]))
print('The answer to part 2: ', ans2)
