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
    outputs = []
    while True:
        counter += 1
        if counter >= 1000:
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
            mem, ip = add(mem, ip, mode)
        elif instr == 2:
            mem, ip = multiply(mem, ip, mode)
        elif instr == 3:
            try:
                value = inputs[inputcounter]
            except:
                print("Too few inputs provided, at least", inputcounter+1, "inputs needed")
                break
            inputcounter += 1
            mem, ip = inp(mem, ip, value)
        elif instr == 4:
            mem, ip, output = outp(mem, ip, mode)
            outputs.append(output)
        elif instr == 5:
            mem, ip = jmpiftrue(mem, ip, mode)
        elif instr == 6:
            mem, ip = jmpiffalse(mem, ip, mode)
        elif instr == 7:
            mem, ip = lessthan(mem, ip, mode)
        elif instr == 8:
            mem, ip = equals(mem, ip, mode)
        elif instr == 99:
            break
        
    return mem, outputs

# =============================================================================
# Instructions
# =============================================================================

#Instruction 1, add
def add(mem, ip, mode):
    a, b = read2var(mem, ip, mode)
    mem[mem[ip+3]] = a + b
    ip+= 4
    return mem, ip

#Instruction 2, multiply
def multiply(mem, ip, mode):
    a, b = read2var(mem, ip, mode)
    mem[mem[ip+3]] = a * b
    ip+= 4
    return mem, ip

#Instruction 3, input
def inp(mem, ip, value):
    # mem[mem[ip+1]] = int(input("Please provide input: "))
    mem[mem[ip+1]] = value
    ip += 2
    return mem, ip
    
#Instruction 4, output
def outp(mem, ip, mode):
    a = read1var(mem, ip, mode)
    # print('Output: ', a)
    ip += 2
    return mem, ip, a

#Instruction 5, Jump if first parameter is non-zero
def jmpiftrue(mem,ip,mode):
    a, b = read2var(mem, ip, mode)
    if a != 0:
        ip = b
    else:
        ip += 3
    return mem, ip

#Instruction 6, Jump if first parameter is zero    
def jmpiffalse(mem,ip,mode):
    a, b = read2var(mem, ip, mode)
    if a == 0:
        ip = b
    else:
        ip += 3
    return mem, ip

#Instruction 7, Less than. Put 1 in position 3 if pos 2 < pos 1. Otherwise put a 0
def lessthan(mem, ip, mode):
    a, b = read2var(mem, ip, mode)
    if a < b:
        mem[mem[ip+3]] = 1
    else:
        mem[mem[ip+3]] = 0
    ip += 4
    return mem,ip

def equals(mem,ip,mode):
    a, b = read2var(mem, ip, mode)
    if a == b:
        mem[mem[ip+3]] = 1
    else:
        mem[mem[ip+3]] = 0
    ip += 4
    return mem,ip

# =============================================================================
# Read variables depending on mode
# =============================================================================
    
def read1var(mem, ip, mode):
    if mode%10:
        return mem[ip+1]
    else:
        return mem[mem[ip+1]]
    
def read2var(mem, ip, mode):
    if mode%10:
        a = mem[ip+1]
    else:
        a = mem[mem[ip+1]]
    if (mode//10)%10:
        b =  mem[ip+2]
    else:
        b = mem[mem[ip+2]]
    return a,b


    
    


if __name__ == "__main__":
    # print("Use F6, you idiot")
    testmem = codetomem('3,3,1108,-1,8,3,4,3,99'.split(','))
    runintcode(testmem, [1])

