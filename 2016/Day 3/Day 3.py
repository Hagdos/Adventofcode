file = open('input.txt')

correctTriangles = 0

for line in file:
    sides = line.strip().split()
    sides = [int(side) for side in sides]
    
    if max(sides) < sum(sides)-max(sides):
        correctTriangles += 1
        
print('Answer to part 1: ', correctTriangles)

# =============================================================================
# Part 2
# =============================================================================

file = open('input.txt').read().split()

triangles = file[::3] + file[1::3] + file[2::3]
correctTriangles = 0

for i in range(0, len(triangles), 3):
    sides = [int(triangles[i]), int(triangles[i+1]), int(triangles[i+2])]
    
    if max(sides) < sum(sides)-max(sides):
        correctTriangles += 1
        
print('Answer to part 2: ', correctTriangles)