import heapq as hq


class Tiles:
    def __init__(self, data=None, size=[10, 10]):
        if data:
            self.tiles = [[x for x in row] for row in data.strip().split('\n')]
        else:
            self.tiles = [['.' for _ in range(size[1])] for _ in range(size[0])]
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def get_tile(self, location):
        return self.tiles[location[0]][location[1]]

    def set_tile(self, location, char):
        self.tiles[location[0]][location[1]] = char

    def get_size(self):
        return (len(self.tiles), len(self.tiles[0]))

    # Find one or two symbols in the map, return their locations and set them to normal tiles ('.')
    def find_start_end(self, startsymbol, endsymbol=None):
        size = self.get_size()
        for r in range(size[0]):
            for c in range(size[1]):
                if self.get_tile((r, c)) == startsymbol:
                    start = (r, c)
                elif endsymbol and self.get_tile((r, c)) == endsymbol:
                    end = (r, c)

        self.set_tile(start, '.')
        if endsymbol:
            self.set_tile(end, '.')
            return start, end
        return start

    def step(self, location, direction):
        return (location[0] + direction[0], location[1] + direction[1])

    def in_range(self, location):
        return 0 <= location[0] < len(self.tiles) and 0 <= location[1] < len(self.tiles[0])

    def neighbours(self, pos):
        for d in self.directions:
            step = self.step(pos, d)
            if self.in_range(step):
                yield step

    # Manhattan distance
    def distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def BFS(self, start, end):
        Queue = []
        hq.heappush(Queue, (0, start))  # Score, position
        seen = set()

        while Queue:
            (currentScore, position) = hq.heappop(Queue)

            if position in seen:
                continue

            seen.add(position)

            if position == end:
                return currentScore

            # Check all neighbours:
            for n in self.neighbours(position):
                if self.get_tile(n) == '.':
                    hq.heappush(Queue, (currentScore + 1, n))

    # Same Breadth-First search, but returns the tiles in the shortest path
    def BFS_path(self, start, end):
        Queue = []
        hq.heappush(Queue, (0, start))  # Score, position
        seen = set()
        prev_tile = {start: None}

        while Queue:
            (currentScore, position) = hq.heappop(Queue)

            if position in seen:
                continue

            seen.add(position)

            if position == end:
                path = self.back_trace(prev_tile, end, start)
                return currentScore, path

            # Check all neighbours:
            for n in self.neighbours(position):
                if self.get_tile(n) == '.' and n not in prev_tile:
                    hq.heappush(Queue, (currentScore + 1, n))
                    prev_tile[n] = position

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
                if self.get_tile(n) == '.':
                    if n not in scores or currentScore + 1 < scores[n]:
                        scores[n] = currentScore + 1
                        hq.heappush(Queue, (currentScore + 1, n))

    # Same Dijkstra path-search, but returns the tiles in the shortest path
    def Dijkstra_path(self, start, end):
        Queue = []
        hq.heappush(Queue, (0, start))
        scores = {start: 0}
        prev_tile = {start: None}

        while Queue:
            (currentScore, position) = hq.heappop(Queue)

            if position == end:
                path = self.back_trace(prev_tile, end, start)
                return currentScore, path, scores

            # Check all neighbours:
            for n in self.neighbours(position):
                if self.get_tile(n) == '.':
                    if n not in scores or currentScore + 1 < scores[n]:
                        scores[n] = currentScore + 1
                        hq.heappush(Queue, (currentScore + 1, n))
                        prev_tile[n] = position

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
                if self.get_tile(n) == '.':
                    if n not in distances or distance + 1 < distances[n]:
                        distances[n] = distance + 1
                        hq.heappush(Queue, (distance + 1 + self.distance(n, end), distance + 1, n))

    # Function to find the path
    def back_trace(self, links, position, start):
        path = set()
        while position != start:
            path.add(position)
            position = links[position]

        path.add(start)

        return path

    # Print the tiles, with all locations in marks marked with an X
    # Debugging tool
    def print_Tiles(self, marks=set()):
        oldmarks = {}
        for m in marks:
            oldmarks[m] = self.get_tile(m)
            self.set_tile(m, 'X')

        print(self)

        for m in oldmarks:
            self.set_tile(m, oldmarks[m])

    def __str__(self):
        string = ''

        size = self.get_size()
        for row in [100, 10, 1]:
            string += '\n    '
            for i in range(len(self.tiles[0])):
                string += f'{i//row%10}'
        string += '\n'



        for r, row in enumerate(self.tiles):
            string += f'{r:03d} '
            for char in row:
                string += char
            string += '\n'
        return string
