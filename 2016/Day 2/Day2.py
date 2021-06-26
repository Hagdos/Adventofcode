file = open('Input.txt')

inputs = file.read().split('\n')

# Part 1
location = [1, 1]
numpad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
code = []

for input in inputs:
    for command in input:
        if command == "U" and location[0] > 0:
            location[0] -= 1
        elif command == "D" and location[0] < 2:
            location[0] += 1
        elif command == "L" and location[1] > 0:
            location[1] -= 1
        elif command == "R" and location[1] < 2:
            location[1] += 1

    print(location)
    code.append(numpad[location[0]][location[1]])

print("Answer to part 1:", ''.join(str(x) for x in code))

# Part 2
file = open('Input.txt')
inputs = file.read().split('\n')

location = [0, 0]
numpad = (
          ('0', '0', '1', '0', '0'),
          ('0', '2', '3', '4', '0'),
          ('5', '6', '7', '8', '9'),
          ('0', 'A', 'B', 'C', '0'),
          ('0', '0', 'D', '0', '0'))
code = []

for input in inputs:
    for command in input:
        newlocation = [x for x in location]
        if command == "U":
            newlocation[0] -= 1
        elif command == "D":
            newlocation[0] += 1
        elif command == "L":
            newlocation[1] -= 1
        elif command == "R":
            newlocation[1] += 1
        if sum([abs(x) for x in newlocation]) <= 2:
            location = newlocation
    print(location)
    code.append(numpad[location[0]+2][location[1]+2])

print("Answer to part 2:", ''.join(code))



