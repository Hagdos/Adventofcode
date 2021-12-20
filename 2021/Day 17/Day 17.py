file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
ans1 = ans2 = 0

tx = range(70,125+1)
ty = range(-159, -121+1)
maxsteps = 0

options = set()
options2 = set()
for ySpeedInit in range(min(ty)-2, 200):
    print(ySpeedInit)
    for xSpeedInit in range(max(tx)+1):
        x, y = 0, 0
        yspeed = ySpeedInit
        xspeed = xSpeedInit
        ymax = 0
        while y > min(ty):
            y += yspeed
            x += xspeed
            yspeed -= 1
            xspeed -= 1 if xspeed > 0 else 0
            ymax = max(ymax, y)

            if x in tx and y in ty:
                options.add(ymax)
                options2.add((xSpeedInit, ySpeedInit))
                break

print('The answer to part 1: ', max(options))
print('The answer to part 2: ', len(options2))

# correct answers: 12561 and 3785