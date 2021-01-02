import intcode as ic
from PIL import Image

f = open('code.txt')
code = f.readline().strip().split(',')

white = set()
visited =set()

p2 = 1
finished = False
if p2:
    inputs = [1]
else:
    inputs = [0]
xloc = yloc = 0
location = (xloc,yloc)
direction = 0       #0 is north, 1 is east, 2 is south, 3 is west

mem = ic.codetomem(code)
counters = [0, 0, 0, 0]


while not finished:
    mem, outputs, counters, finished = ic.runintcode(mem, inputs, counters)
    colour = outputs[0]
    turn = outputs[1]
    
    #Paint current block
    if colour == 1 and location not in white:
        white.add(location)
    elif colour == 0 and location in white:
        white.remove(location)
    
    visited.add(location)
    
    #Turn the robot    
    if turn:
        direction += 1
    else:
        direction -= 1
    direction %= 4
    
    #Move 1 step forward
    if direction == 0:
        xloc -= 1
    elif direction == 1:
        yloc += 1
    elif direction == 2:
        xloc += 1
    elif direction == 3:
        yloc -= 1
    else:
        assert False, "Error"
    location = (xloc,yloc)
    
    # check current colour
    if location in white:
        inputs.append(1)
    else:
        inputs.append(0)


if p2:
    xmin = xmax = ymin = ymax = 0
    for v in visited:
        if v[0] > xmax:
            xmax = v[0]
        elif v[0] < xmin:
            xmin = v[0]
        if v[1] > ymax:
            ymax = v[1]
        elif v[1] < ymin:
            ymin = v[1]
    newpicture = []
    height = xmax-xmin+1
    width = ymax-ymin+1
    im = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            if (y-ymin,x-xmin) in white:
                im.putpixel((x, y), (255, 255, 255))
            else:
                im.putpixel((x, y), (0,0,0))

    im = im.resize(((ymax-ymin)*100,(xmax-xmin)*100), Image.ANTIALIAS)
    im.save('picture.bmp')
    print("Answer to Part2: Open picture.bmp")
            
else:
    print("Answer to Part 1:", len(visited))

