import itertools

def flash(data, x, y):
    data[x][y] = 0
    flashes = 1
    for (nx, ny) in findNeighbours(x, y):
        if nx in range(10) and ny in range(10):
            if data[nx][ny]:
                data[nx][ny] += 1
                if data[nx][ny] > 9:
                    flashes += flash(data, nx, ny)
    
    return flashes
        

def findNeighbours(x, y):
    for dx, dy in itertools.product((-1, 0, 1), repeat=2):
        if dx or dy:
            yield x+dx, y+dy
    
    
file = open('input.txt').readlines()
data = [[int(i) for i in line.strip()] for line in file]
ans1 = ans2 = 0


flashes = 0
for i in range(1,1000):
    newflashes = 0
    for x, y in itertools.product(range(10), repeat=2):
        data[x][y] += 1
    
    for x, y in itertools.product(range(10), repeat=2):
        if data[x][y] > 9:
            newflashes += flash(data, x, y)
        
    flashes += newflashes
    if i == 100:
        print('The answer to part 1: ', flashes)
        
    if newflashes == 100:
        print('The answer to part 2: ', i)
        break
    
    # print('Step:', i)
    # print(*data, sep='\n')
    # print()
