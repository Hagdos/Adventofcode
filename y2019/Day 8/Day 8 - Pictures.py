from PIL import Image

f = open('picture.txt')

linesread = f.readline().strip()

width = 25
height = 6

lines = []
pictures = []

for i in range(len(linesread)//width):
    lines.append(linesread[width*i:width*(i+1)])
    
for i in range(len(lines)//height):
    pictures.append(lines[height*i:height*(i+1)])
    
leastzeroes = 100
for picture in pictures:
    zeroes = 0
    for line in picture:
        zeroes += line.count('0')
    if zeroes < leastzeroes:
        leastzeroes = zeroes
        answerpicture = picture
        
ones = 0
twos = 0
for line in answerpicture:
    ones += line.count('1')
    twos += line.count('2')

print('Answer to Part 1:', ones*twos)       
    
# =============================================================================
# Part 2 
# =============================================================================

def fillpixel(h, w, layer):
    if pictures[layer][h][w] != '2':
        newpicture[h].append(pictures[layer][h][w])
    else:
        fillpixel(h, w, layer+1)

newpicture = []
for h in range(height):
    newpicture.append([])

for h in range(height):
    for w in range(width):
        fillpixel(h,w,0)
        

im = Image.new("RGB", (width, height))
for h in range(height):
    for w in range(width):
        color = int(newpicture[h][w])*255
        im.putpixel((w, h), (color, color, color))

im = im.resize((width*100,height*100), Image.ANTIALIAS)
im.save('picture.bmp')
print("Answer to Part2: Open picture.bmp")

