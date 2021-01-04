import intcode as ic
import time

f = open('code.txt')
code = f.readline().strip().split(',')


mem = ic.codetomem(code)
counters = [0, 0, 0, 0]
finished = False
inputs = []

# while not finished:
#     mem, outputs, counters, finished = ic.runintcode(mem, inputs, counters)

# cmds = []
# for i in range(0, len(outputs), 3):
#     cmds.append(outputs[i:i+3])
    
# blocks = {}
# ans = 0
# for c in cmds:
#     blocks[(c[0],c[1])] = c[2]
#     if c[-1] == 2:
#         ans += 1
                       
# print("Answer part 1:", ans)

# =============================================================================
# Part 2 
# =============================================================================

def printgame(outputs, display):
    blocks = {}
    for i in range(0, len(outputs), 3):
        if outputs[i+2] == 3:
            paddleloc = outputs[i]
        elif outputs[i+2] == 4:
            balloc = outputs[i]
        if display:
            blocks[(outputs[i],outputs[i+1])] = outputs[i+2]

    score = 0
    if display:
        screen = []
        for _ in range(20):
            screen.append([9]*37)
        for i in blocks:
            if i == (-1,0):
                score = blocks[i]
            elif blocks[i] == 0:                  #Empty tile
                screen[i[1]][i[0]] = ' '
            elif blocks[i] == 1:                #Wall tile
                screen[i[1]][i[0]] = '|'
            elif blocks[i] == 2:                #Block tile
                screen[i[1]][i[0]] = 'X'
            elif blocks[i] == 3:                #Horizontal Paddle
                screen[i[1]][i[0]] = '='
                paddleloc = i[0]
            elif blocks[i] == 4:                #Ball
                screen[i[1]][i[0]] = 'O'
                balloc = i[0]
            else:
                screen[i[1]][i[0]] = 9
            
        for line in screen:
            print(''.join(line))
        print("De score is", score)
    else:
        for i in blocks:
            if i == (-1,0):
                score = blocks[i]
            elif blocks[i] == 3:                #Horizontal Paddle
                paddleloc = i[0]
            elif blocks[i] == 4:                #Ball
                balloc = i[0]
    
    return paddleloc, balloc, score



inputs = [0]
mem[0] = 2

start = time.time()

while not finished:
    mem, outputs, counters, finished = ic.runintcode(mem, inputs, [0,0,0,0])
    paddleloc, balloc, score = printgame(outputs, 1)
    
    if paddleloc>balloc:
        inputs[0] = -1
    elif paddleloc<balloc:
        inputs[0] = 1
    else:
        inputs[0] = 0
    
    while True:
        try:
            userinput = int(input("Input: "))
            if userinput not in [1,2,3,8]:
               print("Wrong value") 
            else:
               break
        except:
            print("Wrong input")
    if userinput == 8:
        break
    inputs[0] = (userinput-2)

    
print(score)
print(time.time()-start)
































