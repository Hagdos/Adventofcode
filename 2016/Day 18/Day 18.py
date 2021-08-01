import time

line = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.' 

# line = '.^^.^.^^^^'

size = len(line)
rows = 40
# For part 2:
rows = 400000

rows = 20000

lastline = [x == '^' for x in line]

ans = 0

start = time.time()

for _ in range(rows-1):
    newline = []    
    newline.append(lastline[1])
    for i in range(1,size-1):
        newline.append(lastline[i-1] ^ lastline[i+1])        
    newline.append(lastline[-2])
            
    ans += sum(newline)
    
    lastline = newline
  
 
print(time.time()-start)
print('The answer to part 1 or 2:', ans)