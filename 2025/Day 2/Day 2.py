import pyperclip

def invalid_generator(startingnumber, endnumber, repetitions=2):

    startingnumberstr = str(startingnumber)

    # Check for odd-length numbers:
    while len(startingnumberstr) % repetitions:
        startingnumberstr = str(10**(len(startingnumberstr)))

    invalid_number = int(startingnumberstr[:len(startingnumberstr)//repetitions])

    if double_number(invalid_number, repetitions) < startingnumber:
        invalid_number += 1
    
    d = double_number(invalid_number, repetitions)
    while d <= endnumber:
        yield d
        invalid_number += 1
        d = double_number(invalid_number, repetitions)
    
    return 0

def double_number(number, repetitions):
    return int(str(number)*repetitions)


file = open('2025/Day 2/input.txt').readline().strip().split(',')

data = [tuple(int(i) for i in x.split('-')) for x in file]
ans1 = ans2 = 0

for d in data:
    ans1 += sum(invalid_generator(d[0], d[1]))

    numbers = set()
    for r in range(2, len(str(d[1]))+1):
        numbers.update(set(invalid_generator(d[0], d[1], r)))
    ans2 += sum(list(numbers))


print('The answer to part 1: ', ans1)
pyperclip.copy(ans2)
print('The answer to part 2: ', ans2)


# New issue; Numbers will be found twice (like 222222)