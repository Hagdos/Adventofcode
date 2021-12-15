import bisect

file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

risk = []

for line in data:
    line = [int(i) for i in line]
    risk.append(line)
    

risk2 = []
for line in data:
    nl = []
    for i in range(5):
        nl += [(int(l)+i)%9 for l in line]
    risk2.append(nl)
    
for j in range(1, 5):
    for i in range(len(data)):
        nl = [(l + j)%9 for l in risk2[i]]
        risk2.append(nl)
    
x = y = 0
r = 0
tx1 = len(risk[0])-1
ty1 = len(risk)-1 
tx2 = len(risk2[0])-1
ty2 = len(risk2)-1 

heads = [(r, x, y)]
seen = set((x,y))

for step in range(10000000):
    r, x, y = heads.pop(0)
    
    if (x, y) == (tx1, ty1):
        ans1 = r
    
    if (x, y) == (tx2, ty2):
        ans2 = r
        break
    
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx = x+dx
        ny = y+dy
        if  tx2 >= nx >= 0 and ty2 >= ny >= 0:
            ra = risk2[ny][nx]
            if ra == 0:
                ra = 9
            nr = r + ra
            
            if (nx,ny) not in seen:
                seen.add((nx, ny))
                bisect.insort(heads, (nr, nx, ny))
    
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)