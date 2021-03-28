import itertools

rules = open('input.txt')

cities = set()

distances = dict()

for line in rules:
    line = line.strip().split(' ')
    cities.add(line[0])
    cities.add(line[2])
    
    if line[0] not in distances:
        distances[line[0]] = dict()
        
    if line[2] not in distances:
        distances[line[2]] = dict()
    
    distances[line[0]][line[2]] = int(line[4])
    distances[line[2]][line[0]] = int(line[4])
    
shortestDistance = 1000
longestDistance = 0

for path in itertools.permutations(cities, len(cities)):
    distance = 0
    for i in range(len(path)-1):
        distance += distances[path[i]][path[i+1]]
        
    if distance < shortestDistance:
        shortestDistance = distance
        shortestPath = path
        
    if distance > longestDistance:
        longestDistance = distance
        
print('Answer part 1:', shortestDistance)
print('Answer part 2:', longestDistance)


#95 is wrong