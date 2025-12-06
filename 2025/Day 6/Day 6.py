import pyperclip
import math

file = open('2025/Day 6/input.txt').readlines()

data = [x.strip().split() for x in file]
ans1 = ans2 = 0

# Part 1
for s in range(len(data[0])):
    numbers = (int(i) for i in [d[s] for d in data[:-1]])
    if data[-1][s] == '+':
        ans1 += sum(numbers)
    if data[-1][s] == '*':
        ans1 += math.prod(numbers)

# Part 2

data = file

# Read column per column
for c in range(len(data[0])):

    if not data[-1][c].isspace():   # If there's a symbol at the bottom, we start a new sum/multiplication
        if data[-1][c] == '+':
            multiplication = False
            answer = 0
        elif data[-1][c] == '*':
            multiplication = True
            answer = 1
        else:
            assert False

    number = ''.join(d[c] for d in data[:-1])
    if not number.isspace():
        number = int(number)
        if multiplication:
            answer *= number
        else:
            answer += number
    else:
        ans2 += answer

pyperclip.copy(ans2)
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)