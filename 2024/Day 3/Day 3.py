import re

file = open('input.txt').readlines()

data = ''.join([x.strip() for x in file])

ans1 = ans2 = 0

regex = r"mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don\'t\(\))"

enabled = True

matches = re.findall(regex, data)

for m in matches:
    if m[0]:
        mul = int(m[0])*int(m[1])
        ans1 += mul
        if enabled:
            pass
            ans2 += mul
    if m[2]:
        enabled = True
    if m[3]:
        enabled = False

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
