#Print photo in console
def printphoto(photo):
    for x in photo:
        printline(x)
        print()
    print()
    
#Print line of photo in console
def printline(line):
    print(line, end=' ')
    # for c in line:
    #     # print(c, ' ', end='')
    #     print(c,  end='')
    # # print()
    
    
#Print full picture
def printfull(parray, photos):
    for py in parray:
        for line in range(len(photos[py[0]])):
            for px in py:
                printline(photos[px][line])
            print()
        print()
        
def stitchfull(parray, photos):
    bigphoto = []
    for py in parray:
        for line in range(len(photos[py[0]])):
            l = []
            for px in py:
                l.append(photos[px][line])
            bigphoto.append(''.join(l))
    return bigphoto


#Rotates a photo to the right
def rotate(photo, n):
    xlen = len(photo[0])-1
    # ylen = len(photo)-1
    nphoto = photo
    for _ in range(n):
        nphoto = []
        for y, line in enumerate(photo):
            nline = []
            for x, char in enumerate(line):
                nline.append(photo[xlen-x][y])
            nphoto.append(''.join(nline))
        photo = nphoto
    return nphoto


#Flip a photo over the x-axis

def flipy(photo):
    nphoto = []
    for line in photo:
        nphoto.append(flipx(line))
    return nphoto

def flipx(photo):
    return photo[::-1]

def gettop(photo):
    return(photo[0])

def getbottom(photo):
    return(photo[-1])

def getleft(photo):
    nline = []
    for line in photo:
        nline.append(line[0])
    return ''.join(nline)

def getright(photo):
    nline = []
    for line in photo:
        nline.append(line[-1])
    return ''.join(nline)

def getedges(ph):
    edges = []
    edges.append(getright(ph))
    edges.append(getleft(ph))
    edges.append(gettop(ph))
    edges.append(getbottom(ph))
    edges.append(flipx(getright(ph)))
    edges.append(flipx(getleft(ph)))
    edges.append(flipx(gettop(ph)))
    edges.append(flipx(getbottom(ph)))
    return edges

def get4edges(ph):
    edges = []
    edges.append(getright(ph))
    edges.append(getleft(ph))
    edges.append(gettop(ph))
    edges.append(getbottom(ph))
    return edges

def getflipedges(ph):
    edges = []
    edges.append(flipx(getright(ph)))
    edges.append(flipx(getleft(ph)))
    edges.append(flipx(gettop(ph)))
    edges.append(flipx(getbottom(ph)))
    return edges

def stripphoto(ph):
    nph = []
    for line in ph[1:-1]:
        nph.append(line[1:-1])
    return nph



