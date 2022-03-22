from operations import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr

file = open('2018/Day 21/input.txt')
ipreg = int(file.readline().split()[1])


instructions = []
for line in file:
    instr = line.strip().split()
    instr[1:] = [int(i) for i in instr[1:]]
    instructions.append(instr)


a = 5169186
nInstructions = 10000
reg4 = []
last = 0
instrCount = 0
registers = [a, 0, 0, 0, 0, 0]
for _ in range(nInstructions):
    instrCount += 1
    instr = instructions[registers[ipreg]]
    locals()[instr[0]](registers, instr[1], instr[2], instr[3])
    if registers[ipreg] == 28:
        reg4.append(registers[4])
        # print(registers[ipreg], instr, registers)
    registers[ipreg] += 1

    if registers[ipreg] >= len(instructions):
        if instrCount < minCount:
            ans1 = a
            minCount = instrCount

        print(instrCount, a, ans1)
        break


reg2 = 0
reg4 = 0
options = []
noRepeat = True
while noRepeat:
    # LOOP4:
    reg5 = reg4 | 65536
    reg4 = 10704114

    # LOOP2:
    while True:
        reg2 = reg5 % 2**8
        reg4 += reg2
        reg4 %= 2**24
        reg4 *= 65899
        reg4 %= 2**24

        if reg5 < 256:  # LOOP3
            if reg4 in options:
                print(f'The answer to part 2: {options[-1]}')
                noRepeat = False
            options.append(reg4)
            break

        reg2 = 0
        # LOOP1:
        reg2 = reg5//256
        reg5 = reg2


# 1670686
# 12111537 is too high
