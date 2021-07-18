def space(x, y, code):
    value = x*x + 3*x + 2*x*y + y + y*y + code
    string = str(bin(value))[2:]
    ones = sum([i=='1' for i in string])
    if ones%2 == 1:
        return '#'
    elif ones%2 == 0:
        return '.'   
    
def printfloorplan(floorplan):
    for y in floorplan:
        print(''.join(y))
    print()
    
def nextStep(position):
    x, y = position
    for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
        if x+dx >= 0 and y+dy >= 0:
            if floorplan[y+dy][x+dx] == '.':
                return (x+dx, y+dy)
    return None
                
def distance(target, position):
    dx = target[0] - position[0]
    dy = target[1] - position[1]
    distance = dx*dx+dy*dy
    return distance

def fillfloorplan(position, char):
    x, y = position
    floorplan[y][x] = char
    
def countvisited(floorplan):
    ans = 0
    for line in floorplan:
        for char in line:
            if char == 'X' or char == '0':
                ans += 1
    print("The answer to part 2: ", ans) 

code = 1362
target = (31, 39)
size = 50

floorplan = [[space(x, y, code) for x in range(size)] for y in range(size)]

position = (1, 1)
floorplan[1][1] = '0'
steps = 0
i = 0
found = False
Pt2 = True

checklist = {position: steps}

while found is False and i < 1000:
    i+= 1
    loweststeps = 10001
    for position in checklist:
        if checklist[position] < loweststeps:
            loweststeps = checklist[position]
            testposition = position
            
    steps = loweststeps + 1
    x, y = testposition
    
    if loweststeps == 50 and Pt2 is True:
        found = True
        countvisited(floorplan)
        break

    newposition = nextStep(testposition)
    if newposition:
        fillfloorplan(newposition, '0')
        dis = distance(target, newposition)
        score = dis//steps
        checklist[newposition] = steps
        if dis == 0 and Pt2 is False:
            print('Answer to part 1:', steps)
            found = True
    else:
        fillfloorplan(testposition, 'X')
        checklist.pop(testposition)
        
printfloorplan(floorplan)