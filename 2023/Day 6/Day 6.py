def abcformula(a, b, c):
    D = b**2-4*a*c
    a1 = (-b-D**0.5)/(2*a)
    a2 = (-b+D**0.5)/(2*a)

    return (a1, a2)

file = open('input.txt').readlines()
ans1 = ans2 = 1
data = [x.strip().split() for x in file]

# Part 1
races = zip((int(t) for t in data[0][1:]), (int(d) for d in data[1][1:]))

for time, distance in races:
    times = abcformula(1, -time, distance)
    ans1 *= int(times[1]) - int(times[0])

# Part 2
time = int(''.join(data[0][1:]))
distance = int(''.join(data[1][1:]))

times = abcformula(1, -time, distance)
ans2 = int(times[1]) - int(times[0])

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
