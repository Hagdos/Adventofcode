file = open('inputcopy3.txt').readlines()
data = [x.strip().split() for x in file]
ans1 = ans2 = 0

rules = []

for line in data:
    if line and line[0] == 'rule:':
        rules.append(''.join(line))
print(*rules, sep = '\n')

# Correct answer part 1:
# 12345678901234
# 52926995971999

# 12345678901234
# Correct answer part 2:
# 11811951311485


print('The answer to part 1: ', 52926995971999)
print('The answer to part 2: ', ans2)
