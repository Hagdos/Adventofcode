file = open('input.txt').readlines()
data = [x.strip().split(' ') for x in file]
ans1 = ans2 = 0

dots = set()

for i, line in enumerate(data):
    if line == ['']:
        break
    dots.add(tuple(int(i) for i in line[0].split(',')))

for j, line in enumerate(data[i+1:]):
    a = line[2].split('=')
    fold = int(a[1])
    print(a)
    # Check dimension
    if a[0] == 'x':
        dim = 0
    else:
        dim = 1
    
    # Add dots to the folded paper
    newdots = set()
    for dot in dots:
        if dot[dim] < fold:
            newdots.add(dot)
        elif dot[dim] > fold:
            nd = list(dot)
            nd[dim] = -dot[dim]+2*fold
            newdots.add(tuple(nd))
    dots = newdots

    if j == 0:
        print('The answer to part 1: ', len(dots))

    

print('The answer to part 2: ')
for y in range(6):
    newline = []
    for x in range(39):
        if (x,y) in dots:
            newline.append('#')
        else:
            newline.append('.')
    print(''.join(newline))
    
