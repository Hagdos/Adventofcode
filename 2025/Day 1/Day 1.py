file = open('2025/Day 1/aoc-2025-day-1-challenge-1.txt').readlines()

data = [x.strip() for x in file]
#print(data)
ans1 = ans2 = 0

position = 50

for instruction in data:
    if position == 0:
        ans1 += 1
        if previnstruction[0] == 'L' and instruction[0] == 'R':
            ans2 += 1
        elif previnstruction[0] == 'R' and instruction[0] == 'L':
            ans2 -= 1

    if instruction[0] == 'L':
        position -= int(instruction[1:])
    elif instruction[0] == 'R':
        position += int(instruction[1:])

    # print(position, abs(position//100), position%100)

    ans2 += abs(position//100)
    position %= 100

    previnstruction = instruction

if position == 0:
    ans1 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

# 6796 is too high
# When stopped at 0; it might count double or not at all
