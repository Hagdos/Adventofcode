def runburst1(node, direction, directions, ans1):
    n = tuple(node)

    if n not in infected or infected[n] == 0:   # Not infected (or not yet found; which is not infected too)
        direction = (direction + 1) % 4         # Turn left
        ans1 += 1               # If not infected; add one to answer
        infected[n] = 2
    elif infected[n] == 2:                      # If infected
        direction = (direction - 1) % 4        # Turn right
        infected[n] = 0

    node = stepforward(node, direction, directions)
    
    return node, direction, ans1
    

def runburst2(node, direction, directions, ans):
    n = tuple(node)

    if n not in infected or infected[n] == 0:   # Not infected (or not yet found; which is not infected too)
        infected[n] = 0                         # Newly found are made 0
        direction = (direction + 1) % 4         # Turn left
    elif infected[n] == 1:
        ans += 1               # When turning infected; add one to answer
    elif infected[n] == 2:                      # If infected
        direction = (direction - 1) % 4        # Turn right
    elif infected[n] == 3:
        direction = (direction + 2) % 4        # Reverse direction
        
    infected[n] = (infected[n] + 1) % 4

    node = stepforward(node, direction, directions)
    
    return node, direction, ans


def stepforward(node, direction, directions):
        # One step forward
    for i, step in enumerate(directions[direction]):
        node[i] += step
        
    return node


def readinput(inputfile):
    file = open(inputfile).readlines()
    data = [x.strip() for x in file]
    
    infected = dict()
    
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                infected[(i,j)] = 2
            else:
                infected[(i,j)] = 0
                
    
    node = [len(data)//2, len(data)//2]
    
    return infected, node

directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # Up, left, down and right)


# Part 1
infected, node = readinput('input.txt')

direction = 0

ans1 = 0

for burst in range(10000):
    node, direction, ans1 = runburst1(node, direction, directions, ans1)

print('The answer to part 1: ', ans1)


# Part 2
infected, node = readinput('input.txt')
direction = 0
ans2 = 0

for burst in range(10000000):
    node, direction, ans2 = runburst2(node, direction, directions, ans2)

print('The answer to part 2: ', ans2)

