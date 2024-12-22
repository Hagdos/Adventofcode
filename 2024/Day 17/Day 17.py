def combo(operand, reg):
    if operand//4:
        return reg[operand % 4]
    return operand


def runProgram(Astart=None):
    reg = [int(i) for i in file[0].split()[2::3]]
    program = [int(i) for i in file[1].split()[1].split(',')]

    if Astart is not None:
        reg[A] = Astart

    ip = 0
    output = []

    while ip < len(program):

        instruction, operand = program[ip], program[ip+1]

        if instruction == 0:
            num = reg[A]
            denom = 2**combo(operand, reg)
            reg[A] = num // denom
        elif instruction == 1:
            reg[B] = reg[B] ^ operand
        elif instruction == 2:
            reg[B] = combo(operand, reg) % 8
        elif instruction == 3:
            if reg[A]:
                ip = operand
                continue
        elif instruction == 4:
            reg[B] = reg[B] ^ reg[C]
        elif instruction == 5:
            output.append(combo(operand, reg) % 8)
        elif instruction == 6:
            num = reg[A]
            denom = 2**combo(operand, reg)
            reg[B] = num // denom
        elif instruction == 7:
            num = reg[A]
            denom = 2**combo(operand, reg)
            reg[C] = num // denom

        ip += 2

    return output


file = open('input2.txt').read()
file = file.split('\n\n')

A = 0
B = 1
C = 2

ans1 = ans2 = 0

print(file[1])
goalprogram = [int(i) for i in file[1].split()[1].split(',')]

options = [0]

for n, goal in enumerate(goalprogram[::-1]):
    nextoptions = []
    for option in options:
        option *= 8

        for Astart in range(8):
            if runProgram(option + Astart)[0] == goal:
                nextoptions.append(option + Astart)

    options = nextoptions


print('The answer to part 1: ', ','.join([str(s) for s in runProgram()]))
print('The answer to part 2: ', min(options))

"""
Register A: 32916674
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0

Program:
    2,4, B = A%8
    1,1, B = B XOR 1  > Flip the LSB
    7,5, C = A // 2^B  -> C = A // ((A%8) XOR 1) -> A divided by the last three bits of A, but the LSB flipped
    0,3, A = A // 2^3
    1,4, B = B XOR 4 (0b100)  -> Flip the third bit
    4,0, B = B XOR C
    5,5, Output B%8
    3,0  End if A ==0, else jump to 0

Output is last three bits of (B XOR C)
B = Last three bits of A XOR 001 XOR 100
C = A divided by the last three bits of A, but the LSB flipped

A loses it's last three bits every time.
Last time around:
    C = A/(A XOR 1) = A%2 (Last bit)
    Last bit = A XOR !A = 1, no matter what A is...

"""