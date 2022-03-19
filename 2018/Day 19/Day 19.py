from operations import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr

file = open('2018/Day 19/input.txt')
ipreg = int(file.readline().split()[1])
registers = [0, 0, 0, 0, 0, 0]

instructions = []
for line in file:
    instr = line.strip().split()
    instr[1:] = [int(i) for i in instr[1:]]
    instructions.append(instr)

while True:
    instr = instructions[registers[ipreg]]
    locals()[instr[0]](registers, instr[1], instr[2], instr[3])
    registers[ipreg] += 1

    if registers[ipreg] >= len(instructions):
        print(f'The answer to part 1: {registers[0]}')
        break

pt1 = 864
pt2 = 10551264
ans1 = ans2 = 0
for i in range(1, pt2+1):
    if pt1 % i == 0:
        ans1 += i
    if pt2 % i == 0:
        ans2 += i

print(f'The answer to part 1: {ans1}')
print(f'The answer to part 2: {ans2}')

# 5275632 is too low
# 10551264
