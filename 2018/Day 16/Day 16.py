from operations import addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr

file = open('2018/Day 16/input.txt').readlines()

for line in file:


funcSet = {addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}

registers = [1, 2, 3, 4]
addr(registers, 1, 2, 3)

print(registers)

funcDict = {i: funcSet.copy() for i in range(10)}
a = 8

funcDict[3].remove(addr)

for b in funcDict:
    print(funcDict[b])
