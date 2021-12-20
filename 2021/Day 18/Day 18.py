import copy

def add(f1, f2):
    s = [f1, f2]
    highs = True
    while highs:
        s, _, _ = explode2(s, 0)
        s, highs = findHigh(s)
    return s


def findHigh(s):
    foundHigh = False
    if type(s) == list:
        for i, a in enumerate(s):
            a, foundHigh = findHigh(a)
            if foundHigh:
                s[i] = a
                return s, foundHigh
    elif s >= 10:
        foundHigh = True
        a1 = s//2
        a2 = (s+1)//2
        return [a1, a2], foundHigh
    return s, foundHigh


def explode2(s, depth):
    if type(s) == int:
        return s, 0, 0
    
    if depth >= 4:
        return (0, s[0], s[1])
        
    if type(s) == list:
        s[0], left, r = explode2(s[0], depth+1)
        s[1] = addleft(s[1], r)
        
        s[1], l, right = explode2(s[1], depth+1)
        s[0] = addright(s[0], l)
        
        return s, left, right
        

def addleft(s, r):
    if type(s) == int:
        s += r
    else:
        s[0] = addleft(s[0], r)

    return s
    
def addright(s, l):
    if type(s) == int:
        s += l
    else:
        s[1] = addright(s[1], l)

    return s

def magnitude(s):
    if type(s) == int:
        return s
    else:
        return 3*magnitude(s[0]) + 2*magnitude(s[1])

file = open('input.txt').readlines()
snails = [eval(x.strip()) for x in file]
ans1 = ans2 = 0

# Add all snails; part 1
s = snails.pop(0)
while snails:
    s = add(s, snails.pop(0))


ans1 = magnitude(s)
    
# Part 2
file = open('input.txt').readlines()
snails = [eval(x.strip()) for x in file]
    
for s1 in snails:
    for s2 in snails:
        if s1 != s2: 
            s1c = copy.deepcopy(s1)
            s2c = copy.deepcopy(s2)
            m = magnitude(add(s1c, s2c))
            ans2 = max(ans2, m)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
