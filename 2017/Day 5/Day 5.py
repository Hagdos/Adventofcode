file = open('input.txt').readlines()

pointer = 0
steps = 0
instructions = [int(x) for x in file]

while pointer < len(instructions):
    instructions[pointer] += 1
    pointer += instructions[pointer]-1
    steps += 1

print("The answer to part 1:", steps)

# # Part 2

pointer = 0
steps = 0
instructions = [int(x) for x in file]

while pointer < len(instructions):
    if instructions[pointer] >= 3:
        instructions[pointer] -= 1
        pointer += instructions[pointer]+1
    else:
        instructions[pointer] += 1
        pointer += instructions[pointer]-1
    steps += 1


print("The answer to part 2:", steps)

# 41926707 is too high
