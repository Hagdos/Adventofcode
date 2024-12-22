import heapq as hq

class Tiles:
    def __init__(self, data=None, size = [10, 10]):
        if data:
            self.tiles = [[x for x in row] for row in data.strip().split('\n')]
        else:
            self.tiles = [['.' for _ in range(size[1])] for _ in range(size[0])]
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def getTile(self, location):
        return self.tiles[location[0]][location[1]]

    def setTile(self, location, char):
        self.tiles[location[0]][location[1]] = char

    def getSize(self):
        return (len(self.tiles), len(self.tiles[0]))

    def step(self, location, direction):
        return (location[0] + direction[0], location[1] + direction[1])
        # return tuple([location[i] + direction[i] for i in (0, 1)])

    def inRange(self, location):
        return 0 <= location[0] < len(self.tiles) and 0 <= location[1] < len(self.tiles[0])

    def neighbours(self, pos):
        for d in self.directions:
            step = self.step(pos, d)
            if self.inRange(step):
                yield self.step(pos, d)

    # Manhattan distance
    def distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def Dijkstra(self, start, end):
        Queue = []
        hq.heappush(Queue, (0, start))
        scores = {start: 0}

        while Queue:
            (currentScore, position) = hq.heappop(Queue)

            if position == end:
                return currentScore

            # Check all neighbours:
            for n in self.neighbours(position):
                if self.getTile(n) == '.':
                    if n not in scores or currentScore + 1 < scores[n]:
                        scores[n] = currentScore + 1
                        hq.heappush(Queue, (currentScore + 1, n))

    def Astar(self, start, end):
        Queue = []
        hq.heappush(Queue, (self.distance(start, end), 0, start))   # Score, distance walked, position
        distances = {start: 0}

        while Queue:
            (currentScore, distance, position) = hq.heappop(Queue)

            if position == end:
                return distance

            # Check all neighbours:
            for n in self.neighbours(position):
                if self.getTile(n) == '.':
                    if n not in distances or distance + 1 < distances[n]:
                        distances[n] = distance + 1
                        hq.heappush(Queue, (distance + 1 + self.distance(n, end), distance + 1, n))


    def __str__(self):
        string = ''
        for row in self.tiles:
            for char in row:
                string += char
            string += '\n'
        return string