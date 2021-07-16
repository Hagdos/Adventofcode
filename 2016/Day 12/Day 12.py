file = open('input.txt')

commands = []

for line in file:
    commands.append(line.strip().split(' '))

pointer = 0
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
# Part 2:
registers = {"a": 0, "b": 0, "c": 1, "d": 0}

while pointer < len(commands):
    cmd = commands[pointer]
    if cmd[0] == 'cpy':
        if cmd[1] in registers.keys():
            value = registers[cmd[1]]
        else:
            value = int(cmd[1])
        registers[cmd[2]] = value
        pointer += 1
    elif cmd[0] == 'inc':
        registers[cmd[1]] += 1
        pointer += 1
    elif cmd[0] == 'dec':
        registers[cmd[1]] -= 1
        pointer += 1
    elif cmd[0] == 'jnz':
        if cmd[1] in registers.keys():
            value = registers[cmd[1]]
        else:
            value = int(cmd[1])
        if value != 0:
            pointer += int(cmd[2])
        else:
            pointer += 1
    else:
        print("Something went wrong")
        print(cmd)
        break

print(registers)
