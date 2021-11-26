def printmap(infected, node):
    for i, line in enumerate(infected):
        printline = []
        for char in line:
            printline.append('#' if char else '.')
        
        if i == node[0]:
            printline[node[1]] = '0'
        
        print(''.join(printline))
    print()

file = open('input.txt').readlines()
data = [x.strip() for x in file]

infected = [[i=='#' for i in line] for line in data ]


# Increase size of infected; to allow it wandering out of bounds
add = 1000
for i in range(len(infected)):
    infected[i] = [False]*add + infected[i] + [False]*add
infected = [[False]*len(infected[0])for _ in range(add)] + infected + [[False]*len(infected[0])for _ in range(add)]


node = [len(infected)//2, len(infected)//2]
directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # Up, left, down and right)
direction = 0

ans1 = ans2 = 0


for burst in range(10000):
    # print('Burst:', burst)
    # printmap(infected, node)
    
    if infected[node[0]][node[1]]:  # If infected; turn right
        direction = (direction - 1) % 4
    else:                       # If not, turn left
        direction = (direction + 1) % 4
        ans1 += 1               # If not infected; add one to anser
    # Reverse infection
    infected[node[0]][node[1]] = not(infected[node[0]][node[1]])
    # One step forward
    for i in range(2):
        node[i] += directions[direction][i]


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

# 5000 is too low
# 5514 is too high