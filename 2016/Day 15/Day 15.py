file = open('input.txt').readlines()

discs = []

Pt2 = True

for number, line in enumerate(file):
    line = line.split()
    positions = int(line[3])
    startposition = int(line[-1][:-1])
    discs.append((number+1, positions, startposition))
    
if Pt2 is True:
    discs.append((number+2, 11, 0))

start = 0
stepsize = 1

while discs:
    start += stepsize
    for disc in discs[:]:
        number, positions, startposition = disc
        time = start + number
        position = (startposition + time)%positions
        
        if position == 0:
            stepsize *= positions
            discs.remove(disc)

print('The answer is: ', start)



for t in range(100000000):    
    if (11 + (t + 1))%13 == 0:   
        if (0 + (t + 2))%5 == 0:   
            if (11 + (t + 3))%17 == 0:
                if (0 + (t + 4))%3 == 0:
                    if (2 + (t + 5))%7 == 0:
                        if (17 + t + 6)%19 == 0:
                            if (0 + t + 7)%11 == 0:
                                print(t)
                                break