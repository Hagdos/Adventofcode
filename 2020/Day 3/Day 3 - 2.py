fname = 'Trees.txt'
f = open(fname)

slopes = [1, 3, 5, 7]
length = len(f.readline())-1
print length

answer = 1

for s in slopes:
    loc = 0
    total = 0
    f = open(fname)
    for x in f:
        if x[loc] == '#':
            total += 1
    ##        print total

        loc = (loc+s)%length
    print total
    answer = answer * total


loc = 0
total = 0
f = open(fname)
i=1
for x in f:
    if i%2:
        if x[loc] == '#':
            total += 1
    ##        print total

        loc = (loc+1)%length
    i+=1    
print total

answer = answer*total

print answer
