# Read input

f = open('XMAS.txt')
psize = 25
D = []

for x in f:
    D.append(int(x))
    
# Check for wrong numbers:

    
def checknumber(D, i, psize):
    pre = D[i-psize:i]
    for j in pre:
        if j<D[i]/2:
            if D[i]-j in pre:
                return 0
    return D[i]

for i in range(psize,len(D)):
    if(checknumber(D, i, psize)):
        weak = D[i]
        # print(weak)

# -- Part 2 --

for i in range(len(D)):
    total = 0
    j = i
    while total<weak:
        total += D[j]
        
        if total == weak:
            print(i,j)
            print(D[i])
            print(D[j])
            print(min(D[i:j])+max(D[i:j]))
            break
        j+=1

