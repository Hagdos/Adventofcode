file = open('input.txt')

inputs = file.read().split(", ")

# First position is up/down (negative is up)
# Second position is left/right (negative is left)
direction = [-1, 0]
#First is x (up/down), second is y (left/right)
location = [0, 0]
visited = set()
firstDouble = False

for input in inputs:
    if input[0] == 'L':
        direction = [direction[1]*-1, direction[0]]
    elif input[0] == 'R':
        direction = [direction[1], direction[0]*-1]
    else:
        raise ValueError
    distance = int(input[1:])
    for j in range(distance):
        for i in range(2):
            location[i] += direction[i]
        if tuple(location) in visited and firstDouble == False:
            firstDouble = True
            print("Answer to part 2:", abs(location[0]) + abs(location[1]))
        else:
            visited.add(tuple(location))

print("Answer to part 1:", abs(location[0])+abs(location[1]))