file = open('input.txt')

instructions = []

for line in file:
    instructions.append(line.strip().replace(',','').split())
    
pointer = 0

# Part 1
registers = {'a': 0, 'b': 0} 

# Part 2
registers = {'a': 1, 'b': 0} 

while pointer < len(instructions):
    cmd = instructions[pointer]
    
    if cmd[0] == 'hlf':
        registers[cmd[1]] = registers[cmd[1]]//2
        pointer += 1
    elif cmd[0] == 'tpl':
        registers[cmd[1]] = registers[cmd[1]]*3
        pointer +=1
    elif cmd[0] == 'inc':
        registers[cmd[1]] += 1
        pointer += 1
    elif cmd[0] == 'jmp':
        pointer += int(cmd[1])
    elif cmd[0] == 'jie':
        if registers[cmd[1]]%2 == 0:
            pointer += int(cmd[2])
        else:
            pointer += 1
    elif cmd[0] == 'jio':
        if registers[cmd[1]] == 1:
            pointer += int(cmd[2])
        else:
            pointer += 1
        
print(registers['b'])