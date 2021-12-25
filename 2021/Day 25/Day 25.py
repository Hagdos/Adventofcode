from copy import deepcopy

file = open('input.txt').readlines()
floor = [list(x.strip()) for x in file]

height = len(floor)
width = len(floor[0])


steps = 0
moved = True
while moved:
    steps += 1
    moved = False
    nfloor = deepcopy(floor)
    for row in range(height):
        for column in range(width):
            if floor[row][column] == '>':
                n = (column+1)%width
                if floor[row][n] == '.':
                    nfloor[row][column] = '.'
                    nfloor[row][n] = '>'
                    moved = True
    
    floor = nfloor                
    nfloor = deepcopy(floor)
    
    for row in range(height):
        for column in range(width):
            if floor[row][column] == 'v':
                n = (row+1)%height
                if floor[n][column] == '.':
                    nfloor[row][column] = '.'
                    nfloor[n][column] = 'v'
                    moved = True

    floor = nfloor

print('The answer to part 1: ', steps)
