from operations import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
import json

file = open('2018/Day 16/input.txt').readlines()

funcSet = {addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}
opcodes = [funcSet.copy() for i in range(16)]

ans1 = 0
i = 0
while i < len(file):
    line = file[i].strip().split(': ')
    if line[0] == 'Before':
        registers = json.loads(line[1])
        instr = [int(j) for j in file[i+1].strip().split()]
        result = json.loads(file[i+2].strip().split(': ')[1])

        sum = 0
        for func in funcSet:
            r = registers.copy()
            func(r, instr[1], instr[2], instr[3])
            if r == result:
                sum += 1
            else:
                opcodes[instr[0]].discard(func)

        if sum >= 3:
            ans1 += 1
        i += 4
    else:
        i += 2
        break

print(f'The answer to part 1: {ans1}')

found = set()
while len(found) < 16:
    solved = True
    for j in range(16):
        if type(opcodes[j]) == set:
            if len(opcodes[j]) == 1:
                opcodes[j] = list(opcodes[j])[0]
                found.add(opcodes[j])
            else:
                [opcodes[j].discard(f) for f in found]

# [print(f.__name__) for f in opcodes]

registers = [0, 0, 0, 0]
while i < len(file):
    instr = [int(j) for j in file[i].strip().split()]
    opcodes[instr[0]](registers, instr[1], instr[2], instr[3])
    i += 1

print(f'The answer to part 2: {registers[0]}')
