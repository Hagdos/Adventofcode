import pyperclip

file = open('2025/Day 12/input.txt').readlines()
problems = goodfits = nofits = mightfits = 0
shapes = {}

for line in file:
    line = line.strip()
    if line == '':
        continue
    elif line[1] == ':':
        shapenumber = int(line[0])
        r = 0
        shapes[shapenumber] = 0
    elif 'x'  in line.split()[0]:
        problems += 1
        line = line.split(': ')

        w, h = [int(i) for i in line[0].split('x')]
        gridsize = w*h
        
        totalpackages = sum(int(i) for i in line[1].split())
        tightfitsize = sum((shapes[i] * int(line[1].split()[i]) for i in range(shapenumber+1)))

        if totalpackages <= w//3 * h//3: 
            goodfits += 1
        elif gridsize <= tightfitsize:
            nofits += 1
        else:
            mightfits += 1
            
    else:
        shapes[shapenumber] += sum(1 if c=='#' else 0 for c in line)


print(goodfits, nofits, mightfits)

print('The answer to part 1: ', goodfits)
pyperclip.copy(goodfits)

