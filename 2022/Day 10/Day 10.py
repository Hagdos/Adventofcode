def calcSignalStrength(reg):
    ans = [0]*len(reg)
    for i, r in enumerate(reg):
        ans[i] = reg[i] * i

    return ans


def runInstructions(instructions):
    regx = [1, 1]

    for i in instructions:
        if i[0] == 'noop':
            regx.append(regx[-1])
        elif i[0] == 'addx':
            regx.append(regx[-1])
            regx.append(regx[-1]+int(i[1]))

    return regx


def drawScreen(sprite):
    screen = []
    for v in range(1, 240, 40):
        for h in range(0, 40):
            if sprite[v+h] in [h-1, h, h+1]:
                screen.append('█')
            else:
                screen.append(' ')
        screen.append('\n')

    return ''.join(screen)


file = open('input.txt').readlines()

instructions = [x.strip().split() for x in file]

regx = runInstructions(instructions)
signalstrength = calcSignalStrength(regx)
ans1 = sum([signalstrength[i] for i in range(20, 221, 40)])



print('The answer to part 1: ', ans1)
# print(len(regx), len(signalstrength))
print('The answer to part 2: \n')
print(drawScreen(regx))
