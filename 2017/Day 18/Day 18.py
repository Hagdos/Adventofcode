# Returns values from the registers given in the instructions
def decode(instruction, registers):
    cmd = instruction[0]
    reg1 = instruction[1]
    try:
        value1 = int(instruction[1])
    except ValueError:
        value1 = registers[instruction[1]]
    try:
        value2 = int(instruction[2])
    except ValueError:
        value2 = registers[instruction[2]]
    except IndexError:
        value2 = None
    return cmd, value1, value2, reg1


# Executes a single command
def exec1(instructions, registers, pointer):
    cmd, val1, val2, reg1 = decode(instructions[pointer], registers)
    if cmd == 'snd':
        registers['sound'] = val1
    elif cmd == 'set':
        registers[reg1] = val2
    elif cmd == 'add':
        registers[reg1] += val2
    elif cmd == 'mul':
        registers[reg1] *= val2
    elif cmd == 'mod':
        registers[reg1] %= val2
    elif cmd == 'rcv':
        return None, registers['sound']
    elif cmd == 'jgz':
        if val1 > 0:
            pointer += val2 - 1
    pointer += 1
    return pointer, 0


def exec2(instructions, registers, pointer, ownqueue, otherqueue):
    waiting = False
    cmd, val1, val2, reg1 = decode(instructions[pointer], registers)
    if cmd == 'snd':
        ownqueue.append(val1)
        registers['Counter'] += 1
    elif cmd == 'set':
        registers[reg1] = val2
    elif cmd == 'add':
        registers[reg1] += val2
    elif cmd == 'mul':
        registers[reg1] *= val2
    elif cmd == 'mod':
        registers[reg1] %= val2
    elif cmd == 'rcv':
        try:
            registers[reg1] = otherqueue.pop()
        except IndexError:
            pointer -= 1
            waiting = True
    elif cmd == 'jgz':
        if val1 > 0:
            pointer += val2 - 1
    pointer += 1
    return pointer, waiting


file = open('Day 18/input.txt').readlines()
instructions = [x.strip().split() for x in file]
pt2 = True

# Create list of registernames (letters)
registernames = set()
for line in instructions:
    if line[1].isalpha():
        registernames.add(line[1])

# Fill the register with zeroes
registers0 = {"Counter": 0}
registers1 = {"Counter": 0}
for name in registernames:
    registers0[name] = 0
    registers1[name] = 0
registers1['p'] = 1

# Command pointer
pointer0 = 0
pointer1 = 0

queue0 = []
queue1 = []

if not pt2:
    for _ in range(1000000):
        pointer0, ans1 = exec1(instructions, registers0, pointer0)
        if ans1 != 0:
            print('The answer to part 1: ', ans1)
            break
else:
    for _ in range(100000000):
        pointer0, waiting0 = exec2(instructions, registers0, pointer0, queue0, queue1)
        pointer1, waiting1 = exec2(instructions, registers1, pointer1, queue1, queue0)
        if waiting0 and waiting1:
            break

print(registers0, registers1)
print(queue0, queue1)
print('The answer to part 2: ', registers1['Counter'])

# 111181 is too high
