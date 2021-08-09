# Check if the argument given with an instruction is a registar value or an
# integer, and return the correct value
def readArgument(value):
    if value in registers.keys():
        return registers[value]
    else:
        return int(value)

file = open('input.txt').readlines()

program = [line.strip().split() for line in file]

pointer = 0
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
# Part 2:
registers = {"a": 12, "b": 0, "c": 0, "d": 0}

while pointer < len(program):
    
    #Speed improvement; replace the multiply part of the assembly code by
    #a custom multiplier.
    if pointer == 5:
        registers["a"] += registers["c"] * registers["d"]
        registers["c"] = 0
        registers["d"] = 0
        pointer += 5
        
    cmd = program[pointer]

    if cmd[0] == 'cpy':
        registers[cmd[2]] = readArgument(cmd[1])
        pointer += 1
    elif cmd[0] == 'inc':
        registers[cmd[1]] += 1
        pointer += 1
    elif cmd[0] == 'dec':
        registers[cmd[1]] -= 1
        pointer += 1
    elif cmd[0] == 'jnz':
        if readArgument(cmd[1]) != 0:
            pointer += readArgument(cmd[2])
        else:
            pointer += 1
    elif cmd[0] == 'tgl':
        togglepointer = pointer+registers[cmd[1]]
        if togglepointer < len(program):
            changecommand = program[togglepointer]
            if changecommand[0] == 'inc':
                changecommand[0] = 'dec'
            elif changecommand[0] in ['dec', 'tgl']:
                changecommand[0] = 'inc'
            elif changecommand[0] == 'jnz':
                changecommand[0] = 'cpy'
            elif changecommand[0] == 'cpy':
                changecommand[0] = 'jnz'
        pointer += 1
    else:
        print("Something went wrong")
        print(cmd)
        break

print('The answer to part 1:', registers['a'])