import regex as re
import matplotlib.pyplot as plt


def returnlocation(robot, steps):
    xpos, ypos, xspeed, yspeed = robot

    xpos = (xpos + xspeed*steps) % xrange
    ypos = (ypos + yspeed*steps) % yrange

    return xpos, ypos


def part1(robots, steps):
    quadrants = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for robot in robots:
        xpos, ypos = returnlocation(robot, steps)

        if xpos < xrange//2:
            LR = 0
        elif xpos > xrange//2:
            LR = 1
        else:
            LR = 2

        if ypos < yrange//2:
            UD = 0
        elif ypos > yrange//2:
            UD = 1
        else:
            UD = 2

        quadrants[LR][UD] += 1

    ans1 = 1
    for LR in (0, 1):
        for UD in (0, 1):
            ans1 *= quadrants[LR][UD]

    return ans1


def printField(robots):
    row = ""
    for r in range(yrange):

        for c in range(xrange):
            if (c, r) in robots:
                row += "#"
            else:
                row += "."

        row += "\n"
    return row


file = open('input.txt').readlines()

steps = 100
xrange = 101
yrange = 103

ans1 = ans2 = 0
robots = [[int(i) for i in re.findall("-?\d+", robot)] for robot in file]

prevfields = {}


outputfile = open("output2.txt", "w")

sizes = []

for steps in range(xrange*yrange):
    nrobots = {returnlocation(robot, steps) for robot in robots}

    sizes.append(len(nrobots))

    if len(nrobots) == 500:
        print(steps)

    # outputfile.write(f"\nThe field after {steps} steps:\n")
    # outputfile.write(printField(nrobots))

    ans2 += 1



# nrobots = {returnlocation(robot, 6398) for robot in robots}
# print(printField(nrobots))

print('The answer to part 1: ', part1(robots, 100))
print('The answer to part 2: ', 6398)

# 10403 is too high