# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
def addr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]
# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(registers, A, B, C):
    registers[C] = registers[A] + B

# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(registers, A, B, C):
    registers[C] = registers[A] * registers[B]
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(registers, A, B, C):
    registers[C] = registers[A] * B

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(registers, A, B, C):
    registers[C] = registers[A] & registers[B]
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(registers, A, B, C):
    registers[C] = registers[A] & B

# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(registers, A, B, C):
    registers[C] = registers[A] | registers[B]
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(registers, A, B, C):
    registers[C] = registers[A] | B

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(registers, A, B, C):
    registers[C] = registers[A]
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(registers, A, B, C):
    registers[C] = A

# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(registers, A, B, C):
    if A > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(registers, A, B, C):
    if registers[A] > B:
        registers[C] = 1
    else:
        registers[C] = 0
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(registers, A, B, C):
    if registers[A] > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(registers, A, B, C):
    if A == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(registers, A, B, C):
    if registers[A] == B:
        registers[C] = 1
    else:
        registers[C] = 0
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(registers, A, B, C):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0
