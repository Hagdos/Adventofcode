from photofunctions import *
import re

f = open('photos.txt')

photos = {}

for x,line in enumerate(f):
    if line[0] == 'T':
        key = int(line.strip().split(' ')[1][:4])
        photo = []
    elif line[0] == '\n':
        photos[key] = photo
    else:
        photo.append(line.strip())
photos[key] = photo
    
matches = {}
for p1 in photos:
    edges = getedges(photos[p1])
    match = []
    for p2 in photos:
        if p2 != p1:
                if any(e in edges for e in get4edges(photos[p2])):
                    # print('Match! P2 = ', p2)
                    match.append(p2)
    matches[p1] = match

ans = 1
for p in matches:
    if len(matches[p]) == 2:
        ans *= p
        
print('Answer to part 1 = ',ans, '\n')

# ---------- Part 2 ----------------

size = int(len(photos)**0.5)
parray = [ [] for _ in range(size) ]

#Fill top left corner
for p in matches:
    if len(matches[p]) == 2:
        parray[0].append(p)
        parray[0].append(matches[p][0])
        parray[1].append(matches[p][1])
        break

# =============================================================================
# #             Rotate top left corner to the right position
# =============================================================================
y = x = 0
# printphoto(photos[parray[y][x]])
p1 = photos[parray[y][x]]
   
if getright(p1) in getedges(photos[parray[y][x+1]]):
    pass
elif getleft(p1) in getedges(photos[parray[y][x+1]]):
    p1 = flipy(p1)    
elif gettop(p1) in getedges(photos[parray[y][x+1]]):  
    p1 = rotate(p1, 1)
elif getbottom(p1) in getedges(photos[parray[y][x+1]]):
    p1 = rotate(p1, 3)
else:
    assert False
if getbottom(p1) in getedges(photos[parray[y+1][x]]):
    pass
elif gettop(p1) in getedges(photos[parray[y+1][x]]):
    p1 = flipx(p1)
else:
    assert False

photos[parray[y][x]] = p1
# =============================================================================
#  #          Fill everything to the right
# =============================================================================
for y in range(size):
    x = 0
    if y!= 0:
# =============================================================================
#     Go 1 row lower
# =============================================================================
        
        p1 = photos[parray[y][x]]
        tomatch = getbottom(photos[parray[y-1][x]])
        if tomatch in getflipedges(p1):
            p1 = rotate(p1,2)
        if gettop(p1) in tomatch:
            pass
        elif getbottom(p1) in tomatch:
            p1 = flipx(p1)
        elif getright(p1) in tomatch:
            p1 = rotate(p1, 3)
        elif getleft(p1) in tomatch:
            p1 = rotate(p1, 1)
            p1 = flipy(p1)
        else:
            assert False
        photos[parray[y][x]] = p1
        for m in matches[parray[y][x]]:
            if getright(p1) in getedges(photos[m]):
                parray[y].append(m)
            if getbottom(p1) in getedges(photos[m]):
                parray[y+1].append(m)
             
    for x in range(1,size):
        p1 = photos[parray[y][x]]
        tomatch = getright(photos[parray[y][x-1]])
        if tomatch in getflipedges(p1):
            p1 = rotate(p1, 2)
        if getleft(p1) in tomatch:
            pass
        elif getright(p1) in tomatch:
            p1 = flipy(p1)
        elif gettop(p1) in tomatch:
            p1 = rotate(p1, 3)
            p1 = flipx(p1)
        elif getbottom(p1) in tomatch:
            p1 = rotate(p1, 1)
        else:
            assert False
        # if parray[y][x] == 2473:
        #     printphoto(p1)
        photos[parray[y][x]] = p1
        # =============================================================================
        #     #           Fill in parray to the right and bottom
        # =============================================================================
        for m in matches[parray[y][x]]:
            if getright(p1) in getedges(photos[m]):
                parray[y].append(m)
            # if getbottom(p1) in getedges(photos[m]):
            #     print(parray[y][x], m)
            #     parray[y+1].append(m)
# =============================================================================
# Strip all photos     
# =============================================================================
for i in photos:
    photos[i] = stripphoto(photos[i])

big = stitchfull(parray,photos)
# big = flipy(rotate(big, 1))

# printphoto(big)
# big = flipx(big)
i = 0


regex1 = re.compile('(?=#....##....##....###)')
regex2 = re.compile('.#..#..#..#..#..#...')

monstercount = 0
roughness = 0

big = rotate(big, 1)                                                            #This is my big picture, rotated to the correct position
for _ in range(2):                                                              #Run it multiple times; to find multiple monsters on the same line line 
    for y, line in enumerate(big):                                              #For each line search if the middle part of the monster is in there
        if regex1.findall(line):
            # i+=1
            # print(regex1.findall(line), i)
            f = regex1.search(line)         
            if big[y-1][f.start()+18] == '#':                                   #If it is, check if the "head" of the monster is there                            
                if regex2.findall(big[y+1][f.start():f.start()+20]):            #If it is, check if the bottom of the monster is there
                    monstercount+=1                                         
                    nrule = list(big[y])                                        #If it is, replace the first # of the monster with an S, so it isn't found again    
                    nrule = nrule[:f.start()] + ['S'] + nrule[f.start()+1:]
                    big[y] = ''.join(nrule)  
            else:
                q = regex1.findall(line)
                print(q, f.start(), y)
                print(line)
            #     nrule = list(big[y])                                        #If it is, replace the first # of the monster with an S, so it isn't found again    
            #     nrule = nrule[:f.start()] + ['O'] + nrule[f.start()+1:]
            #     big[y] = ''.join(nrule)
            #     roughness += 1
            for i in regex1.finditer(line):
                print(y, i)


for line in big:
    for char in line:
        if char == '#':
            roughness +=1
print('Monsters = ', monstercount)     
print(roughness-monstercount*14)  #Now only 14 because of the S


# printphoto(photos[parray[y][x]])
# printphoto(stripphoto(photos[parray[y][x]]))

Initialroughness = 2440

#1930 is too high
#1900 is too high
#1885 is the right answer. I'm missing one monster somewhere...

# There are 37 matches to regex1
# I count 36 monsters. There should be 37

#1864 is too low




































