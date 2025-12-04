import pyperclip

def part1(line):
    d1 = max(line[:-1])
    p1 = line.index(d1)

    d2 = max(line[p1+1:])

    return d1*10+d2

# Return the largest digit; given that another d digits are needed after that.
# Also return the remainder of the line.
def find_largest_digit(line, d):
    if d > 0:
        largest_digit = max(line[:-d]) 
    else:
        largest_digit = max(line)
    remaining_line = line[line.index(largest_digit)+1:]
    return largest_digit, remaining_line


def part2(line, length):
    ans = 0
    while length:
        length -= 1
        d, line = find_largest_digit(line, length)
        ans += d * 10**length
    return ans

file = open('2025/Day 3/input.txt').readlines()

data = [[int(i) for i in x.strip()] for x in file]

ans1 = ans2 = 0

for line in data:
    # ans1 += part1(line)
    ans1 += part2(line, 2)
    ans2 += part2(line, 12)

    # assert part1(line) == part2(line, 2), print(line, part1(line),  part2(line, 2))

print(part2([1, 9, 8, 8], 2))


print(part2([1, 4, 9, 9], 2))
print(part2([1, 4, 7, 9], 2))

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
pyperclip.copy(ans2)
