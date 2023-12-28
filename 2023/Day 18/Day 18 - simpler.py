def readhex(hexcode, direction):
    d = direction[int(hexcode[-2])]
    distance = int(hexcode[2:-2], 16)

    return distance, d


def move(area, yposition, direction, length):
    if direction[1]:
        area -= yposition*direction[1]*length
    else:
        yposition = yposition+direction[0]*length

    if direction == (0, 1):
        area += length
    elif direction == (1, 0):
        area += length

    return area, yposition


def solve_part1(instructions):
    dtable = {'U': (-1, 0),
              'D': (1, 0),
              'L': (0, -1),
              'R': (0, 1)}

    area = 0
    yposition = 0
    for command, length, _ in instructions:
        direction = dtable[command]
        area, yposition = move(area, yposition, direction, int(length))

    return area+1


def solve_part2(instructions):
    dtable = {3: (-1, 0),
              1: (1, 0),
              2: (0, -1),
              0: (0, 1)}

    area = 0
    yposition = 0
    for _, _, colour in instructions:
        length, direction = readhex(colour, dtable)
        area, yposition = move(area, yposition, direction, length)

    return area+1


file = open('input.txt').readlines()
instructions = [x.strip().split() for x in file]

print(f'The answer to part 1: {solve_part1(instructions)}')
print(f'The answer to part 2: {solve_part2(instructions)}')
