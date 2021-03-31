text = open('input.txt')
t1 = 2503

reindeer = dict()

fastest = 0

for line in text:
    line = line.strip().split()
    data = dict()
    name = line[0]
    data['speed'] = int(line[3])
    data['tfly'] = int(line[6])
    data['trest'] = int(line[13])    
    data['ttotal'] = (data['tfly']+data['trest'])
    data['avSpeed'] = data['speed']*data['tfly']/data['ttotal']
    
    reindeer[name] = data
    
bestDistance = 0        
for deer in reindeer.keys():
    distance = t1//reindeer[deer]['ttotal']*reindeer[deer]['speed']*reindeer[deer]['tfly'] + min(t1%reindeer[deer]['ttotal'], reindeer[deer]['tfly'])*reindeer[deer]['speed']
    if distance > bestDistance:
        bestDistance = distance
        
print('Answer to part 1:', bestDistance)
    
