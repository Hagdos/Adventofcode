import time
import bisect

file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
ans2 = 100000

depth = int(data[0][1])
tx, ty = (int(i) for i in data[1][1].split(','))

size = ty + 100

# Create arrays for erosion and rocktype
erosion = [[None]*(size) for _ in range(size)]
rtype = [[None]*(size) for _ in range(size)]
emod = 20183

for y in range(size):
    for x in range(size):
        if y == 0:
            erosion[y][x] = (x*16807 + depth) % emod
        elif x == 0:
            erosion[y][x] = (y*48271 + depth) % emod
        elif x == tx and y == ty:
            erosion[y][x] = depth
        else:
            erosion[y][x] = (erosion[y-1][x] * erosion[y][x-1] + depth) % emod
        rtype[y][x] = erosion[y][x] % 3


# Ideal score is distance to go + minutes; because that guarantees that
# the first solution that arrives is also the best (Any other solution would
# have to at least add the missing distance in minutes)
# But that converges very slowly; because a step in the right direction
# doesn't really increase the score
# 7 minutes are added if the wrong equipment is equipped
def calcScore(x, y, minutes, equip):
    score = abs(tx-x) + abs(ty-y) + minutes
    if equip != 1:
        score += 7
    return score

# Return a list of all possible next steps (4 directions + equipment change)
# Will only return the steps that are possible with the current equipment
# Does not check if the next step is already known
def nextSteps(status):
    _, minutes, x, y, equip = status
    ns = []
    for dx in (-1, 1):
        if x+dx >= 0 and rtype[y][x+dx] != equip:
            ns.append((calcScore(x+dx, y, minutes+1, equip), minutes + 1, x+dx, y, equip))
    for dy in (-1, 1):
        if y+dy >= 0 and rtype[y+dy][x] != equip:
            ns.append((calcScore(x, y+dy, minutes+1, equip), minutes + 1, x, y+dy, equip))

    # Equipment change -> Change to the equipment that's not the current
    # and not the same as the current tile's type.
    t = rtype[y][x]
    newequip = [e for e in (0, 1, 2) if e != equip and e != t][0]
    ns.append((calcScore(x, y, minutes+7, newequip), minutes+7, x, y, newequip))

    return ns

# Starting position: location 0,0; equipped with torch.
x, y = (0, 0)
equip = 1
minutes = 0

# A status contains a score for sorting the most promising head, the minutes
# taken so far, x/y-location and the equipped tool
status = (calcScore(x, y, minutes, equip), minutes, x, y, equip)

# seen is a list of already visited locations + equipment; with the lowest
# possible minutes to get there
seen = {(x, y, equip): 0}

# heads is the list of all trailheads. Every step the most promising head
# is taken off the list; and the next steps for that head are added to the list
heads = [status]
found = False

start = time.time()
for step in range(250000):
    if step % 50000 == 0:
        print(step, ans2, time.time()-start)

    best = heads.pop(0)
    ns = nextSteps(best)
    for n in ns:
        _, minutes, x, y, equip = n

        # For every nextstep; check if it's the destination
        if x == tx and y == ty and equip == 1:
            print('Solution:', minutes, step)
            ans2 = minutes
            found = True
            break

        # And check if we've been here before. If we've already found 
        # a path to (x,y) that's better or as good as; skip this nextstep.
        elif (x, y, equip) not in seen or seen[(x, y, equip)] > minutes:
            # Otherwise; add/update the seen
            seen[(x, y, equip)] = minutes
            # And add to the sorted list; in the right location
            bisect.insort(heads, n)

    if found:
        break

print('The answer to part 1: ', sum([sum(x[:tx+1]) for x in rtype[:ty+1]]))
print('The answer to part 2: ', ans2)

# Rocky = 0 : Allows gear and torch  (2, 1)
# Wet   = 1 : Allows gear and none   (2, 0)
# Narrow= 2 : Allows torch and none  (0, 1)

# none  = 0
# torch = 1
# gear  = 2

# Each type allows all but itself
