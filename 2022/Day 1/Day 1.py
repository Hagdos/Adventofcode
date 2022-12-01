file = open('2022/Day 1/input.txt').read()

data = sorted([sum([int(food) for food in elf.split()]) for elf in file.split('\n\n')], reverse=True)

print('The answer to part 1: ', data[0])
print('The answer to part 2: ', sum(data[0:3]))
