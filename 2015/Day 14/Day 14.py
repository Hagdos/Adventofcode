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
    
# =============================================================================
# Part 2
# =============================================================================

class Reindeer:
    def __init__(self, line):
        line = line.strip().split()    
        self.speed = int(line[3])
        self.tfly = int(line[6])
        self.trest = int(line[13])
        self.ttotal = self.tfly+self.trest
        self.flying = True
        self.time = 0
        self.distance = 0
        self.points = 0
        
    def step(self):
        self.distance += self.speed*self.flying
        self.time += 1
        if self.time%self.ttotal >= self.tfly:
            self.flying = False
        else:
            self.flying = True
        return self.distance
            
text = open('input.txt')
t1 = 2503

reindeers = []

for line in text:
    reindeers.append(Reindeer(line))
    
for t in range(t1):
    distances = []    
    for reindeer in reindeers:
        distances.append(reindeer.step())
    for reindeer in reindeers:
        if reindeer.distance == max(distances):
            reindeer.points += 1
points = []    
for reindeer in reindeers:
    points.append(reindeer.points)
    
print("Answer to part 1:", max(distances))
print("Answer to part 2:", max(points))