import time

def magnitude(vector):
    length = 0
    for v in vector:
        length += v*v
    return length**0.5


data = open('input.txt').read().splitlines()

data = [x.split(', ') for x in data]

positions = [x[0][3:-1].split(',') for x in data]
speeds = [x[1][3:-1].split(',') for x in data]
accelerations = [x[2][3:-1].split(',') for x in data]

positions = [[int(i) for i in j] for j in positions]
speeds = [[int(i) for i in j] for j in speeds]
accelerations = [[int(i) for i in j] for j in accelerations]

lowestacc = 100000
for i, a in enumerate(accelerations):
    if magnitude(a) < lowestacc:
        lowestacc = magnitude(a)
        ans1 = i

print("The answer to part 1:", ans1)

# =============================================================================
# Part 2
# =============================================================================
start = time.time()
for _ in range(10):
    positionsmagnitude = [0] * len(positions)
    # Update speeds and positions of all particles
    # Do this first, because they all update simultaneously
    for particle in range(len(positions)):
        for dim in range(3):
            speeds[particle][dim] += accelerations[particle][dim]
            positions[particle][dim] += speeds[particle][dim]
            
        # Calculate positionvectors
        positionsmagnitude[particle] = magnitude(positions[particle])
            
    # Check for collisions
    collissionparticles = set()
    # Check for all particles if their magnitude is in the list more than once
    for particle in range(len(positions)):
        if positionsmagnitude.count(positionsmagnitude[particle]) > 1:
            # If that's the case; find all the indices where the position is equal
            for i in range(len(positions)):
                if positionsmagnitude[i]==positionsmagnitude[particle] and \
                i != particle and \
                positions[i] == positions[particle]:
                        
                    collissionparticles.add(i)
    
    if collissionparticles:
        collissionparticles = list(collissionparticles)
        collissionparticles.sort()
        collissionparticles.reverse()
    
    for particle in collissionparticles:
        positions.pop(particle)
        speeds.pop(particle)
        accelerations.pop(particle)

print("Time [s]:", time.time() - start)
print("The answer to part 2:", len(positions))