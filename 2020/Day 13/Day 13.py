import time
f = open("Bus.txt")

timestamp = int(f.readline().strip())

IDs = f.readline().split(',')
validIDs = []
for i in IDs:
    if i != 'x':
        validIDs.append(int(i))
    
waittimes = []
for i in validIDs:
    waittimes.append(i - timestamp%i)



# ---------- Part 2 ---------------
times = {}
for i in range(len(IDs)):
    if IDs[i] != 'x':
        IDs[i] = int(IDs[i])
        times[IDs[i]] = i

validIDs.sort()
validIDs.reverse()

start = time.time()

t = -times[validIDs[0]]
stepsize = validIDs[0]
solution = False

found = set()
found.add(validIDs[0])
while not solution and t<10000000000000000:
    t+=stepsize
    # print(stepsize)
    # # print(t)
    for ID in validIDs[1:]:
        # print(ID, t+times[ID], (t+times[ID])%ID)
        if (t+times[ID])%ID !=0:
            # print('Break')
            break
        elif ID not in found:
            found.add(ID)
            stepsize = stepsize*ID
        if ID == validIDs[-1]:
            solution = True
            # print('Solutionfound')
            # print(solution)
            break
   

    
    
    # solution = True

print('Time taken: ',time.time()-start)
print(t)


# print(t-1068781)


    

    
    