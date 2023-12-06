def checknumbers(data, r, c):
    neighbours = dict()
    for dr in [-1, 0, 1]:
        if 0 <= r+dr < len(data):
            for dc in [-1, 0, 1]:
                if 0 <= c+dc < len(data[r]):
                    if data[r+dr][c+dc].isdigit():
                        number, column = findfullnumber(data, r+dr, c+dc)
                        neighbours[(r+dr, column)] = number
    return neighbours

def findfullnumber(data, r, c):
    string = ''
    # First go as far left as needed
    while c >= 0 and data[r][c].isdigit():
        c-= 1
    c += 1
    # Then add all characters in the right order
    while c < len(data[r]) and data[r][c].isdigit():
        string += data[r][c]
        c += 1
    return int(string), c

file = open('input.txt').readlines()

data = [x.strip() for x in file]

ans1 = ans2 = 0

# Part 1
validnumbers = dict()
for r, row in enumerate(data):
    for c, char in enumerate(row):
        # Part 1
        if char != '.' and not char.isdigit():
            neighbours = checknumbers(data, r, c)
            validnumbers.update(neighbours)
        # Part 2
            if char == '*':
                if len(neighbours) == 2:
                    n = list(neighbours.values())
                    ans2 += n[0]*n[1]

print('The answer to part 1: ', sum(validnumbers.values()))
print('The answer to part 2: ', ans2)


# 82824352