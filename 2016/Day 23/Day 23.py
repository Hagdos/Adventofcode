file = open('input.txt').readlines()

program = [line.strip().split() for line in file]

pointer = 0
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
# Part 2:
registers = {"a": 12, "b": 0, "c": 0, "d": 0}

while pointer < len(program):
    cmd = program[pointer]
    
    print(pointer, cmd, registers)
    
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
            if cmd[2] in registers.keys():
                pointer += registers[cmd[2]]
            else:   
                pointer += int(cmd[2])
        else:
            pointer += 1
    elif cmd[0] == 'tgl':
        togglepointer = pointer+registers[cmd[1]]
        if togglepointer < len(program):
            changecommand = program[togglepointer]
            if changecommand[0] == 'inc':
                changecommand[0] = 'dec'
            elif changecommand[0] in ['inc', 'tgl']:
                changecommand[0] = 'inc'
            elif changecommand[0] == 'jnz':
                changecommand[0] = 'cpy'
            elif changecommand[0] == 'cpy':
                changecommand[0] = 'jnz'
                
            # print(changecommand)
        pointer += 1
    else:
        print("Something went wrong")
        print(cmd)
        break

print('The answer to part 1:', registers['a'])
# print(registers)
