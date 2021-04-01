import copy
file = open('input.txt')

pt2 = False

#Count how many neighbouring lights are on for a single light
def countneighbours(x,y, oldlights):
    neighbours = 0
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if 0 <= x+dx < size:
                if 0 <= y+dy < size:
                    if not (dx == 0 and dy == 0):
                        if oldlights[x+dx][y+dy] == '#':
                            neighbours += 1
    return neighbours

#Check the conditions for a single light, and toggle it in the newlights if necessary
def togglelight(x,y, oldlights, newlights):
    neighbours = countneighbours(x,y, oldlights)
    if oldlights[x][y] == '#' and neighbours not in (2,3):
        newlights[x][y] = '.'
    elif oldlights[x][y] == '.' and neighbours == 3:
        newlights[x][y] = '#'


#Read the input
oldlights = []
for line in file:
    oldlights.append(list(line.strip()))
newlights = copy.deepcopy(oldlights)
    
size = len(oldlights)
    
for _ in range(100):
    #Loop over all lights to check if they need to be toggled.
    for x in range(size):
        for y in range(size):
            togglelight(x,y,oldlights, newlights)
    #Turn the corner lights back on
    if pt2 == True:
        for x in (0,99):
            for y in (0,99):
                newlights[x][y] = '#'
    #Save the new state into the old state, for the next step.
    oldlights = copy.deepcopy(newlights)


#Count the number of lights that are on at the end of the run
count = 0
for x in range(size):
    for y in range(size):
        if newlights[x][y] == '#':
            count += 1
            
print('Answer to part 1/2:', count)

# 4934 is too high
# 2871 is too high