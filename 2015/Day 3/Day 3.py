xloc = yloc = 0
housesVisited = set()
housesVisited.add((xloc, yloc))

instructions = open('input.txt').read()

for direction in instructions:
    if direction == '^':
        yloc += 1
    elif direction == 'v':
        yloc -= 1
    elif direction == '>':
        xloc += 1
    elif direction == '<':
        xloc -= 1
    else:
        print("Error")
        break
        
    housesVisited.add((xloc, yloc))
    
print("Answer to part 1:", len(housesVisited))


# =============================================================================
# Part 2
# =============================================================================

xlocSanta = ylocSanta = 0
xlocRobot = ylocRobot = 0
Santa = True

housesVisited = set()
housesVisited.add((xlocSanta, ylocSanta))

instructions = open('input.txt').read()

for direction in instructions:
    if Santa == True:
        if direction == '^':
            ylocSanta += 1
        elif direction == 'v':
            ylocSanta -= 1
        elif direction == '>':
            xlocSanta += 1
        elif direction == '<':
            xlocSanta -= 1
        else:
            print("Error")
            break
        Santa = False
        housesVisited.add((xlocSanta, ylocSanta))
    else:
        if direction == '^':
            ylocRobot += 1
        elif direction == 'v':
            ylocRobot -= 1
        elif direction == '>':
            xlocRobot += 1
        elif direction == '<':
            xlocRobot -= 1
        else:
            print("Error")
            break
        Santa = True
        housesVisited.add((xlocRobot, ylocRobot))
    
    
print("Answer to part 2:", len(housesVisited))

