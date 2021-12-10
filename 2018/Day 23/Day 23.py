from itertools import product

# Function to find how many bots are in range of a single point
# Used for debugging
def findBotsInRange(location, bots):    
    return sum([sum([abs(i-j) for i, j in zip(bot, location)]) <= bots[bot] for bot in bots])


# Function reading the input bots; returning a dict of bots
# with {location: radius}
# Also returns the answer to part 1
def readinput(inputfile):
    file = open(inputfile).readlines()
    data = [x.strip().split() for x in file]
    maxradius = 0
    positions = []
    bots = dict()
    for line in data:
        position = tuple([int(i) for i in line[0].strip('pos=<,>').split(',')])
        radius = int(line[1].strip('r='))
        if radius > maxradius:
            maxradius = radius
            bestposition = position
    
        positions.append(position)
        bots[position] = radius
    
    ans1 = sum([sum([abs(i-j) for i, j in zip(position, bestposition)]) <= maxradius for position in positions])

    return bots, ans1


# Function to check how many bots have (a part of) a given cube in their range
# The cube is defined by a midpoint and a size; ranging from midpoint-size
# to midpoint + size; so effectively (size+1)^3 large.
# This gives an upper limit for the number of bots in range of any point 
# within the cube
def checkCube(midpoint, size, bots):
    botsInRange = 0
    for b in bots:
        distance = 0
        # The manhattan distance is the sum of the distance in each dimension
        for dim in range(3):
            # Check the distance on this axis between bot and closest plane
            # The size//2 is subtracted; because the distance to the edgeplane
            # of the cube is needed; not to the midpoint
            d = abs(midpoint[dim] - b[dim]) - size//2
            # If the distance is negative; that means the point is within
            # the cube (for this dimension) and the distance can be set to 0
            distance += max(d, 0)
        
        # If the manhattan distance is smaller or equal to the bots radius
        # at least a part of the cube is in range of the bot.
        if distance <= bots[b]:
            botsInRange += 1

    return (botsInRange, size, midpoint)

# Function to split a cube in 8 smaller cubes; and return them and their values
def splitCube(midpoint, size, bots):
    newCubes = []
    if size > 2:
        # Add the 8 cubes; midpoints at +/- half of the size
        for direction in product((-1, 1), repeat=3):
            newmidpoint = tuple(midpoint[i] + size//4 * direction[i] for i in range(3))
            newCubes.append(checkCube(newmidpoint, size//2, bots))
    
    # When the size is 2 (actually 3); all 27 points should be added as 
    # cubes of size 1
    elif size == 2:
        for direction in product((-1, 0, 1), repeat=3):
            newmidpoint = tuple(midpoint[i] + direction[i] for i in range(3))
            newCubes.append(checkCube(newmidpoint, 1, bots))

    return newCubes

bots, ans1 = readinput('input.txt')
print('The answer to part 1:', ans1)

# Stack of cubes checked so far; find the best cube each time
cubes = []

# Start with a single cube; centered around origin
point = (0, 0, 0)
# The size we start with is the distance between the two furthest bots
# x-axis turned out to be the largest
xrange = range(min([x[0]+bots[x] for x in bots]),
               max([x[0]-bots[x] for x in bots]))
# Take a power of two; so it's easily divisible every time.
size = 2**len(xrange).bit_length()

# Every cycle; pick the best cube; and split it in smaller cubes
# The best cube is defined as the cube with the highest possible bots in range
# In equal cases; the largest cube is taken; to prevent stopping too early.

# If the best cube is of size 1 (a point), that's the answer. All other cubes
# can not contain a better point
for i in range(200):
    cubes += splitCube(point, size, bots)
    cubes.sort()
    
    botsinrange , size, point = cubes.pop()
    if size == 1:
        print('The answer to part 2:', sum(point))
        break
        
    
# Definition of a cube:
# It has a midpoint (x,y,z) and a size n+1 (n being a power of 2)
# The edges of the cube are at dim - n//2 and dim + n//2
# This causes the edges of cubes to just overlap; but makes math easier (symmetric cubes around a point)


# How to check if a bot is in range of a cube:
# Calculate the distance from bot to midpoint; minus the size of the cube
# If any dimension is within the range of the cube; it is "in" the cube
# (for that dimension); so the distance is 0.
# If all dimensions are within the range of the cube; the bot is in the cube
# and it's within range by definition.
