solutions = {}
def solveTowels(instruction, towels):

    if instruction == '':
        return 1

    elif instruction in solutions:
        return solutions[instruction]

    print(f'Instr: {instruction}')

    possibleOptions = 0

    for towel in towels:
        if towel == instruction[:len(towel)]:
            possibleOptions += solveTowels(instruction[len(towel):], towels)

    solutions[instruction] = possibleOptions

    return possibleOptions


file = open('input.txt').read()

towels, instructions = file.split('\n\n')

towels = towels.split(', ')
instructions = instructions.split()
ans1 = ans2 = 0



for instruction in instructions:
    print(instruction)
    a = solveTowels(instruction, towels)
    ans2 += a
    if a:
        ans1 += 1


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
