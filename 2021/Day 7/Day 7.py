file = open('input.txt').read()

data = file.strip().split(',')
data = [int(x) for x in data]

ans1 = ans2 = 0

bestfuel1 = bestfuel2 = 10000000

for i in range(0, max(data)):
    fuel1 = fuel2 = 0
    for line in data:
        path = abs(line-i)
        fuel1 += path
        fuel2 += path*(path+1)//2
        
    if fuel1 < bestfuel1:
        bestfuel1 = fuel1
    if fuel2 < bestfuel2:
        bestfuel2 = fuel2

print('The answer to part 1: ', bestfuel1)
print('The answer to part 2: ', bestfuel2)
