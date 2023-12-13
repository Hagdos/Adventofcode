# Row, Column is Real, Complex
def createmap(data):
    shapes = {  '|': (-1, 1),
                '-': (-1j, 1j),
                'L': (-1, 1j),
                'J': (-1, -1j),
                '7': (-1j, 1),
                'F': (1j, 1),
                '.': (),
                'S': ()}

    connections = {}

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            position = complex(r, c)

            neighbours = [position+n for n in shapes[char]]

            if len(neighbours) == 2:
                connections[position] = {neighbours[0]: neighbours[1],
                                         neighbours[1]: neighbours[0]}

            elif char == 'S':
                start = position

    return connections, start

def nextstep(position, nextposition):
    nextstep = connections[nextposition][position]
    return nextstep

def runcircle(start, nextposition):
    position = start
    route = [position]
    lefts = set()
    rights = set()
    while nextposition != start:
        nextposition, position = nextstep(position, nextposition), nextposition
        direction = nextposition - position

        left = direction*1j
        right = direction*-1j

        lefts.add(position+left)
        lefts.add(nextposition+left)

        rights.add(position+right)
        rights.add(nextposition+right)

        route.append(position)


    rights = set((r for r in rights if r not in route))
    lefts = set((l for l in lefts if l not in route))

    return route, lefts, rights

def drawmap(route, marked, size=140):
    counter = 0
    for r in range(size):
        row = []
        for c in range(size):
            if complex(r,c) in route:
                row.append(data[r][c])
            elif complex(r,c) in marked:
                row.append('█')
            else:
                row.append(' ')
        print(''.join(row))

def findconnected(start, route, size=140):
    stack = list(start)
    found = set(start)
    while stack:
        point = stack.pop()
        # for direction in [-1, 1, -1j, 1j, -1-1j, 1-1j, -1+1j, 1+1j]:
        for direction in [-1, 1, -1j, 1j]:
            n = point+direction
            if 0 <= n.real < size:
                if 0 <= n.imag < size:
                    if n not in route and n not in found:
                        found.add(n)
                        stack.append(n)
    return found


file = open('input.txt').readlines()

data = [x.strip() for x in file]

connections, start = createmap(data)

for direction in [-1, 1, -1j, 1j]:
    if start in connections[start+direction].keys():
        nextposition = start+direction
        route, lefts, rights = runcircle(start, nextposition)
        break

size = len(data[0])

rights = findconnected(rights, route, size=size)

drawmap(route, rights, size=size)

marks = []
print('The answer to part 1: ', len(route)//2)
print('The answer to part 2: ', len(rights))

# 705 is too high
# 698 is too high
# 302 is too low