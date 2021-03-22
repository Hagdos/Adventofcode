dimensions = open('input.txt')

totalWrapping = 0
totalRibbon = 0

for present in dimensions:
    lengths = present.strip().split('x')
    lengths = list(map(int, lengths)) #Convert to integers
    lengths.sort()
    
    areas = [lengths[0]*lengths[1], lengths[0]*lengths[2], lengths[1]*lengths[2]]
    
    wrappingNeeded = 3*areas[0]+2*areas[1]+2*areas[2]
    totalWrapping += wrappingNeeded
    
    ribbonNeeded = 2*lengths[0]+2*lengths[1]+lengths[0]*lengths[1]*lengths[2]
    totalRibbon += ribbonNeeded
    
print('Answer to part 1:', totalWrapping)
print('Answer to part 2:', totalRibbon)
