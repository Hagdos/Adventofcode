def getNumber(numbers, monkey):
    if not isinstance(numbers[monkey], int):
        operation = numbers[monkey]
        a = getNumber(numbers, operation[0])
        b = getNumber(numbers, operation[2])
        if operation[1] == '+':
            ans = a + b
        elif operation[1] == '-':
            ans = a - b
        elif operation[1] == '*':
            ans = a * b
        elif operation[1] == '/':
            ans = a // b
        numbers[monkey] = ans

    return numbers[monkey]


def readData(filename):
    file = open(filename).readlines()

    data = [x.strip().split(': ') for x in file]

    numbers = dict()

    for monkey in data:
        if monkey[1].isnumeric():
            numbers[monkey[0]] = int(monkey[1])
        else:
            numbers[monkey[0]] = monkey[1].split()
    return numbers


def part1(filename):
    numbers = readData(filename)
    return getNumber(numbers, 'root')


def part2(filename):
    upperlimit = 0
    lowerlimit = 1
    for _ in range(1000):
        if upperlimit == 0:
            guess = lowerlimit*100
        else:
            guess = lowerlimit + (upperlimit-lowerlimit)//2
        numbers = readData(filename)
        numbers['humn'] = guess
        a, _, b = numbers['root']
        if getNumber(numbers, a) > getNumber(numbers, b):
            lowerlimit = guess
        elif getNumber(numbers, a) < getNumber(numbers, b):
            upperlimit = guess
        elif getNumber(numbers, a) == getNumber(numbers, b):
            return(guess)


print('The answer to part 1: ', part1('2022/Day 21/input.txt'))
print('The answer to part 2: ', part2('2022/Day 21/input.txt'))

# numbers = readData('2022/Day 21/input.txt')
# numbers['humn'] = 3740214169961+0
# a, _, b = numbers['root']
# print(getNumber(numbers, a), getNumber(numbers, b))
