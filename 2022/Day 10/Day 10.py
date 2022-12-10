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
        row = []
        for h in range(0, 40):
            if sprite[v+h] in [h-1, h, h+1]:
                row.append('█')
            else:
                row.append(' ')
        screen.append(''.join(row))

    for row in screen:
        print(row)

    return screen


file = open('input.txt').readlines()

instructions = [x.strip().split() for x in file]

regx = runInstructions(instructions)
signalstrength = calcSignalStrength(regx)
ans1 = sum([signalstrength[i] for i in range(20, 221, 40)])

drawScreen(regx)

print('The answer to part 1: ', ans1)
# print(len(regx), len(signalstrength))
# print('The answer to part 2: ', ans2)
