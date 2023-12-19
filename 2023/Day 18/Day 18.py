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

def score(walls, r1, r2): # TODO: Startline isn't really needed, we can also add the line score right away whenever there's 2 corners
    score = 0
    i = 0

    while i < len(walls):
        # Find the starting point
        if (r1, walls[i]) in corners:
            if corners[(r1, walls[i])] == 'Upper':
                if corners[(r1, walls[i+1])] == 'Upper':
                    score += (walls[i+1] - walls[i] + 1) * (r2 - r1)
                    i += 2
                    continue
                elif corners[(r1, walls[i+1])] == 'Lower':
                    startline = startrange = walls[i]
                    i += 2
            elif corners[(r1, walls[i])] == 'Lower':
                if corners[(r1, walls[i+1])] == 'Upper':
                    startline = walls[i]
                    startrange = walls[i+1]
                    i += 2
                elif corners[(r1, walls[i+1])] == 'Lower':
                    score += (walls[i+1] - walls[i] + 1)
                    i += 2
                    continue
            else:
                raise ValueError
        else:
            startline = startrange = walls[i]
            i += 1

        s, i = findend(walls, r1, r2, startline, startrange, i)
        # print(s, i)
        score += s

    return score

def findend(walls, r1, r2, startline, startrange, i):
    if (r1, walls[i]) in corners:
        if corners[(r1, walls[i])] == 'Upper':
            if corners[(r1, walls[i+1])] == 'Upper':
                range1 = walls[i] - startrange + 1
                line = walls[i+1] - startline
                score = line + range1 * (r2-r1-1)
                i += 2
                s, i = findend(walls, r1, r2, walls[i-1], walls[i-1], i)
                score += s
                return score, i
            elif corners[(r1, walls[i+1])] == 'Lower':
                range1 = walls[i] - startrange + 1
                line = walls[i+1] - startline + 1
                score = line + range1 * (r2-r1-1)
                i += 2
                return score, i
        elif corners[(r1, walls[i])] == 'Lower':
            if corners[(r1, walls[i+1])] == 'Upper':
                line = walls[i+1] - startline + 1
                range1 = walls[i+1] - startrange + 1
                score = line + range1 * (r2-r1-1)
                i += 2
                return score, i
            elif corners[(r1, walls[i+1])] == 'Lower':
                i += 2
                score, i = findend(walls, r1, r2, startline, startrange, i)
                return score, i
        else:
            raise ValueError
    else:
        range1 = walls[i] - startrange + 1
        line = walls[i] - startline + 1
        score = line + range1 * (r2-r1-1)
        i += 1
        return score, i

file = open('input.txt').readlines()

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

part1 = False

for command, length, colour in instructions:
    d = direction[command]
    for _ in range(int(length)):
        position = move(position, d)
        dug.add(position)

    length2, d2 = readhex(colour)
    if part1:
        length2, d2 = int(length), d

    if d2 == direction['U']:
        corners[position2] = 'Lower'
        position2 = move(position2, d2, length2)
        corners[position2] = 'Upper'
    elif d2 == direction['D']:
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

for command, l, colour in instructions:
    length, d = readhex(colour)
    if part1:
        d = direction[command]
        length = int(l)
    newposition = move(position, d, length)

    if d in [(-1, 0), (1, 0)]:
        for r in relevantrows:
            if min(position[0],newposition[0]) <= r <= max(position[0], newposition[0]):
                walls[r].append(newposition[1])     # Walls included corners
    position = newposition

ans2 = 0
relevantrows = sorted(relevantrows)

for r1, r2 in zip(relevantrows[0:-1], relevantrows[1:]):

    # print(r1, r2)
    w = sorted(walls[r1])
    ans2 += score(w, r1, r2)


# Add the last row
w = sorted(walls[r2])
for w1, w2 in zip(w[0:-1:2], w[1::2]):
    ans2 += w2 - w1 + 1

print('The answer to part 2: ', ans2)
