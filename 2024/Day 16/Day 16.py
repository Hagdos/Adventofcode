class Tiles:
    def __init__(self, data):
        self.tiles = [[x for x in row] for row in data.strip().split('\n')]
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def getTile(self, location):
        return self.tiles[location[0]][location[1]]

    def setTile(self, location, char):
        self.tiles[location[0]][location[1]] = char

    def getSize(self):
        return (len(self.tiles), len(self.tiles[0]))

    def step(self, location, direction):
        return tuple([location[i] + direction[i] for i in (0, 1)])

    def neighbours(self, pos):
        for d in self.directions:
            yield self.step(pos, d)

    def __str__(self):
        string = ''
        for row in self.tiles:
            for char in row:
                string += char
            string += '\n'
        return string


def turn(direction):
    return [(direction[1]*-1, direction[0]*-1), (direction[1], direction[0])]


def part1(tiles, start, direction):
    Queue = [(0, start, direction)]
    scores = {(start, direction): 0}

    while Queue:

        Queue.sort()
        (currentScore, position, direction, ) = Queue.pop()

        # Try a step forward
        forward = tiles.step(position, direction)
        if tiles.getTile(forward) == 'E':
            return currentScore+1

        elif tiles.getTile(forward) == '.':
            if (forward, direction) not in scores or currentScore+1 < scores[(forward, direction)]:
                scores[(forward, direction)] = currentScore + 1
                Queue.append((currentScore+1, forward, direction))

        # Try a turn

        for newdirection in turn(direction):
            if (position, newdirection) not in scores or currentScore+100 < scores[(position, newdirection)]:
                scores[(position, newdirection)] = currentScore + 100
                Queue.append((currentScore+100, position, newdirection))

file = open('input.txt').read()

tiles = tiles.Tiles(file)
ans1 = ans2 = 1275200

start = (tiles.getSize()[0]-2, 1)
direction = (0, 1)

# ans1 = part1(tiles, start, direction)


Queue = [(0, start, direction)]
scores = {(start, direction): 0}
paths = {(start, direction): {start}}
besttiles = set()

while Queue:
    Queue.sort(reverse=True)
    (currentScore, position, direction) = Queue.pop()

    # Try a step forward
    forward = tiles.step(position, direction)

    if tiles.getTile(forward) in ('.', 'E'):
        if (forward, direction) not in scores or currentScore+1 < scores[(forward, direction)]:
            scores[(forward, direction)] = currentScore + 1

            newpath = paths[(position, direction)].copy()
            newpath.add(forward)
            paths[(forward, direction)] = newpath

            Queue.append((currentScore+1, forward, direction))

        elif currentScore+1 == scores[(forward, direction)]:
            paths[(forward, direction)].update(paths[(position, direction)])


    if tiles.getTile(forward) == 'E':
        if currentScore+1 > ans1:
            break
        ans1 = currentScore+1
        besttiles = paths[(forward, direction)]

    # Try a turn
    for newdirection in turn(direction):
        if (position, newdirection) not in scores or currentScore+1000 < scores[(position, newdirection)]:
            scores[(position, newdirection)] = currentScore + 1000
            Queue.append((currentScore+1000, position, newdirection))
            paths[(position, newdirection)] = paths[(position, direction)]

        elif currentScore+1000 == scores[(position, newdirection)]:
            paths[(position, newdirection)].update(paths[(position, direction)])


# for t in besttiles:
#     tiles.setTile(t, 'O')
# print(tiles)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', len(besttiles))
