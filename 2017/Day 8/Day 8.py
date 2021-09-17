file = open('input.txt').readlines()

data = [x.strip().split(' if ') for x in file]
largest2 = 0
reg = dict()

for line in data:
    instr = line[0].split()
    cond = line[1].split()
    
    reg[cond[0]] = reg.get(cond[0], 0)
    
    if eval(str(reg[cond[0]]) + cond[1] + cond[2]):
        reg[instr[0]] = reg.get(instr[0], 0)
        if instr[1] == 'inc':
            reg[instr[0]] += int(instr[2])
        elif instr[1] == 'dec':
            reg[instr[0]] -= int(instr[2])
            
    for key in reg.keys():
        if reg[key] >= largest2:
            largest2 = reg[key]
            

largest = 0
for key in reg.keys():
    if reg[key] >= largest:
        largest = reg[key]


print('The answer to part 1: ', largest)
print('The answer to part 2: ', largest2)