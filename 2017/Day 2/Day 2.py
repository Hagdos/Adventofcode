file = open('input.txt').readlines()

data = [x.strip().split() for x in file]

data = [[int(x) for x in line] for line in data]

ans1 = 0
ans2 = 0

for line in data:
    ans1 += max(line) - min(line)

# =============================================================================
# Part 2
# =============================================================================
    
    for value1 in line:
        for value2 in line:
            if value1 % value2 == 0 and value1 != value2:
                ans2 += value1 // value2
                break

print('The answer to part 1:', ans1)
print('The answer to part 2:', ans2)