def printScreen(screen):
    printscreen = []
    for line in screen:
        printline = []
        for position in line:
            if position:
                printline.append('#')
            else:
                printline.append(' ')
        printline = ''.join(printline)
        printscreen.append(printline)
        print(printline)
    return printscreen

def rect(screen, x, y):
    for j in range(y):
        for i in range(x):
            screen[j][i] = True
            
    return screen

def shiftRow(screen, lineNumber, dx):
    newline = screen[lineNumber][-dx:] +  screen[lineNumber][:-dx]
    screen[lineNumber] = newline
    
    return screen
               
def shiftColumn(screen, columnNumber, dy):
    newColumn = []
    for line in range(len(screen)):
        newColumn.append(screen[line-dy][columnNumber])
    
    for line in range(len(screen)):
        screen[line][columnNumber] = newColumn[line]
        
    return screen

# =============================================================================
# Create empty screen. False = off, True = on
# =============================================================================
size = (50, 6)

screen = []
for i in range(size[1]):
    screen.append([False]*size[0])

# =============================================================================
# Walk through instruction list
# =============================================================================
file = open('input.txt')

for line in file:
    line = line.strip().split()
    
    if line[0] == 'rect':
        (x,y) = line[1].split('x')
        screen = rect(screen, int(x), int(y))
    
    elif line[0] == 'rotate':
        ID = int(line[2][2:])
        delta = int(line[4])
        
        if line[1] == 'row':
            screen = shiftRow(screen, ID, delta)
        elif line[1] == 'column':
            screen = shiftColumn(screen, ID, delta)
        else:
            raise ValueError
    else:
        raise ValueError
        
answer1 = 0
for line in screen:
    answer1 += sum(line)
    
print('The answer to part 1:', answer1, '\n')

print('The answer to part 2:\n')
printScreen(screen)

