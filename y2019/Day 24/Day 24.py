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
    
print('Answer part 1 = ', ans)

