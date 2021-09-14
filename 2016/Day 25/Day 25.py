# Check if the argument given with an instruction is a registar value or an
# integer, and return the correct value
def readArgument(value):
    if value in registers.keys():
        return registers[value]
    else:
        return int(value)


file = open('input.txt').readlines()
program = [line.strip().split() for line in file]

improvements = True
finished = False
a = 0

while finished is False and a < 1000:
    counter = 0
    pointer = 0
    pointercounter = [0] * 30
    outputarray = [-1]
    a += 1
    registers = {"a": a, "b": 0, "c": 0, "d": 0}
    while pointer < len(program) and counter < 1e6:
        counter += 1

        if improvements is True:
            # Speed improvement; replace the multiply part of the assembly code
            # by custom multiplier.
            if pointer == 3:
                registers["d"] += registers["b"] * registers["c"]
                registers["b"] = 0
                registers["c"] = 0
                pointer += 5

            # Speed improvement 2;
            if pointer == 12:
                registers["a"] += registers["b"] // 2
                registers["c"] = 2 - registers["b"] % 2
                registers["b"] = 0
                pointer += 8

            # Speed improvement 3;
            if pointer == 21:
                registers["b"] -= registers["c"]
                registers["c"] = 0
                pointer += 5

        # Analys of pointers
        # pointercounter[pointer] += 1

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
        elif cmd[0] == 'out':
            outputarray.append(readArgument(cmd[1]))
            if outputarray[-1] == outputarray[-2]:
                # print(outputarray)
                break
            if len(outputarray) >= 500:
                print(outputarray)
                finished = True
                break
            pointer += 1
        else:
            print("Something went wrong")
            print(cmd)
            break

print(registers)
print('Counter:', counter)
print('output:', outputarray)
print('Starta:', a)
#
# for number, count in enumerate(pointercounter):
#     print(number+1, count)
