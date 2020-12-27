f = open('intcode.txt')

code = f.readline().strip().split(',')
# code = [1,1,1,4,99,5,6,0,99]
# =============================================================================
# Put code into memory
# =============================================================================
def codetomem(code):
    mem = {}
    for i, c in enumerate(code):
        mem[i] = int(c)
    return mem

# =============================================================================
# Puzzle instructions
# =============================================================================


# =============================================================================
# Process code
# =============================================================================
def runintcode(mem):
    ip = 0
    while True:
        instr = mem[ip]
        if instr == 1:
            mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
        elif instr == 2:
            mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
        elif instr == 99:
            break
        ip+=4
    return mem

# =============================================================================
# Part 1
# =============================================================================
mem = codetomem(code)

mem[1] = 12
mem[2] = 2

ans = runintcode(mem)[0]
print("Answer part 1 =", ans)

# =============================================================================
# Part 2
# =============================================================================
for noun in range(100):
    for verb in range(100):  
        mem = codetomem(code)
        mem[1] = noun
        mem[2] = verb
        
        ans = runintcode(mem)[0]
        if ans == 19690720:
            solution = 100*noun+verb
            print("Answer part 2 =", solution)