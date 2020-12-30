import intcode as ic
import copy
import itertools

f = open('code.txt')
code = f.readline().strip().split(',')

mem = ic.codetomem(code)
mem2 = copy.deepcopy(mem)

permutations = [0, 1, 2, 3, 4]
maxout = 0

for phases in itertools.permutations(permutations):
    output = [0]
    for phase in phases:
        mem2 = copy.deepcopy(mem)
        mem2, output = ic.runintcode(mem2, [phase, output[0]])
        
    
    if output[0] > maxout:
        maxout = output[0]
        
print('Answer to Part 1:', maxout)

# =============================================================================
# Part 2
# =============================================================================
permutations = [5, 6, 7, 8, 9]

for phases in itertools.permutations(permutations):
    inputsA = [phases[0]] + [0]*10
    inputsB = [phases[1]]
    inputsC = [phases[2]]
    inputsD = [phases[3]]
    inputsE = [phases[4]]
    
    for _ in range(11):
        mem2 = copy.deepcopy(mem)
        mem2, outputsA = ic.runintcode(mem2, inputsA)
        inputsB = [phases[1]]+outputsA
        
        mem2 = copy.deepcopy(mem)
        mem2, outputsB = ic.runintcode(mem2, inputsB)
        inputsC = [phases[2]]+outputsB
        
        mem2 = copy.deepcopy(mem)
        mem2, outputsC = ic.runintcode(mem2, inputsC)
        inputsD = [phases[3]]+outputsC
        
        mem2 = copy.deepcopy(mem)
        mem2, outputsD = ic.runintcode(mem2, inputsD)
        inputsE = [phases[4]]+outputsD
        
        mem2 = copy.deepcopy(mem)
        mem2, outputsE = ic.runintcode(mem2, inputsE)
        inputsA = [phases[0], 0]+outputsE
        
        # print(inputsA)
        # print(outputsE)
    output = outputsE[-1]
    if output > maxout:
        maxout = output
        
print('Answer to Part 2:', maxout)

#7320155 is too low


#Hint: It's enough to just calculate the first output and pass it on.