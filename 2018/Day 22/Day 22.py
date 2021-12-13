import time

file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
ans2 = 10000

depth = int(data[0][1])
tx, ty = (int(i) for i in data[1][1].split(','))

# #Testvalues
# depth = 510
# tx, ty = (10, 10)

addedsize = 100

erosion = [[None]*(tx+addedsize) for _ in range(ty+addedsize)]
rtype = [[None]*(tx+addedsize) for _ in range(ty+addedsize)]
emod = 20183

for x in range(tx+addedsize):
    erosion[0][x] = (x*16807 + depth) % emod
    rtype[0][x] = erosion[0][x]%3


for y in range(1, ty+addedsize):
    for x in range(tx+addedsize):
        if x == 0:
            erosion[y][x] = (y*48271 + depth) % emod
        else:
            erosion[y][x] = (erosion[y-1][x] * erosion[y][x-1] + depth) % emod
        rtype[y][x] = erosion[y][x]%3

erosion[ty][tx] = 0
rtype[ty][tx] = 0

# Ideal score is distance to go + minutes; because that guarantees that
# the first solution that arrives is also the best
# (Any other solution would have to at least add the missing distance in minutes)
# But that converges very slowly; because a step in the right direction 
# doesn't really increase the score
def calcScore(x, y, minutes):
    return abs(tx-x) + abs(ty-y) + minutes
    # return 3*(abs(tx-x) + abs(ty-y)) + 2*minutes
    # return minutes


def calcDistance(x, y):
    return abs(tx-x) + abs(ty-y)

def nextSteps(status):
    _, _, x, y, minutes, equip = status
    ns = []
    for dx in (-1, 1):
        if x+dx >= 0 and rtype[y][x+dx] != equip:
            ns.append((calcScore(x+dx, y, minutes+1), calcDistance(x+dx, y), x+dx, y, minutes+1, equip))
    for dy in (-1, 1):
        if y+dy >= 0 and rtype[y+dy][x] != equip:
            ns.append((calcScore(x, y+dy, minutes+1), calcDistance(x, y+dy), x, y+dy, minutes+1, equip))
    
    # Equipment change
    t = rtype[y][x]
    newequip = [x for x in (0, 1, 2) if x != equip and x!= t][0]
    ns.append((calcScore(x, y, minutes+7), calcDistance(x, y), x, y, minutes+7, newequip))
    
    return ns
    
def headSort(heads):
    heads.sort(reverse=True)


x, y = (0, 0)
equip = 1
minutes = 0

status = (calcScore(x, y, minutes), calcDistance(x, y), x, y, minutes, equip)

seen = {(x, y, equip): 0}
heads = [status]
found = False

start = time.time()

for step in range(100000):
    if step%1000 == 0:
        print(step, ans2, time.time()-start)
    
    best = heads.pop()
    ns = nextSteps(best)
    for n in ns:
        _, _, x, y, minutes, equip = n
        
        if x == tx and y == ty and equip == 1:
            # ans2 = min(ans2, minutes)
            ans2 = minutes
            found = True
            break
        
        # if this position has already been visited; with less minutes
        # dont use this direction
        elif (x, y, equip) not in seen or seen[(x, y , equip)] > minutes:
            seen[(x, y, equip)] = minutes
            heads.append(n)
    
    # heads.sort(reverse=True)
    headSort(heads)
    
    if found:
        break
    

print("Step:", step)
print(*heads, sep='\n')
print("(scr, dis, x, y, m, e)")

print('The answer to part 1: ', sum([sum(x[:tx+1]) for x in rtype[:ty+1]]))

print('The answer to part 2: ', ans2)

# 1122 is too high
# 1095 is too high
# 1056 is too high

#dqueue?


# Rocky = 0 : Allows gear and torch  (2, 1)
# Wet   = 1 : Allows gear and none   (2, 0)
# Narrow= 2 : Allows torch and none  (0, 1)

# none  = 0
# torch = 1
# gear  = 2

# Each type allows all but itself