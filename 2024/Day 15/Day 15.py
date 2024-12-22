class Tiles:
    def __init__(self, data):
        self.tiles = [[x for x in row] for row in data.split('\n')]

    def getTile(self, location):
        return self.tiles[location[0]][location[1]]

    def setTile(self, location, char):
        self.tiles[location[0]][location[1]] = char

    def getSize(self):
        return (len(self.tiles[0]), len(self.tiles))

    def __str__(self):
        string = ''
        for row in self.tiles:
            for char in row:
                string += char
            string += '\n'
        return string

    def getScore(self):
        score = 0
        for r, row in enumerate(self.tiles):
            for c, char in enumerate(row):
                if char == 'O':
                    score += 100*r+c
        return score


class Tiles2(Tiles):
    def __init__(self, data):
        self.tiles = []
        for rp, row in enumerate(data.split('\n')):
            r = []
            for c, char in enumerate(row):
                if char == "O":
                    r.append('[')
                    r.append(']')
                elif char == '@':
                    self.pos = (rp, c*2)
                    r. append('.')
                    r. append('.')
                else:
                    r.append(char)
                    r.append(char)
            self.tiles.append(r)

    def getScore(self):
        score = 0
        for r, row in enumerate(self.tiles):
            for c, char in enumerate(row):
                if char == '[':
                    score += 100*r+c
        return score

def step(location, direction):
    return tuple([location[i] + direction[i] for i in (0, 1)])


def moveRobot1(location, direction):
    nstep = step(location, direction)
    if tiles.getTile(nstep) == '.':
        move = True
    elif tiles.getTile(nstep) == '#':
        move = False
    elif tiles.getTile(nstep) in ['O', '[', ']']:
        move = moveRobot1(nstep, direction)

    if move:
        tiles.setTile(nstep, tiles.getTile(location))

    return move


# Only used for moving up or down, for left and right use moveRobot1
# BFS return a list of all parts that have to move, and if they can move (AND all)
# If they can move, move from the rear backwards...
def moveRobot2(location, direction):
    Queue = [location]
    blocks = set()

    while Queue:
        loc = Queue.pop()


        if loc in blocks:
            continue
        blocks.add(loc)

        nstep = step(loc, direction)

        if tiles.getTile(nstep) == '.':
            continue
        elif tiles.getTile(nstep) == '#':
            return None
        elif tiles.getTile(nstep) == '[':
            Queue.append(nstep)
            Queue.append(step(nstep, directions['>']))
        elif tiles.getTile(nstep) == ']':
            Queue.append(nstep)
            Queue.append(step(nstep, directions['<']))
        else:
            raise ValueError

    if direction == directions['^']:
        return sorted(list(blocks))

    return sorted(list(blocks), reverse=True)


""" Part 1 """
file = open('input.txt').read()
tiles, moves = file.split('\n\n')
tiles = Tiles(tiles)
moves = ''.join(moves.split())

directions = {'^': (-1, 0),
              'v': (1, 0),
              '<': (0, -1),
              '>': (0, 1)}


for r in range(tiles.getSize()[0]):
    for c in range(tiles.getSize()[1]):
        if tiles.getTile((r, c)) == "@":
            pos = (r, c)
            tiles.setTile(pos, '.')
            break

for move in moves:
    direction = directions[move]
    if moveRobot1(pos, direction):
        pos = step(pos, direction)

print('The answer to part 1: ', tiles.getScore())

""" Part 2 """
tiles, _ = file.split('\n\n')
tiles = Tiles2(tiles)
pos = tiles.pos

# print(moveRobot2((2, 6), directions['v']))

for move in moves:

    # print(tiles, pos, move)
    direction = directions[move]

    # For left and right, re-use moveRobot1.
    if move in ('<', '>'):
        if moveRobot1(pos, direction):
            pos = step(pos, direction)

    else:
        blocks = moveRobot2(pos, direction)
        if blocks:
            for block in blocks:
                tiles.setTile(step(block, direction), tiles.getTile(block))
                tiles.setTile(block, '.')
            pos = step(pos, direction)

print(tiles)

print('The answer to part 2: ', tiles.getScore())
