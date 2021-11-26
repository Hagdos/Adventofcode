def printpattern(pattern):
    for line in pattern:
        print(''.join(line))
    print()
        

def inputtopattern(inpattern):
    pattern = []
    line = []
    for char in inpattern:
        if char == '#':
            line.append('1')
        elif char == '.':
            line.append('0')
        else:
            pattern.append(line)
            line = []
    pattern.append(line)
    return pattern


def patterntoint(pattern):
    bitpattern = []
    for l in pattern:
        bitpattern += l
    
    return int(''.join(bitpattern), 2)


def inttopattern(i, length):
    bitpattern = format(i, '016b')[-length**2:]
    pattern = [list(bitpattern[j*length:(j+1)*length]) for j in range(length)]
    return pattern


def rotatepattern(inpattern):
    newpattern = []
    for i, line in enumerate(inpattern):
        newline = [inpattern[len(line)-1-j][i] for j in range(len(line))]
        newpattern.append(newline)
        
    return newpattern


def flippattern(inpattern):
    size = len(inpattern)
    newpattern = []
    for i in range(size):
        newpattern.append(inpattern[size-1-i])
        
    return newpattern


def returnrotations(integer, length):
    integers = [integer]
    patterns = [inttopattern(integer, length)]
    
    for _ in range(3):
        patterns.append(rotatepattern(patterns[-1]))
        integers.append(patterntoint(patterns[-1]))

    patterns.append(flippattern(patterns[-1]))
    integers.append(patterntoint(patterns[-1]))
    
    for _ in range(3):
        patterns.append(rotatepattern(patterns[-1]))
        integers.append(patterntoint(patterns[-1]))

    return integers, patterns


def mergepatterns(largepattern):
    osize = len(largepattern)       # The size of the outer 2D array
    isize = len(largepattern[0][0]) # The size of the inner 2D arrays
    size = osize * isize            # The size of the new 2D array
    p = []
    for line in range(size):
        newline = []
        for column in range(osize):
            for item in largepattern[line//isize][column][line%isize]:
                newline.append(item)
        
        # [item for sublist in p[line//isize][column][line%isize] for item in sublist]
        p.append(newline)
        
    return p


file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
iterations = 18

#Add the inputs to the libraries
patternlibrary2 = dict()
for line in data[:6]:
    output = patterntoint(inputtopattern(line[2]))
    inputs = returnrotations(patterntoint(inputtopattern(line[0])), 2)[0]
    for inp in inputs:
        patternlibrary2[inp] = output
        

patternlibrary3 = dict()
for line in data[6:]:
    output = patterntoint(inputtopattern(line[2]))
    inputs = returnrotations(patterntoint(inputtopattern(line[0])), 3)[0]
    for inp in inputs:
        patternlibrary3[inp] = output


# Define the starting pattern
pattern = patternlibrary3[patterntoint(inputtopattern('.#./..#/###'))]
pattern = inttopattern(pattern, 4)
size = 3 * 4 // 3

for _ in range(iterations - 1):  # minus 1; because the first iteration is already in the input

    if size % 2 == 0:   # If the size is evenly divisible by 2, 
        nsquares = size // 2
        newpattern = [[0]*nsquares for _ in range(nsquares)]
        # break the pixels up into 2x2 squares,
        for row in range(nsquares):
            for column in range(nsquares):                
                p = [r[column*2:column*2+2] for r in pattern[row*2:row*2+2]]
                # and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
                newpattern[row][column] = inttopattern(patternlibrary2[patterntoint(p)], 3)
        
        # Merge patterns into one large pattern
        pattern = mergepatterns(newpattern)
        size = size * 3 // 2

        
            
    elif size % 3 == 0:  # Otherwise, the size is evenly divisible by 3; 
        # break the pixels up into 3x3 squares, 
        nsquares = size // 3
        newpattern = [[0]*nsquares for _ in range(nsquares)]
        # break the pixels up into 2x2 squares,
        for row in range(nsquares):
            for column in range(nsquares):                
                p = [r[column*3:column*3+3] for r in pattern[row*3:row*3+3]]
                # and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
                newpattern[row][column] = inttopattern(patternlibrary3[patterntoint(p)], 4)
        
        # Merge patterns into one large pattern
        pattern = mergepatterns(newpattern)
        size = size * 4 // 3

    else:
        print('Weird')
                
                
        
ans1 = ans2 = 0

for row in pattern:
    for item in row:
        if item == '1':
            ans1 += 1

print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans2)

# 4168414 is too high