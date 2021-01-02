import re
import time
import math

def lcm(a,b,c): 
    ab = a*b//math.gcd(a,b)
    return ab*c//math.gcd(ab,c)

class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]
        self.initposition = position
        self.cycletime = []
        
    def move(self):
        self.position = [a+b for a,b in zip(self.position, self.velocity)]
  
f = open('moons.txt')
moons = []

for moon in f:
    moon = moon.strip()
    moon = re.split('[<,=>]', moon)
    position = [int(moon[2]), int(moon[4]), int(moon[6])]
    moons.append(Moon(position))

start = time.time()

steps = 231614
for c in range(steps):
    # print()
    
    for i in range(3):
        s = []
        for m in moons:
            if m.velocity[i] == 0 and m.position[i] == m.initposition[i]:
                s.append(1)
        if len(s) == 4:
            print("Cycle on axis", i, "on cycle", c)
            
    for ma in moons:
        for mb in moons:
            if ma != mb:
                for p, v in enumerate(ma.position):
                    if v>mb.position[p]:
                        ma.velocity[p] -= 1
                    elif v<mb.position[p]:
                        ma.velocity[p] += 1
                    
    for a,m in enumerate(moons):
        m.move()

energy = 0
for m in moons:
    epot = 0
    ekin = 0
    for p in m.position:
        epot += abs(p)
    for v in m.velocity:
        ekin += abs(v)
    energy += epot * ekin
    
# print("Answer to part 1:", energy)

# =============================================================================
# Part 2
# =============================================================================



cycle0 = 186028
cycle1 = 28482
cycle2 = 231614

print(lcm(cycle0,cycle1,cycle2))