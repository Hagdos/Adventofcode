import time

cells = []
sn = 4842

for x in range(1, 301):
    ID = x + 10
    line = []
    for y in range(1, 301):
        power = ID * y + sn
        power *= ID
        power = (power % 1000) // 100 - 5
        line.append(power)
    cells.append(line)

maxpower = 0
for x in range(300-2):
    for y in range(300-2):
        power = 0
        for dx in (0, 1, 2):
            for dy in (0, 1, 2):
                power += cells[x+dx][y+dy]

        if power > maxpower:
            maxpower = power
            ans1 = (x+1, y+1)

print(f'The answer to part 1: {ans1[0]},{ans1[1]}')

# =============================================================================
# Part 2
# =============================================================================

start = time.time()

maxpower = -10
for gridsize in range(1, 30):
    for x in range(300-gridsize+1):
        for y in range(300-gridsize+1):
            power = 0
            for dx in range(gridsize):
                for dy in range(gridsize):
                    power += cells[x+dx][y+dy]

            if power > maxpower:
                maxpower = power
                ans2 = (x+1, y+1, gridsize)

print(f'Time: {time.time()-start}')
print(f'The answer to part 2: {ans2}')