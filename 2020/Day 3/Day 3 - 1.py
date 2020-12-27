f = open("Trees.txt")

loc = 0
total = 0

for x in f:
##    print x
##    print loc
##    print x[loc]
    if x[loc] == '#':
        total += 1
##        print total

    loc = (loc+3)%31

print total
