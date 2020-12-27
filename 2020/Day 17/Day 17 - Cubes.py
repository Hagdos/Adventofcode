import copy
f = open('init.txt')
#Layout is ThreeD[z][y][x]
def printlayout(layout, zdepth):
    for i in layout[zdepth]:
        print(''.join(i))
    print()
    
def printcube(layout):
    for i in range(len(layout)):
        print('Layer', i)
        printlayout(cube,i)
    

#Counts the number of active points directly around the coordinate x,y,z. Does not take into account the difference between cubes; so coordinates still need to be increased with one
def countactive(cube, z,y,x):
    zsize = len(cube)
    ysize = len(cube[0])
    xsize = len(cube[0][0])
    activesum = 0
    for zc in range(z-1,z+2):
        for yc in range(y-1,y+2):
            for xc in range(x-1,x+2):
                if 0 <= zc < zsize and 0 <= yc < ysize and 0 <= xc < xsize and not (xc == x and yc == y and zc == z):
                    if cube[zc][yc][xc] == '#':
                        activesum+=1
                    # print(zc, yc, xc, cube[zc][yc][xc])
    return activesum

#Init; read out file
TwoD = []
for x in f:
    TwoD.append(x.strip())

xsize = len(TwoD[0])
ysize = len(TwoD)
zsize = 1
cube = [TwoD[:]]*zsize

#Perform steps
for _ in range(6):

    xsize += 2
    ysize += 2
    zsize += 2
    
    #Copy cube to oldcube; create new one
    oldcube = cube
    
    line = ['.']*xsize
    square = []
    for i in range(ysize):
        square.append(line[:])
    cube = []
    for i in range(zsize):
        cube.append(copy.deepcopy(square))
    
    #Fill new cube with right data
    
    for z in range(zsize):
        for y in range(ysize):
            for x in range(xsize):
                if 1 <= z < zsize-1 and 1<= y < ysize-1 and 1 <= x < xsize-1 and oldcube[z-1][y-1][x-1] == '#':
                    # print(z,y,x)
                    # print(countactive(oldcube, z-1, y-1, x-1))
                    if 2 <= countactive(oldcube, z-1, y-1, x-1) <= 3:
                        cube[z][y][x] = '#'
                elif countactive(oldcube, z-1, y-1, x-1) == 3:
                    a=1
                    cube[z][y][x] = '#'

ans = 0
for z in range(zsize):
    for y in range(ysize):
        for x in range(xsize):
            if cube[z][y][x] == '#':
                ans+=1
                
# printcube(cube)
print('Part 1 answer = ', ans, '\n')

#  -----------------  Part 2  ---------------------
f = open('init.txt')
#Layout is Cuboid[w][z][y][x]
def printlayout2(layout, zdepth, wdepth):
    for i in layout[wdepth][zdepth]:
        print(''.join(i))
    print()
    
def printcuboid(layout):
    for w in range(len(layout)):
        for z in range(len(layout[0])):            
            print('W = ', w)
            print('Z = ', z)
            printlayout2(layout, z, w)
            
#Counts the number of active points directly around the coordinate x,y,z, w. Does not take into account the difference between cubes; so coordinates still need to be increased with one
def countactive2(cuboid, w, z,y,x):
    wsize = len(cuboid)
    zsize = len(cuboid[0])
    ysize = len(cuboid[0][0])
    xsize = len(cuboid[0][0][0])
    activesum = 0
    for wc in range(w-1,w+2):
        for zc in range(z-1,z+2):
            for yc in range(y-1,y+2):
                for xc in range(x-1,x+2):
                    if 0 <= wc < wsize and 0 <= zc < zsize and 0 <= yc < ysize and 0 <= xc < xsize and not (xc == x and yc == y and zc == z and wc == w):
                        if cuboid[wc][zc][yc][xc] == '#':
                            activesum+=1
                    # print(zc, yc, xc, cube[zc][yc][xc])
    return activesum


xsize = len(TwoD[0])
ysize = len(TwoD)
zsize = 1
wsize = 1
cuboid = [[TwoD[:]]*zsize]*wsize

#Perform steps
for _ in range(6):

    xsize += 2
    ysize += 2
    zsize += 2
    wsize += 2
    
    #Copy cube to oldcube; create new one
    oldcuboid = cuboid
    
    line = ['.']*xsize
    square = []
    for i in range(ysize):
        square.append(line[:])
    cube = []
    for i in range(zsize):
        cube.append(copy.deepcopy(square))
    cuboid = []
    for i in range(wsize):
        cuboid.append(copy.deepcopy(cube))
        
    # printcuboid(oldcuboid)
    
    #Fill new cube with right data
    for w in range(wsize):
        for z in range(zsize):
            for y in range(ysize):
                for x in range(xsize):
                    if 1<= w < wsize-1 and 1 <= z < zsize-1 and 1<= y < ysize-1 and 1 <= x < xsize-1 and oldcuboid[w-1][z-1][y-1][x-1] == '#':
                        # print(w,z,y,x)
                        if 2 <= countactive2(oldcuboid, w-1, z-1, y-1, x-1) <= 3:
                            # print(w,z,y,x)
                            cuboid[w][z][y][x] = '#'
                    elif countactive2(oldcuboid, w-1, z-1, y-1, x-1) == 3:
                        a=1
                        cuboid[w][z][y][x] = '#'

ans = 0
for w in range(wsize):
    for z in range(zsize):
        for y in range(ysize):
            for x in range(xsize):
                if cuboid[w][z][y][x] == '#':
                    ans+=1
                
# printcuboid(cuboid)
print('Part 2 answer: ', ans)
