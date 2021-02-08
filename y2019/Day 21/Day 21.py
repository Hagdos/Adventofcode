# from sys import path
# if "C:\\Users\Tom Kooyman\Documents\AoC\y2019" not in path:
#     path.append("C:\\Users\Tom Kooyman\Documents\AoC\y2019")
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
# springcode = open('springscript.txt')
springcode = open('springscript2.txt')

for line in springcode:
    cline = line.split('#')[0].strip()+'\n'     #Strip any comments; add a newline
    
    if cline != '\n':                           #Skip empty lines
        print(cline)
        for c in cline:
            inputs.append(ord(c))
            # print(c)
        

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)
mem, outputs, counters, finished = ic.runintcode(mem, inputs)

try:
    disp = printdisplay(outputs)
except:
    print(outputs[-1])



# =============================================================================
# Reasoning for springscript1
# =============================================================================

# Jump if there's no ground at A, B or C, but ground at D

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

# =============================================================================
# Reasoning for springscript2
# =============================================================================

# Jump if there's a hole at A, B or C, but not D and H

# Available: AND, OR and NOT; one temp register and the Jump register.
# Jumps if J is true
# ABCDEFGHI is true if there's ground
# T and J start as false

# if D and (E OR H) and (not A or not B or not C)
# if D and (E OR H) and not (A and B and C)

# # not (A and B and C)
# NOT J J   #T True
# AND A J   #if A
# AND B J   #if A AND B
# AND C J   #if A AND B AND C
# NOT J J   #if not (A & B & C)

# # E or H
# OR E T
# OR H T

# # AND D and E|H (T) and !(A&B&C) (J)
# AND D J   #if D & not (A&B&C)
# AND T J

# RUN



# A 1
# B 2
# C 3
# D 4
# E 5
# F 6
# G 7
# H 8
# I 9
