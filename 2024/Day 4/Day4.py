from itertools import product

data = ["MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]

data = [line.strip() for line in open("input.txt")]

charmap = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        charmap[(x,y)] = char
        
ans1 = ans2 = 0

xrange = range(len(data[0]))
yrange = range(len(data))
d1 = [-1, 0, 1]

for x,y in product(xrange,yrange):
    if charmap[(x,y)] == 'X':
        for dx, dy in product(d1, d1):
            try:
                if charmap[(x+dx, y+dy)] == 'M':
                    if charmap[(x+2*dx, y+2*dy)] == 'A':
                        if charmap[(x+3*dx, y+3*dy)] == 'S':
                            ans1 += 1
            except KeyError:
                continue

    if charmap[(x,y)] == 'A':
        try:
            for d in [-1, 1]:
                if charmap[(x+d, y+d)] == "M" and charmap[(x-d, y-d)] == "S":
                    for d in [-1, 1]:
                        if charmap[(x-d, y+d)] == "M" and charmap[(x+d, y-d)] == "S":
                            ans2 += 1

        except KeyError:
            continue


print(ans1, ans2)
