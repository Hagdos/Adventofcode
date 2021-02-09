f = open('map.txt')

alive = set()

for x,line in enumerate(f):
    xrange = yrange = range(len(line))              #Determine the size of the grid, to loop over
    for y, char in enumerate(line.strip()):         #Add all alive bugs to a set called alive()
        if char == '#':
            alive.add((x,y))
 
#Check for the four neighbours of the given coordinate if they're in the given set, and return the sum.
def count(x,y, alive):                                           
    c = 0
    for (a,b) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if (a,b) in alive:
              c+=1
    return c

#oldalives is a list of all sets that have passed; to check if a new alive set is equal to a previous one
oldalives = []
#newalive is the set that will be filled in the coming minute/iteration
newalive = set()

while alive not in oldalives and len(oldalives)<1000:
    for x in xrange:
        for y in yrange:
            if (x,y) in alive and count(x,y, alive) == 1:           #If x,y is alive now and has exactly 1 neighbour, it's alive in the new set
                newalive.add((x,y))
            elif (x,y) not in alive and count(x,y,alive) in [1,2]:  #If xy is not alive now and has 1 or 2 neighbours, it's alive in the new set
                newalive.add((x,y))
   
    oldalives.append(alive)
    alive = newalive
    newalive = set()

ans = 0
#Calculate the answer; n is the position counting from left to right, top to bottom (starting at 0). The sum is 2^n of all alive locations.
for a in alive:
    n = a[1]+a[0]*(max(xrange)+1)
    # print(a, n, 2**n)
    ans += 2**n
    
print('Answer to Part 1:', ans)

# =============================================================================
# Part 2 
# =============================================================================

f = open('map.txt')
minutes = 200
alive = {}
alive[0] = set()

for x,line in enumerate(f):
    xrange = yrange = range(len(line))              #Determine the size of the grid, to loop over
    for y, char in enumerate(line.strip()):         #Add all alive bugs to a set called alive()
        if char == '#':
            alive[0].add((x,y))

# Check for all the neighbours of the given coordinate if they're in the given set, and return the sum.
def count2(x,y,layer,alive):                                           
    count = 0
    for (a,b) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if (a,b) == (2,2):                      #If the neighbour is the middle square (higher layer)
            if layer+1 in alive.keys():         #If the layer above doesn't exist yet, the sum is zero
                if x == 1:         
                    x2 = [0]*5
                    y2 = yrange
                elif x == 3:
                    x2 = [4]*5
                    y2 = yrange
                elif y == 1:
                    x2 = xrange
                    y2 = [0]*5
                elif y == 3:
                    x2 = xrange
                    y2 = [4]*5
                for (c,d) in zip(x2,y2):
                    if (c,d) in alive[layer+1]:
                        count += 1
        elif a not in xrange or b not in yrange:            #if the neighbour is outside (lower layer))
            if layer-1 in alive.keys():                     #If the layer below doesn't exist yet, the sum is zero
                if a == -1 and (1,2) in alive[layer-1]:
                    count += 1
                elif a == 5 and (3,2) in alive[layer-1]:
                    count += 1
                elif b == -1 and (2,1) in alive[layer-1]:
                    count += 1
                elif b == 5 and (2,3) in alive[layer-1]:
                    count += 1
        elif (a,b) in alive[layer]:
              count += 1
    return count

newalive = {}


for _ in range(minutes):
    for layer in alive.keys():
        newalive[layer] = set()
        for x in xrange:
            for y in yrange:
                if (x,y) == (2,2):
                    pass
                elif (x,y) in alive[layer] and count2(x,y,layer,alive) == 1:           #If x,y is alive now and has exactly 1 neighbour, it's alive in the new set
                    newalive[layer].add((x,y))
                elif (x,y) not in alive[layer] and count2(x,y,layer,alive) in [1,2]:  #If xy is not alive now and has 1 or 2 neighbours, it's alive in the new set
                    newalive[layer].add((x,y))
                    
    for layer in [min(alive.keys())-1, max(alive.keys())+1]:
        newalive[layer] = set()
        alive[layer] = set()
        for x in xrange:
            for y in yrange:
                if (x,y) == (2,2):
                    pass
                elif count2(x,y,layer,alive) in [1,2]:  #xy is not alive now; if it has 1 or 2 neighbours, it's alive in the new set
                    newalive[layer].add((x,y))
   
    alive = newalive
    newalive = {}
    
ans = 0
for layer in alive:
    ans += len(alive[layer])
    
print("Answer to Part 2:", ans)
