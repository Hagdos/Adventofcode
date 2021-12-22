def calcOverlap(r1, r2):
    if any(r2[d][1] < r1[d][0] or r2[d][0] > r1[d][1] for d in range(3)):
        return 0
    else:
        overlap = 1
        for dim in range(3): # Calculate the overlap for each dimension. Total overlap is the 3 dimensions multiplied
            if r2[dim][0] in range(r1[dim][0], r1[dim][1]+1):
                pass
    # This won' 

file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

on = set()
boxes = []

for line in data:
    cmd, coords = line.split(' ')
    ranges = coords.split(',')
    ranges = [tuple(int(i) for i in x[2:].split('..')) for x in ranges]
    boxes.append((cmd, ranges))
    
sboxes = boxes[:20]
    
i = 0
for i, (cmd, ranges) in enumerate(sboxes):
    if cmd == 'on':
        size = [r[1] - r[0] for r in ranges]
        size = size[0]*size[1]*size[2]
        for _, r2 in sboxes[i+1:]:
            size -= calcOverlap(ranges, r2)
        
        ans2 += size
        
        
        
        
        
        
    # else:
    #     i = 0
    #     for cmd2, ranges2 in boxes:
    #         if ranges != ranges2:
    #             if all((ranges2[r][0] < ranges[r][0] < ranges2[r][1] or ranges2[r][0] < ranges[r][1] < ranges2[r][1]) for r in range(3)):
    #                 i+= 1
    #                 if any((ranges2[r][0] < ranges[r][0] < ranges2[r][1] and ranges2[r][0] < ranges[r][1] < ranges2[r][1]) for r in range(3)):
    #                     print(cmd, ranges)
    #                     print(cmd2, ranges2)
    #                     print()
                    
                    
                    
                    
        print(i)




    #     print(cmd, ranges)
    #     for x in range(ranges[0][0], ranges[0][1]+1):
    #         for y in range(ranges[1][0], ranges[1][1]+1):
    #             for z in range(ranges[2][0], ranges[2][1]+1):
    #                 if cmd == 'on':
    #                     on.add((x, y, z))
    #                 else:
    #                     on.discard((x, y, z))
    

print('The answer to part 1: ', len(on))
print('The answer to part 2: ', ans2)
