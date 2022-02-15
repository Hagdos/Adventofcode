class Cart:
    def __init__(self, r, c, direction):
        self.location = (r, c)
        self.direction = direction
        self.counter = 0

    def move(self, tracks, carts):
        nextlocation = tuple([i+j for i,j in zip(self.location, self.direction)])

        for c in carts:
            if nextlocation == c.location:
                print(f'Crash at location: {nextlocation[1],nextlocation[0]}')
                return self, c

        self.location = nextlocation

        if tracks[self.location] == '+':
            self.turn()
        elif tracks[self.location] == '/':
            self.direction.reverse()
            self.direction = [-i for i in self.direction]
        elif tracks[self.location] == '\\':
            self.direction.reverse()

        return None

    def turn(self):
        if self.counter == 0:
            self.turnleft()
        elif self.counter == 1:
            pass
        elif self.counter == 2:
            self.turnright()
        self.counter += 1
        self.counter %= 3

        return None

    def turnleft(self):
        di = complex(self.direction[0], self.direction[1])
        di *= 1j
        self.direction = [int(di.real), int(di.imag)]
        return

    def turnright(self):
        di = complex(self.direction[0], self.direction[1])
        di *= -1j
        self.direction = [int(di.real), int(di.imag)]
        return

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        return self.location == other.location
    def __gt__(self, other):
        return self.location > other.location

# Create input data
data = open('input.txt').readlines()

tracks = dict()
carts = []

# Create look-up table for track elements
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == '>':
            carts.append(Cart(r, c, [0, 1]))
            tracks[(r,c)] = '-'
        elif char == '<':
            carts.append(Cart(r, c, [0, -1]))
            tracks[(r,c)] = '-'
        elif char == 'v':
            carts.append(Cart(r, c, [1, 0]))
            tracks[(r,c)] = '|'
        elif char == '^':
            carts.append(Cart(r, c, [-1, 0]))
            tracks[(r,c)] = '|'
        elif char in ['-', '|', '+', '/', '\\']:
            tracks[(r,c)] = char

# Run all carts until there's only one left
while len(carts) > 1:
    carts.sort()
    crashed = []
    for cart in carts:
        crash = cart.move(tracks, carts)
        if crash:
            for c in crash:
                crashed.append(c)

    for c in crashed:
        if c in carts:
            carts.remove(c)

print(f'The answer to part 2: {carts[0].location[1],carts[0].location[0]}')