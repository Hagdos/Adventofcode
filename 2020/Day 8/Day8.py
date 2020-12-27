import copy

#Read file
f = open("Code.txt")
code = []

for x in f:
    instr = x[0:3]
    arg = x[4:-1]
    if arg[0] == '+':
        arg = arg[1:]
    code.append([instr, int(arg)])
    

# Run code
def runcode(codefunc):

    pc = 0 #Program Counter
    var = 0 #Variable
    i = 0
    lineschecked = set()
    # print(codefunc)
    while i<1000:
        i+=1
        if pc in lineschecked:             #Check if this line has been run before
            print("Code got stuck in loop")        
            print('Lines of code run = ', i)
            print('Accumulator value = ', var)
            print('\n')
            return 0
            break
        elif pc > len(code)-1:                #Or if we're out of the code normally
            print("Code exited normally")
            print('Accumulator value = ', var)
            return 1
            break
        else:                               #Otherwise add pc to the lines of code already visited
            lineschecked.add(pc)
        # Run code
        if codefunc[pc][0] == 'nop':
            pc += 1
            
        elif codefunc[pc][0] =='acc':
            var += codefunc[pc][1]
            pc += 1
            
        elif code[pc][0] == 'jmp':
            pc += codefunc[pc][1]

# runcode(code)     
        
for j in range(len(code)):
    if code[j][0] == 'nop':
        # print('j = ', j)
        codecopy = copy.deepcopy(code)
        codecopy[j][0] = 'jmp'
        if runcode(codecopy):
           
            break
    if code[j][0] == 'jmp':
        codecopy = copy.deepcopy(code)
        codecopy[j][0] = 'nop'
        if runcode(codecopy):
            print('j = ', j)
            break
        

# print(runcode(code))