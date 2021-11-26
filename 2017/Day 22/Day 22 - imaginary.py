def runburst1(n, direction, ans1):

    if n not in infected or infected[n] == 0:   # Not infected (or not yet found; which is not infected too)
        direction *= 1j         # Turn left
        ans1 += 1               # If not infected; add one to answer
        infected[n] = 2
    elif infected[n] == 2:                      # If infected
        direction *= -1j        # Turn right
        infected[n] = 0

    n = stepforward(n, direction)
    
    return n, direction, ans1
    

def runburst2(n, direction, ans):
    if n not in infected or infected[n] == 0:   # Not infected (or not yet found; which is not infected too)
        infected[n] = 0                         # Newly found are made 0
        direction *= 1j         # Turn left
    elif infected[n] == 1:
        ans += 1               # When turning infected; add one to answer
    elif infected[n] == 2:                      # If infected
        direction *= -1j        # Turn right
    elif infected[n] == 3:
        direction *= -1       # Reverse direction
        
    infected[n] = (infected[n] + 1) % 4

    n += direction
    
    return n, direction, ans


def stepforward(node, direction):
        # One step forward
    node += direction
        
    return node


def readinput(inputfile):
    file = open(inputfile).readlines()
    data = [x.strip() for x in file]
    
    infected = dict()
    
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                infected[complex(i,j)] = 2
            else:
                infected[complex(i,j)] = 0
                
    
    node = complex(len(data)//2, len(data)//2)
    
    return infected, node

# Part 1
infected, node = readinput('input.txt')

direction = -1 + 0j

ans1 = 0

for burst in range(10000):
    node, direction, ans1 = runburst1(node, direction, ans1)

print('The answer to part 1: ', ans1)


# Part 2
infected, node = readinput('input.txt')
direction = -1 + 0j
ans2 = 0

for burst in range(10000000):
    node, direction, ans2 = runburst2(node, direction, ans2)

print('The answer to part 2: ', ans2)

