instructions = open('input.txt')

lights = [[False for _ in range(1000)] for _ in range(1000)]
brightness = [[0 for _ in range(1000)] for _ in range(1000)]

for line in instructions:
    instruction = line.strip().split(' ')
    corner1 = instruction[-3].split(',')
    corner2 = instruction[-1].split(',')
    
    if instruction[0] == 'toggle':
        toggle = True
    else:
        toggle = False
        if instruction[1] == 'on':
            instruct = True
        elif instruction[1] == 'off':
            instruct = False
    
    
    for x in range(int(corner1[0]), int(corner2[0])+1):
        for y in range(int(corner1[1]), int(corner2[1])+1):
            if toggle == True:
                lights[x][y] ^= True
                brightness[x][y] += 2
            else:
                lights[x][y] = instruct
                if instruct == True:
                    brightness[x][y] += 1
                elif brightness[x][y] > 0:
                    brightness[x][y] -= 1
                
lightsOn = 0
totalBrightness = 0
for x in range(1000):
    for y in range(1000):
        if lights[x][y]:
            lightsOn += 1
        totalBrightness += brightness[x][y]

            
print("Answer to part 1:", lightsOn)

print("Answer to part 2:", totalBrightness)
