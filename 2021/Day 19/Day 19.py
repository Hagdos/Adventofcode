import itertools

# Returns all possible rotations of a single beacon position
def rotateBeacon(beacon):
    for face in range(3):
        for dx in (-1, 1):
            x = beacon[face] * dx
            y = beacon[face-2] * dx
            z = beacon[face-1]
            
            for _ in range(4):
                yield tuple((x,y,z))
                y, z = -z, y


def rotateScanner(scanner):
    generators = []
    for b in scanner:
        generators.append(rotateBeacon(b))
        
    for _ in range(24):
        newscanner = set()
        for i in range(len(scanner)):
            newscanner.add(next(generators[i]))
        yield newscanner
        

def checkOverlap(s1, s2):
    for b1 in s1:           # Option: Instead of checking all; check only the ones at the furthest corners? (8 instead of 13/25)
        for c, b2 in enumerate(s2):     
            if c > len(s2)-12:
                break
            (dx, dy, dz) = (i2 - i1 for i1, i2 in zip(b1, b2))
            overlap = 0
            for c2, beacon in enumerate(s2):
                beacon1 = tuple(i-di for i,di in zip(beacon, (dx,dy,dz)))
                if beacon1 in s1:
                    overlap +=1
                elif c2 - overlap > len(s2)-12:
                    break
            
            if overlap >= 12:
                return (dx, dy, dz)            
    return None
    

file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

# Read input to a list of scanners.
# Each scanner contains a set of 25 beacon locations
scanners = []
scanner = set()
for line in data:
    if line:
        if line[:3] == '---':
            if scanner:
                scanners.append(scanner)
                scanner = set()
        else:
            scanner.add(tuple(int(i) for i in line.split(',')))
scanners.append(scanner)    


positions = set()
# Find all beacons
knownBeacons = scanners.pop(0)
while(scanners):
    s = scanners.pop(0)
    found = False
    for s1 in rotateScanner(s):
        position = checkOverlap(knownBeacons, s1)
        if position:
            for beacon in s1:
                newBeacon = tuple(i-di for (i, di) in zip(beacon, position))
                knownBeacons.add(newBeacon)
                positions.add(position)
            print('Found one! Scanners to go:', len(scanners))
            found = True
            break
    if not found:
        scanners.append(s1)

for p1, p2 in itertools.combinations(positions, 2):
    distance = sum([abs(a-b) for a,b in zip(p1, p2)])
    ans2 = max(ans2, distance)
    
print('The answer to part 1: ', len(knownBeacons))
print('The answer to part 2: ', ans2)

