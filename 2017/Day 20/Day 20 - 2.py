import time

class Particle:
    def __init__(self, text):
        data = text.split(', ')
        self.position = [int(i) for i in data[0][3:-1].split(',')]
        self.speed = [int(i) for i in data[1][3:-1].split(',')]
        self.acceleration = [int(i) for i in data[2][3:-1].split(',')]
        self.calcmagnitude()
        
    def update(self):
        for dim in range(3):
            self.speed[dim] += self.acceleration[dim]
            self.position[dim] += self.speed[dim]
        
        self.calcmagnitude()
        
    def calcmagnitude(self):
        length = 0
        for v in self.position:
            length += v*v
        self.magnitude = length**0.5
        
    def __eq__(self, other):
        if self.magnitude == other.magnitude and \
           self.position == other.position:
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(repr(self))
        
        
data = open('input.txt').read().splitlines()

particles = []
for line in data:
    particles.append(Particle(line))
    
start = time.time()
for _ in range(100):
    for particle in particles:
        particle.update()
        
    removeset = set()
    for particle1 in particles:
        for particle2 in particles:
            if particle1 == particle2 and \
                particle1 is not particle2:
                
                
                removeset.add(particle1)
                
    for particle in removeset:
        particles.remove(particle)
    

print("Time [s]:", time.time() - start)
print("The answer to part 2:", len(particles))