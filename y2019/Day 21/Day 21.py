from sys import path
if "C:\\Users\Tom Kooyman\Documents\AoC\y2019" not in path:
    path.append("C:\\Users\Tom Kooyman\Documents\AoC\y2019")
import intcode as ic

def printdisplay(outputs):    
    disp = [[[]]]
    n = 0
    line = 0
    for i, o in enumerate(outputs):
        if o == 10:
            print(''.join(disp[n][line]))
            disp[n].append([])
            line+=1
            if outputs[i-1] == 10:
                disp.append([[]])
                n+=1
                line = 0
        else:
            disp[n][line].append(chr(o))
    print(''.join(disp[n][line]))
    return disp

inputs = []
springcode = open('springscript.txt')
springcode = open('springscript2.txt')

for line in springcode:
    for c in line:
        inputs.append(ord(c))
        

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)
mem, outputs, counters, finished = ic.runintcode(mem, inputs)

disp = printdisplay(outputs)
print(outputs)



# =============================================================================
# Reasoning for springscript
# =============================================================================

# Jump if there's a hole at A, B or C, but not D'

# Available: AND, OR and NOT; one temp register and the Jump register.
# Jumps if J is true
# ABCD is true if there's ground'
# T and J start as false

# if D and (not A or not B or not C)
# if D and not (A and B and C)

#not (A and B and C)
# NOT T T
# AND A T
# AND B T
# AND C T
# NOT T J

# AND D J