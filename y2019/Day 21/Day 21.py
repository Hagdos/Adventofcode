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

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)
mem, outputs, counters, finished = ic.runintcode(mem)

disp = printdisplay(outputs)


# C:\Users\Tom Kooyman\Documents\AoC\y2019
# D:\Mijn Documenten\AdventofCode\y2019