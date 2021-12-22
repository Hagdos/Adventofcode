from collections import OrderedDict

def play(p, s, die):
    p += sum(range(die, die+3))
    while p>10:
        p -= 10
        
    s += p
    die += 3
    while die > 100:
        die -= 100
    
    return p, s, die

p1 = 10
p2 = 7

s1 = s2 = 0
die = 1
rolls = 0
while s1 < 1000 and s2 < 1000:
    rolls += 6
    p1, s1, die = play(p1, s1, die)
    if s1 >= 1000:
        rolls -= 3
        break
    p2, s2, die = play(p2, s2, die)
    
print('The answer to part 1: ', rolls * min(s1, s2))

# =============================================================================
# Part 2
# =============================================================================

p = (10, 7)
s = (0, 0)

universes = OrderedDict()
s1 = s2 = 0
turn = 0

ts = [0, 0]

universes[(p, s, turn)] = 1
while universes:
    (p, s, turn), n = universes.popitem(False)
    for die1 in range(1,4):
        for die2 in range(1,4):
            for die3 in range(1,4):
                np = list(p)
                np[turn] += die1 + die2 + die3
                if np[turn] > 10:
                    np[turn] -= 10
                ns = list(s)
                ns[turn] += np[turn]
                
                if ns[turn] >= 21:
                    ts[turn] += n
                else:
                    universes[(tuple(np), tuple(ns), (turn+1)%2)] = universes.get((tuple(np), tuple(ns), (turn+1)%2), 0) + n

print('The answer to part 2: ', max(ts))