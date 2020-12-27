import re
import time

f = open('math.txt')
equations = []

equations = open('math.txt').read().splitlines()

for x in f:
    equations.append(x.strip().replace(' ',''))

def solve(eq):
    regex = '\([^\(]*?\)'
    while '(' in eq:
        s = re.findall(regex, eq)
        eq = eq.replace(s[0], solve(s[0][1:-1]))
    regex2 = '(\d+)(\*|\+)(\d+)'
    while '*' in eq or '+' in eq:
        s = re.findall(regex2, eq)
        if s[0][1] == '+':
            a = str(int(s[0][0]) + int(s[0][2]))
        elif s[0][1] == '*':
            a = str(int(s[0][0]) * int(s[0][2]))
        eq = eq.replace(''.join(s[0]), a, 1)
    return eq
        
start = time.time()

ans = 0
for x in equations:
    # print('Equation: ',x)
    a = int(solve(x))
    # print(a)
    ans+= a

print('Answer Part 1: ', ans - 1408133923393)
print('It took: ', time.time()-start, ' seconds')

# ------------------- Part 2 --------------------

def solve2(eq):
    regex = '\([^\(]*?\)'
    while '(' in eq:
        # print(eq)
        s = re.findall(regex, eq)
        eq = eq.replace(s[0], solve2(s[0][1:-1]))
    regexp = '(\d+)(\+)(\d+)'
    regexm = '(\d+)(\*)(\d+)'
    while '+' in eq:
        # print(eq)
        s = re.findall(regexp, eq)
        a = str(int(s[0][0]) + int(s[0][2]))
        eq = eq.replace(''.join(s[0]), a, 1)   
    while '*' in eq:
        # print(eq)
        s = re.findall(regexm, eq)
        a = str(int(s[0][0]) * int(s[0][2]))
        eq = eq.replace(''.join(s[0]), a, 1)  
    return eq
        
ans = 0
for x in equations:
    # print('Equation: ',x)
    a = int(solve2(x))
    # print(a)
    ans+= a

print('Answer Part 2: ', ans - 314455761823725)

























