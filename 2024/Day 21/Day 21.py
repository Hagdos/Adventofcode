import heapq as hq


class Dirpad:
    def __init__(self):
        self.key_locations = {'^': (0, 1),
                              '<': (1, 0),
                              'v': (1, 1),
                              '>': (1, 2),
                              'A': (0, 2)}
        self.keys = {v: k for k, v in self.key_locations.items()}
        self.directions = {(-1, 0): '^',
                           (1, 0): 'v',
                           (0, -1): '<',
                           (0, 1): '>'}

        self.cost_cache = {}

        self.dirpad = self

    def neighbours(self, pos):
        for d in self.directions.keys():
            step = self.step(pos, d)
            if step in self.keys:
                yield step, self.directions[d]

    def step(self, location, direction):
        return (location[0] + direction[0], location[1] + direction[1])

    # Function to find the path
    def back_trace(self, links, position, start):
        paths = []

        if position == start:
            return ['']

        for newposition, button in links[position]:
            for newpath in self.back_trace(links, newposition, start):
                paths.append(newpath+button)

        return paths

    # I'm only interested in shortest paths from A to a button and back
    # BFS
    def shortest_paths(self, button1, button2):

        start = self.key_locations[button1]
        Queue = []
        hq.heappush(Queue, (0, start))  # Score, position
        scores = {start: 0}
        prev_tile = {start: []}

        while Queue:
            (current_score, position) = hq.heappop(Queue)

            if self.keys[position] == button2:
                paths = self.back_trace(prev_tile, position, start)

                return [p+'A' for p in paths]

            # Check all neighbours:
            for neighbour, button in self.neighbours(position):
                if neighbour not in scores or current_score + 1 < scores[neighbour]:
                    scores[neighbour] = current_score + 1
                    hq.heappush(Queue, (current_score + 1, neighbour))
                    prev_tile[neighbour] = [(position, button)]
                elif current_score + 1 == scores[neighbour]:
                    prev_tile[neighbour].append((position, button))

    def calc_cost(self, button1, button2, levels):
        assert levels >= 0
        key = (button1, button2, levels)
        if key in self.cost_cache:
            return self.cost_cache[key]

        if levels == 0:
            self.cost_cache[key] = len(self.shortest_paths(button1, button2)[0])
            return self.cost_cache[key]

        options = self.shortest_paths(button1, button2)
        bestcost = 2**60
        for option in options:
            cost = 0
            button1 = 'A'
            for button2 in option:
                cost += self.dirpad.calc_cost(button1, button2, levels-1)
                button1 = button2
            if cost < bestcost:
                bestcost = cost

        assert bestcost != 2**60

        self.cost_cache[key] = bestcost
        return self.cost_cache[key]


class Keypad(Dirpad):
    def __init__(self):
        super().__init__()
        self.key_locations = {'7': (0, 0),
                              '8': (0, 1),
                              '9': (0, 2),
                              '4': (1, 0),
                              '5': (1, 1),
                              '6': (1, 2),
                              '1': (2, 0),
                              '2': (2, 1),
                              '3': (2, 2),
                              '0': (3, 1),
                              'A': (3, 2)}
        self.keys = {v: k for k, v in self.key_locations.items()}
        self.dirpad = Dirpad()


file = open('input.txt').readlines()

passwords = [x.strip() for x in file]
ans1 = ans2 = 0

keypad = Keypad()

for password in passwords:
    numeric = int(password[:-1])
    sequencelength = 0
    sequencelength2 = 0

    button1 = 'A'
    for button2 in password:
        sequencelength += keypad.calc_cost(button1, button2, 2)
        sequencelength2 += keypad.calc_cost(button1, button2, 25)
        button1 = button2
    ans1 += sequencelength * numeric
    ans2 += sequencelength2 * numeric


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
