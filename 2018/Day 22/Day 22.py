import time
import bisect

file = open('2018/Day 22/input.txt').readlines()
data = [x.strip().split() for x in file]
ans2 = 100000

depth = int(data[0][1])
tx, ty = (int(i) for i in data[1][1].split(','))

# # Testvalues
# depth = 510
# tx, ty = (10, 10)

size = ty + 1000

erosion = [[None]*(size) for _ in range(size)]
rtype = [[None]*(size) for _ in range(size)]
emod = 20183

for x in range(size):
    erosion[0][x] = (x*16807 + depth) % emod
    rtype[0][x] = erosion[0][x] % 3


for y in range(1, size):
    for x in range(size):
        if x == 0:
            erosion[y][x] = (y*48271 + depth) % emod
        else:
            erosion[y][x] = (erosion[y-1][x] * erosion[y][x-1] + depth) % emod
        rtype[y][x] = erosion[y][x] % 3

erosion[ty][tx] = 0
rtype[ty][tx] = 0


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


def nextSteps(status):
    _, minutes, x, y, equip = status
    ns = []
    for dx in (-1, 1):
        if x+dx >= 0 and rtype[y][x+dx] != equip:
            ns.append((calcScore(x+dx, y, minutes+1, equip), minutes + 1, x+dx, y, equip))
    for dy in (-1, 1):
        if y+dy >= 0 and rtype[y+dy][x] != equip:
            ns.append((calcScore(x, y+dy, minutes+1, equip), minutes + 1, x, y+dy, equip))

    # Equipment change
    t = rtype[y][x]
    newequip = [e for e in (0, 1, 2) if e != equip and e != t][0]
    ns.append((calcScore(x, y, minutes+7, newequip), minutes+7, x, y, newequip))

    return ns


x, y = (0, 0)
equip = 1
minutes = 0

status = (calcScore(x, y, minutes, equip), minutes, x, y, equip)

seen = {(x, y, equip): 0}
heads = [status]
found = False

start = time.time()
for step in range(294332):
    if step % 50000 == 0:
        print(step, ans2, time.time()-start)

    best = heads.pop(0)
    ns = nextSteps(best)

    print(ns)
    for n in ns:
        _, minutes, x, y, equip = n

        assert rtype[x][y] != n

        if x == tx and y == ty and equip == 1:
            print('Solution:', minutes, step)
            ans2 = min(ans2, minutes)
            # found = True
            # break

        # if this position has already been visited; with less minutes
        # dont use this direction
        elif (x, y, equip) not in seen or seen[(x, y, equip)] > minutes:
            seen[(x, y, equip)] = minutes
            bisect.insort(heads, n)

    if found:
        break


print("Step:", step)
print(*heads[:20], sep='\n')
print("(scr, m, x, y, e)")

print('The answer to part 1: ', sum([sum(x[:tx+1]) for x in rtype[:ty+1]]))
print('The answer to part 2: ', ans2)

# print(*rtype[ty-2:ty+3], sep='\n')
# 1122 is too high
# 1095 is too high
# 1056 is too high
# 1048 is wrong
# 1041 is wrong

# Someone else's input says 1043..

# Rocky = 0 : Allows gear and torch  (2, 1)
# Wet   = 1 : Allows gear and none   (2, 0)
# Narrow= 2 : Allows torch and none  (0, 1)

# none  = 0
# torch = 1
# gear  = 2

# Each type allows all but itself
