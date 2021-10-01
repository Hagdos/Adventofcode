def dense(sparse):
    dense = []
    for block in range(16):
        value = 0
        for element in range(16):
            value = value ^ sparse[block*16+element]

        dense.append('{:02x}'.format(value))
    return dense

def knothash(string):
    lengths = [ord(char) for char in string] + [17, 31, 73, 47, 23]

    turns = 0
    skip = 0
    string = list(range(0, 256))
    for _ in range(64):
        for length in lengths:
            # Flip the first part of the string
            part1 = string[:length]
            part1.reverse()
            string = part1 + string[length:]
    
            # Update the first position:
            jump = (length + skip) % len(string)
            string = string[jump:] + string[:jump]
            skip += 1
    
            # Calculate how far the string has turned:
            turns += jump
    
    # Reverse back to position 0:
    turns = turns % len(string)
    string = string[-turns:] + string[:-turns]
    
    return ''.join(dense(string))
    
def addNeighbours(grid, x, y, groupnumber):
    grid[x][y] = groupnumber
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= (x+dx) < 128 and 0 <= (y+dy) < 128:
            if grid[x+dx][y+dy] == 1:
                addNeighbours(grid, x+dx, y+dy, groupnumber)

ans1 = ans2 = 0

key = open('input.txt').read().strip() + '-'
# key = 'flqrgnkx-'
grid = []

for line in range(128):
    hashinput = key + str(line)
    
    hexhash = knothash(hashinput)
        
    # for char in hexhash:
    binary = bin(int(hexhash, 16))[2:]
    bitlist = [int(b) for b in binary]
    
    # print(binary)
    ans1 += sum(bitlist)
    bitlist = [0] * (128-len(bitlist)) + bitlist
    grid.append(bitlist)
    
groupcounter = 1

for x, line in enumerate(grid):
    for y, bit in enumerate(line):
        if bit == 1:
            groupcounter += 1
            addNeighbours(grid, x, y, groupcounter)


ans2 = groupcounter - 1       
            
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)