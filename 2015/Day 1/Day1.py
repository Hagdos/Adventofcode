instructions = open('input.txt').read()

floor = 0
part2 = False

for i, character in enumerate(instructions):
    if character == '(':
        floor += 1
    elif character == ')':
        floor -= 1
    else:
        print("Error")
        break
    if floor == -1 and part2 == False:
        print("Answer to part 2: ", i+1)
        part2 = True

print("Answer to part 1: ", floor)