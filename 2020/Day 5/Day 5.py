f = open('Tickets.txt')

maxID = 0
IDs = []
for x in f:
    loc = [0]*10
    # print(x)
    j = 0
    for i in x[0:10]:
        if i == 'F' or i == 'L':
            loc[j] = 0
        else:
            loc[j] = 1
        j+=1
    # print(loc)
    
    loc.reverse()
    
    j = 0
    ID = 0
    for i in loc:
        ID = ID+(i<<j)
        j+=1
    IDs.append(ID)
    maxID = max(IDs)
    
print(maxID)
    
# ---- Part 2 ---

IDs.sort()

for i in range(len(IDs)-1):
    if IDs[i+1]-IDs[i]-1:
        print(i)
        print(IDs[i])
    

    
