import itertools
import time

now = time.time()

part2 = False

inputs = open('input.txt')

connections = dict()

for line in inputs:
    line = line.strip().split()
    person1 = line[0]
    person2 = line[-1][:-1]
    points = int(line[3])
    plusminus = line[2]
    if plusminus == 'lose':
        points *= -1
        
    connections.setdefault(person1,dict())[person2] = points
    
if part2 == True:
    connections['Me'] = dict()
    for person in connections.keys():
        connections['Me'][person] = 0
        connections[person]['Me'] = 0
    
    
groupsize = len(connections)-1
group = list(connections.keys())
maxpoints = 0

p0 = group.pop()

for ordering in itertools.permutations(group, groupsize):
    ordering = list(ordering)
    ordering.append(p0)
    points = 0
    for i, person in enumerate(ordering):
        
        points += connections[person][ordering[i-1]]
        points += connections[person][ordering[(i+1)%groupsize]]
        
    if points > maxpoints:
        maxpoints = points
        bestorder = ordering
 
print('solved in ', time.time()-now, 'seconds')
print('The answer is:', maxpoints, bestorder)
