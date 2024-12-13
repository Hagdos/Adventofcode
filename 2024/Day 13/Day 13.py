def calc(Ax, Ay, Bx, By, X, Y):
    # Maths!
    A1 = (X*By - Bx*Y)
    A2 = (Ax*By - Ay*Bx)

    B1 = (Y*Ax - Ay*X)
    B2 = (By*Ax - Bx*Ay)

    if A1 % A2 or B1 % B2:
        return 0

    A = A1//A2
    B = B1//B2

    return 3*A + B


file = open('input.txt').read().split("\n\n")

data = [x.strip().split() for x in file]
ans1 = ans2 = 0

for claw in data:
    Ax = int(claw[2][2:-1])
    Ay = int(claw[3][2:])
    Bx = int(claw[6][2:-1])
    By = int(claw[7][2:])
    X = int(claw[9][2:-1])
    Y = int(claw[10][2:])

    ans1 += calc(Ax, Ay, Bx, By, X, Y)

    X = X + 10000000000000
    Y = Y + 10000000000000

    ans2 += calc(Ax, Ay, Bx, By, X, Y)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

