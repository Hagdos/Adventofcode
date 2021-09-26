file = open('input.txt').readlines()

pipes = dict()

for line in file:
    data = line.strip().split(' <-> ')
    pipes[int(data[0])] = [int(x) for x in data[1].split(', ')]
    
ingroups = []
toadds = []

groupnumber = 0

for checkprogram in pipes.keys():
    if not any(checkprogram in ingroup for ingroup in ingroups):
        
        ingroups.append([checkprogram])
        toadds.append(pipes[checkprogram])
    
        while toadds[groupnumber]:
            program = toadds[groupnumber].pop()
            ingroups[groupnumber].append(program)
            for newprogram in pipes[program]:
                if newprogram not in ingroups[groupnumber]:
                    toadds[groupnumber].append(newprogram)
                    
        groupnumber += 1

ans1 = len(ingroups[0])

ans2 = len(ingroups)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
