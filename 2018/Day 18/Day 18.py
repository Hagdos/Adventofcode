from itertools import product


def printArea(area):
    for row in area:
        print(row)
    print()


def countNeighbours(area, row, column):
    neighbours = dict()
    neighbours[OPEN] = 0
    neighbours[TREES] = 0
    neighbours[LUMBER] = 0

    for dr, dc in product((-1, 0, 1), (-1, 0, 1)):
        if dr == dc == 0:
            continue
        if 0 <= row + dr < len(area) and 0 <= column + dc < len(area[0]):
            neighbours[area[row+dr][column+dc]] += 1

    return neighbours[OPEN], neighbours[TREES], neighbours[LUMBER]


def createNewArea(area):
    newarea = []
    for row in range(size):
        newrow = ''
        for column in range(size):
            open, trees, lumber = countNeighbours(area, row, column)
            if area[row][column] == OPEN and trees >= 3:
                newrow += TREES
            elif area[row][column] == TREES and lumber >= 3:
                newrow += LUMBER
            elif area[row][column] == LUMBER and (lumber == 0 or trees == 0):
                newrow += OPEN
            else:
                newrow += area[row][column]
        newarea.append(newrow)
    return newarea


def countAns(area):
    # Count wooded and lumber squares:
    trees = lumber = 0
    for row in area:
        for square in row:
            if square == TREES:
                trees += 1
            elif square == LUMBER:
                lumber += 1

    return trees * lumber

file = open('2018/Day 18/input.txt')
area = [line.strip() for line in file]

size = len(area)

areas = [area]

OPEN = '.'
TREES = '|'
LUMBER = '#'

for i in range(1, 1000):
    area = createNewArea(area)

    if i == 10:
        print(f'The answer to part 1: {countAns(area)}')

    # If a previous state has been found, there's a cycle.
    # The length of the cycle can be used to skip a lot of iterations
    if area in areas:
        cyclestart = areas.index(area)
        cyclelength = i - cyclestart
        remainingsteps = (1000000000-cyclestart) % cyclelength

        print(f'The answer to part 2: {countAns(areas[cyclestart+remainingsteps])}')
        break
    else:
        areas.append(area)





# 233400 is too low
