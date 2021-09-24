def calcdistance(x, y):
    return abs(x) + (abs(y)-abs(x))//2


file = open('Day 11/input.txt').readlines()

data = file[0].strip().split(',')

posx = 0
posy = 0
maxdistance = 0

for step in data:
    if step == 'n':
        posy += 2
    elif step == 's':
        posy -= 2
    else:
        if step[0] == 'n':
            posy += 1
        elif step[0] == 's':
            posy -= 1
        if step[1] == 'e':
            posx += 1
        elif step[1] == 'w':
            posx -= 1
    distance = calcdistance(posx, posy)
    if distance > maxdistance:
        maxdistance = distance

ans1 = distance
ans2 = maxdistance
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
