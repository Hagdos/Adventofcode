from copy import deepcopy
f = open('Instructions.txt')

instr = []

for i in f:
    instr.append(i.strip())
    
blacks = set()

# instr = ['eew', ' ee']
for ix in instr:
    i = list(ix)
    i.reverse()
    
    x = 0
    y = 0
    
    while(i):
        c = i.pop()
        if c == 'e':
            x+= 2
        elif c == 'w':
            x-= 2
        elif c in ['s', 'n']:
            c2 = i.pop()
            if c == 's':
                y+=1
            elif c=='n':
                y-=1
            if c2 == 'e':
                x += 1
            elif c2 == 'w':
                x -= 1
    
    if (x,y) in blacks:
        blacks.remove((x,y))
    else:
        blacks.add((x,y))
        
# print("Answer to Part 1 :", len(blacks))

# =============================================================================
# Part 2 
# =============================================================================

def size(blacks):
    xmax = ymax = 0
    for i in blacks:
        if abs(i[0]) > xmax:  xmax = abs(i[0])
        if abs(i[1]) > ymax:  ymax = abs(i[1])
        
    return (xmax,ymax)

def countneighbours(blacks, x,y):
    count = 0
    for dx in [-2,2]:
        if (x+dx, y) in blacks:
            # print(x+dx, y)
            count+=1
    for dx in [-1,1]:
        for dy in [-1,1]:
            if (x+dx, y+dy) in blacks:
                # print('a' , x+dx, y+dy)
                count+=1
    return count
            
            





for a in range(1,101):
    nblacks = deepcopy(blacks)
    xmax, ymax = size(blacks)
    xmax += xmax%2 
    # print(xmax, ymax)
    for y in range(-ymax-2, ymax+3):
        for x1 in range(-xmax-4, xmax+4, 2):
            x = x1+y%2
            neighbours = countneighbours(blacks, x, y)
            # print(x,y, (x,y) in blacks)
            if (x,y) in blacks and not 0<neighbours<3:
                nblacks.remove((x,y))
                # print('Remove', x,y, neighbours)
            elif (x,y) not in blacks and neighbours == 2:
                nblacks.add((x,y))
                # print('Add', x,y, neighbours)
    blacks = deepcopy(nblacks)
    if a % 10 == 0:
        print(len(blacks))































# def printfloor(blacks):
    
#     xmax, ymax = size(blacks)
#     floorline = ['.']*(xmax+1)
#     floor = [deepcopy(floorline)]*ymax
#     for y in range(-ymax, ymax):
#         for x in range(-xmax, xmax, 2):
#             x1 = x+y%2
#             if (x1,y) in blacks:
#                 floor[x1][y] == '0'
#             else:
#                 floor[x1][y] == 'I'
                
#     print(floor)