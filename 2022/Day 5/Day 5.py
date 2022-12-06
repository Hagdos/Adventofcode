def printStacks(stacks):
    for i, s in enumerate(stacks):
        print(i, s)


file = open('2022/Day 5/input.txt').read()

stackinput, instructions = file.split('\n\n')
stackinput = stackinput.split('\n')
ans = []
part1 = True

stacks = [[] for _ in range(9)]
for line in stackinput[:-1]:
    print(line)
    for i, s in enumerate(stacks):
        if line[1+i*4] != ' ':
            s.append(line[1+i*4])

[s.reverse() for s in stacks]

for instr in instructions.strip().split('\n'):
    [amount, source, goal] = [int(word) for word in instr.split(' ') if word.isdigit()]
    # printStacks(stacks)
    if part1:
        moved = stacks[source-1][-amount:]
        moved.reverse()
        stacks[goal-1] += moved
        stacks[source-1] = stacks[source-1][:-amount]
    else:
        stacks[goal-1] += stacks[source-1][-amount:]
        stacks[source-1] = stacks[source-1][:-amount]

for s in stacks:
    ans.append(s[-1])

print('The answer to part 1: ', ''.join(ans))
print('JRVNHHCSJ')
