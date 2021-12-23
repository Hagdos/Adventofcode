import copy

def roomAvailable(rooms, pod):
    r = rooms[rightroom[pod]]
    return all(p == pod for p in r)


def exitRoom(energy, rooms, hall):
    newstates = []
    for n, r in enumerate(rooms):
        if r and rightroom[r[0]] != n:
            newhall = hall.copy()
            newrooms = copy.deepcopy(rooms)
            pod = newrooms[n].pop(0)
            newenergy = energy + (2 - len(r))*cost[pod] # 2 steps if the room is now empty; else 1
            loc = (n+1)*2      # Starting location of the pod
            
            newstates += moveHallway(newhall, newrooms, pod, loc, newenergy)
            
    return newstates
            
def moveHallway(hall, rooms, pod, loc, energy):
    newstates = []
    
    maxleft = 0
    maxright = len(hall)    # Todo; take a good look at maxright and ranges
    p = 0
    # Determine max steps to the left and right
    while p != loc:
        if hall[p] != '.':
            maxleft = p+1
        p += 1
    for p in range(loc+1, len(hall)):
        if hall[p] != '.':
            maxright = p-1
            break
        
    # First check available rooms
    # If so; create new state if this is the right room and skip other steps
    if roomAvailable(rooms,pod):
        if rightroom[pod]*2+1 in range(maxleft, maxright+1):
            newhall = hall.copy()
            newhall[loc] = '.'
            newrooms = rooms.copy()
            newrooms[rightroom[pod]].append(pod)
            newenergy = energy + abs((rightroom[pod] * 2 + 1) - loc) * cost[pod]
            newstates.append((newrooms, newhall, newenergy))
            return newstates

    # Else; try all other positions in the hallway
    for p in range(maxleft, maxright):
        if p in (2, 4, 6, 8):
            pass
        else:
            newhall = hall.copy()
            newhall[loc] = '.'
            newrooms = rooms.copy()
            newenergy = energy + abs(p-loc) * cost[pod]
            newhall[p] = pod
            newstates.append((newrooms, newhall, newenergy))
    
    return newstates
            

file = open('input.txt').readlines()
data = [x.strip('\n') for x in file]
ans1 = 0

hall = list(data[1][1:-1])

cost = {'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000}

rightroom = {'A': 0,
             'B': 1,
             'C': 2,
             'D': 3}


rooms = [['D', 'B'], ['C', 'C'], ['A', 'D'], ['B', 'A']]

energy = 0

heads = [(energy, rooms, hall)]

state = heads.pop()

heads += exitRoom(*state)

print(heads)


# print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans)

#15182 is wrong