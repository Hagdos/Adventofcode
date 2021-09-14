number = 265149
# number = 810

def printmem(mem):
    for line in mem:
        string = [f'{x: 4d}  ' for x in line]
        print(''.join(string))

# Ring number. Middle is ring number 0; ring number 1 has 8 spots (2 - 8)
ringnumber = 0
endsquare = 1
values = [1]

while endsquare < number:
    # Move to the next ring. The first square of this ring is one higher than 
    # the highest square number of the previous ring.
    ringnumber += 1
    startsquare = endsquare + 1
    
    # Determine the dimensions and endsquare of this ring
    side_length = ringnumber * 2
    ring_size = ringnumber * 2 * 4
    endsquare = startsquare + ring_size - 1
    
    # Check if our number is in this ring
    if startsquare <= number <= endsquare:
        # The total number of steps is the number of steps to get to the middle
        # of the side it is in; plus the ringnumber (to get from the side to square 1)
        
        # Number of steps from position to the middle
        dataposition = (number - startsquare)%side_length
        middleposition = side_length//2 - 1
        middlesteps = abs(dataposition - middleposition)
        
        print('The answer to part 1: ', middlesteps + ringnumber)
      
# =============================================================================
# Part 2
# =============================================================================
        
memsize = 11
midpoint = memsize//2

x = y = memsize//2

dx = 1
dy = 0
mem = [[0]*memsize for _ in range(memsize)]

value = 1
mem[y][x] = value

# Keep filling squares until the value is larger than the given input
while value < number:
    # Go to the next square
    x += dx
    y += dy
    
    # Calculate the sum of the surrounding squares
    value = 0
    for di in [-1,0,1]:
        for dj in [-1, 0, 1]:
            value += mem[y+di][x+dj]
    
    # Fill in the current square
    mem[y][x] = value
    
    #Check if the value to the left is empty
    if mem[y-dx][x+dy] == 0:
        dy, dx = -dx, dy
    
# Show the memory array
printmem(mem)



print('The answer to part 2: ', value)