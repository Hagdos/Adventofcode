import computer

file = open('Day 18/input.txt').readlines()
instructions = [x.strip().split() for x in file]

# Create list of registernames (letters)
registernames = set()
for line in instructions:
    if line[1].isalpha():
        registernames.add(line[1])

# Part 1
computer0 = computer.Computer(registernames, instructions)
print('The answer to part 1:', computer0.run1())

# Part 2
computer0 = computer.Computer(registernames, instructions)
computer1 = computer.Computer(registernames, instructions)

computer1.registers['p'] = 1

while True:
    computer0.run2(computer1.queue)
    computer1.run2(computer0.queue)

    if not computer1.queue and not computer0.queue:
        print('The answer to part 2:', computer1.registers['Counter'])
        break
