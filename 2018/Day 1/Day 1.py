file = open('2018/Day 1/input.txt').readlines()
data = [int(x.strip()) for x in file]

print(f'The answer to part 1: {sum(data)}')

frequencies = set()

frequency = 0
i = 0
while True:
    if frequency in frequencies:
        print(f'The answer to part 2: {frequency}')
        break
    frequencies.add(frequency)

    frequency += data[i]
    i += 1
    i %= len(data)
