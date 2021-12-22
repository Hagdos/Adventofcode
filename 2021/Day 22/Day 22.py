import copy

def checkOverlap(r1, r2):
    if any(r2[d][1] < r1[d][0] or r2[d][0] > r1[d][1] for d in range(3)):
        return False
    else:
        return True

def returnRemaining(ra, r2):
    r1 = copy.deepcopy(ra)
    remaining = []
    for dim in range(len(r1)):
        if r1[dim][0] < r2[dim][0] <= r1[dim][1] :
            new = [d.copy() for d in r1]
            new[dim][1] = r2[dim][0]-1
            r1[dim][0] = r2[dim][0]
            remaining.append(new)
        if r1[dim][0] <= r2[dim][1] < r1[dim][1]:
            new = [d.copy() for d in r1]
            new[dim][0] = r2[dim][1]+1
            r1[dim][1] = r2[dim][1]
            remaining.append(new)
  
    return remaining

def size(r):
    s = 1
    for dim in range(len(r)):
        d = r[dim][1] - r[dim][0] + 1
        s *= d        
    return s

file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans = 0

boxes = []

for line in data:
    cmd, coords = line.split(' ')
    ranges = coords.split(',')
    ranges = [[int(i) for i in x[2:].split('..')] for x in ranges]
    boxes.append((cmd, ranges))
    
sboxes = boxes[:]


overlaps = []
for i, (cmd, ranges) in enumerate(sboxes):
    if cmd == 'on':
        onboxes = [ranges]
        for _, r2 in sboxes[i+1:]:
            new_onboxes = []
            for r1 in onboxes:
                if checkOverlap(r1, r2):
                    new_onboxes += returnRemaining(r1, r2)
                else:
                    new_onboxes.append(r1)
            onboxes = new_onboxes

                
        for r1 in onboxes:
            ans += size(r1)
    if i == 19:
        print('The answer to part 1: ', ans)
            
            
print('The answer to part 2: ', ans)