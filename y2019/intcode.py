# =============================================================================
# Put code into memory
# =============================================================================
def codetomem(code):
    mem = {}
    for i, c in enumerate(code):
        mem[i] = int(c)
    return mem

# =============================================================================
# Main intcode loop: Run code
# =============================================================================
def runintcode(mem, inputs):
    ip = 0
    counter = 0
    inputcounter = 0
    relbase = 0
    outputs = []
    while True:
        counter += 1
        if counter >= 1000000:
            print("Program ran for", counter, "cycles")
            break
        # print('IP = ', ip)
        instr = mem[ip]%100         #First two characters are opcode 
        mode = mem[ip]//100         #Floor division; remove first two characters
        # print(instr,mode)
        # print()
        
# =============================================================================
#         Instructions switchcase
# =============================================================================
        if instr == 1:
            mem, ip = add(mem, ip, mode, relbase)
        elif instr == 2:
            mem, ip = multiply(mem, ip, mode, relbase)
        elif instr == 3:
            try:
                value = inputs[inputcounter]
            except:
                print("Too few inputs provided, at least", inputcounter+1, "inputs needed")
                break
            inputcounter += 1
            mem, ip = inp(mem, ip, mode, value, relbase)
        elif instr == 4:
            mem, ip, output = outp(mem, ip, mode, relbase)
            outputs.append(output)
        elif instr == 5:
            mem, ip = jmpiftrue(mem, ip, mode, relbase)
        elif instr == 6:
            mem, ip = jmpiffalse(mem, ip, mode, relbase)
        elif instr == 7:
            mem, ip = lessthan(mem, ip, mode, relbase)
        elif instr == 8:
            mem, ip = equals(mem, ip, mode, relbase)
        elif instr == 9:
            mem, ip, relbase = adjbase(mem,ip, mode, relbase)
        elif instr == 99:
            break
        
    return mem, outputs

# =============================================================================
# Instructions
# =============================================================================

#Instruction 1, add
def add(mem, ip, mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    write(mem, ip+3, mode//100, relbase, a+b)
    ip+= 4
    return mem, ip

#Instruction 2, multiply
def multiply(mem, ip, mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    write(mem, ip+3, mode//100, relbase, a*b)
    ip+= 4
    return mem, ip

#Instruction 3, input
def inp(mem, ip, mode, value, relbase):
    # mem[mem[ip+1]] = int(input("Please provide input: "))
    write(mem, ip+1, mode//1, relbase, value)
    ip += 2
    return mem, ip
    
#Instruction 4, output
def outp(mem, ip, mode, relbase):
    a = read1var(mem, ip, mode, relbase)
    # print('Output: ', a)
    ip += 2
    return mem, ip, a

#Instruction 5, Jump if first parameter is non-zero
def jmpiftrue(mem,ip,mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    if a != 0:
        ip = b
    else:
        ip += 3
    return mem, ip

#Instruction 6, Jump if first parameter is zero    
def jmpiffalse(mem,ip,mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    if a == 0:
        ip = b
    else:
        ip += 3
    return mem, ip

#Instruction 7, Less than. Put 1 in position 3 if pos 2 < pos 1. Otherwise put a 0
def lessthan(mem, ip, mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    if a < b:
        write(mem, ip+3, mode//100, relbase, 1)
    else:
        write(mem, ip+3, mode//100, relbase, 0)
    ip += 4
    return mem,ip
#Instructon 8, Equal. Put 1 in position 3 if pos 2 == pos 1. Otherwise put a 0
def equals(mem,ip,mode, relbase):
    a, b = read2var(mem, ip, mode, relbase)
    if a == b:
        write(mem, ip+3, mode//100, relbase, 1)
    else:
        write(mem, ip+3, mode//100, relbase, 0)
    ip += 4
    return mem,ip
#Instruction 9, change the relative base
def adjbase(mem,ip, mode, relbase):
    a = read1var(mem,ip,mode,relbase)
    relbase += a
    ip += 2
    return mem, ip, relbase

# =============================================================================
# Read variables depending on mode
# =============================================================================
    
def read1var(mem, ip, mode, relbase):
    if mode == 1:
        return value(mem,ip+1)
    elif mode == 2:
        return value(mem, relbase + value(mem,ip+1))
    else:
        return value(mem, value(mem,ip+1))
    
def read2var(mem, ip, mode, relbase):
    # print(ip, mode)
    # print(ip+1)
    # print(mem[ip+1])
    if mode%10 == 1:
        a = value(mem,ip+1)
    elif mode%10 == 2:
        a = value(mem, relbase + value(mem,ip+1))
    else:
        a = value(mem, value(mem,ip+1))
        
    if (mode//10)%10 == 1:
        b =  value(mem,ip+2)
    elif (mode//10)%10 == 2:
        b = value(mem, relbase + value(mem,ip+2))
    else:
        b = value(mem, value(mem,ip+2))
    return a,b

def write(mem, ip, mode, relbase, value):
    if mode == 0:
        mem[mem[ip]] = value
    elif mode == 2:
        mem[relbase+mem[ip]] = value

def value(mem, address):
    try:
        a = mem[address]
    except:
        a = 0
    return a

if __name__ == "__main__":
    print("Use F6, you idiot")
    # testmem = codetomem('104,1125899906842624,99'.split(','))
    # testmem, outputs = runintcode(testmem, [1])

    # print(outputs)
