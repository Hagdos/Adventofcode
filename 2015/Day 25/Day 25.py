n = 20151125

multiplier = 252533
divider = 33554393

row = 2981
column = 3075

cycles = sum(range(row+column-1)) + column

for _ in range(cycles-1):
    n = n*multiplier%divider

print('The answer to Part 1:', n)
