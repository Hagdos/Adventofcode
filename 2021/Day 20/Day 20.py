def printImage(img):
    for line in img:
        pline = []
        for r in line:
            if r:
                pline.append('#')
            else:
                pline.append(' ')
        print(''.join(pline))
    print('-')

def countPixels(img):
    ans = 0
    for row in img:
        for c in row:
            ans += c
    return ans

def calcPixel(r, c, img, a):
    factor = 8
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if 0 <= r+dr < len(img) and 0 <= c+dc < len(img[r]):
                n += img[r+dr][c+dc] * (2**factor)
            elif a:
                n += (2**factor)
                
                # print(r, c, img[r][c], n)
            factor -= 1
    return n

file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

img = []
for line in data:
    l = []
    for char in line:
        if char == '#':
            l.append(1)
        else:
            l.append(0)
    img.append(l)
    
decode = img.pop(0)
img.pop(0)

for counter in range(2):
    print(counter)
    # Pad zeroes or ones
    a = counter%2
    img = [[a]*len(img)] + img + [[a]*len(img)]
    for i in range(len(img)):
        img[i] = [a] + img[i] + [a]

    newimg = []
    for r in range(len(img)):
        newimg.append([None] * len(img))
        for c in range(len(img[r])):
            binary = calcPixel(r,c, img, a)
            newimg[r][c] = decode[binary]
    img = newimg
      
    if counter == 1:
        print(f'The answer to part 1: {countPixels(img)}')
print(f'The answer to part 2: {countPixels(img)}')