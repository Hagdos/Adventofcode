from collections import defaultdict

def move(location, direction, length=1):
    return ((location[0]+direction[0]*length, location[1]+direction[1]*length))

def drawMap(dug, filename = "map.txt"):
    f = open(filename, "w")
    minr = minc = 0
    maxr = maxc = 0

    for d in dug:
        minr = min(minr, d[0])
        maxr = max(maxr, d[0])
        minc = min(minc, d[1])
        maxc = max(maxc, d[1])

    for r in range(minr, maxr+1):
        line = []
        for c in range(minc, maxc+1):

            if (r,c) == (0, 0):
                line.append('0')
            elif (r,c) in dug:
                line.append('#')
            else:
                line.append(' ')
        f.write(''.join(line))
        f.write('\n')
    f.close()
    return None


def floodfill(dug, origin=(0,0)):
    border = [origin]

    while border:
        location = border.pop()
        for d in direction.values():
            n = move(location, d)
            if n not in dug:
                dug.add(n)
                border.append(n)

    return dug


def readhex(hexcode):
    d = direction2[int(hexcode[-2])]
    distance = int(hexcode[2:-2], 16)

    return distance, d

file = open('Day 18/input.txt').readlines()

instructions = [x.strip().split() for x in file]

direction = {'U': (-1, 0),
             'D': (1, 0),
             'L': (0, -1),
             'R': (0, 1)}

direction2 = {3: (-1, 0),
              1: (1, 0),
              2: (0, -1),
              0: (0, 1)}

position = (0,0)
dug = set([position])

position2 = (0,0)
corners = dict()
relevantrows = set()

for command, length, colour in instructions:
    d = direction[command]
    for _ in range(int(length)):
        position = move(position, d)
        dug.add(position)

    length2, d2 = readhex(colour)
    if d2 == direction['U']:
        corners[position2] = 'Lower'
        position2 = move(position2, d2, length2)
        corners[position2] = 'Upper'
    elif d2 == direction['L']:
        corners[position2] = 'Upper'
        position2 = move(position2, d2, length2)
        corners[position2] = 'Lower'
    else:
        position2 = move(position2, d2, length2)
        
    relevantrows.add(position2[0])

dug = floodfill(dug, (1, 1))
print('The answer to part 1: ', len(dug))
position = (0,0)
walls = defaultdict(list)

for _, _, colour in instructions:
    length, d = readhex(colour)
    newposition = move(position, d, length)
    if d2 in [(-1, 0), (1, 0)]:
        for r in relevantrows:
            if min(position[0],newposition[0]) <= r <= max(position[0], newposition[0]):
                walls[r].append(newposition[1])     # Walls included corners
    position = newposition

ans2 = 0
for r in sorted(relevantrows):
    w = sorted(walls[r])
    print(w)
    # i = 0
    # while i < len(w):
    #     # The first wall (or corner) is the start of the line and/or block/range
    #     if (r, w[i]) not in corners:
    #         startline = startrange = w[i]
    #     elif corners[(r, w[i])] == 'Upper':
    #         startline = startrange = w[i]
    #         if corners[(r, w[i+1])] == 'Lower':
    #             i += 1 #Skip this "wall"
    #         # If second corner is also upper, it's an endpoint
    #     elif corners[(r, w[i])] == 'Lower':
    #         startline = w[i]
    #         if corners[(r, w[i+1])] == 'Lower':
    #             endline = w[i+1] # No range in this case, just the single line
    #             ans2 += endline-startline+1
    #             continue
    #         else:
    #             i+= 1
    #             startrange = w[i]
    #     i += 1

    #     if (r, w[i]) not in corners:
    #         endline = endrange = w[i]

    #     elif corners[(r, w[i])] == 'Upper':
    #         endrange = w[i]
    #         if corners[(r, w[i+1])] == 'Lower':
    #             i += 1
    #             endline= w[i]
    #         else:

            


    print(r)

print('The answer to part 2: ', len(corners))



# Rough idea:
    # First only store the corners, and make a list of rows that have corners

# There are multiple rows that have 4 corners, some even have 6
    # Then iterate the instructions, and make a list of vertical wall units for the rows that have a corner (Only vertical! But including the corners)
    # Then for each row, calculate the width between vertical wall units, and multiply it with the height between rows
    # To calculate width: Start counting at every wall, stop counting at every wall. Corners always come in pairs: If outside take the first corner, if inside take the second corner
    # Assert if corners really come in pairs?