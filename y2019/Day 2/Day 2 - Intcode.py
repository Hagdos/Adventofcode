import sys
if "D:\Mijn Documenten\AdventofCode\y2019" not in sys.path:
    sys.path.append("D:\Mijn Documenten\AdventofCode\y2019")

import intcode as ic


f = open('intcode.txt')
code = f.readline().strip().split(',')


mem = ic.codetomem(code)

mem[1] = 12
mem[2] = 2

ans = ic.runintcode(mem)[0]
print("Answer part 1 =", ans)

# =============================================================================
# Part 2
# =============================================================================
for noun in range(100):
    for verb in range(100):  
        mem = ic.codetomem(code)
        mem[1] = noun
        mem[2] = verb
        
        ans = ic.runintcode(mem)[0]
        if ans == 19690720:
            solution = 100*noun+verb
            print("Answer part 2 =", solution)