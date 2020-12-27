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

t = -times[validIDs[0]]
# print(t)

solution = False
start = time.time()
while not solution and t<100000000000:
    t+=validIDs[0]
    # print(t)
    for ID in validIDs[:]:
        # print(ID, t+times[ID], (t+times[ID])%ID)
        if (t+times[ID])%ID !=0:
            # print('Break')
            break
        elif ID == validIDs[-1]:
            solution = True
            print('Solutionfound')
            print(solution)
            break
   
    
    
    # solution = True

print('Time taken: ',time.time()-start)
print(t)
# print(t-1068781)


    

    
    