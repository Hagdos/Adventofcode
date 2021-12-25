import heapq
from copy import deepcopy

def printRoom(energy, rooms, hall):
    hall = ''.join(hall)
    print('#############')
    print(f'#{hall}#')
    toplayer = [rooms[i][0] if len(rooms[i]) == 2 else '.' for i in range(4)]
    botlayer = [rooms[i][-1] if rooms[i] else '.' for i in range(4)]
    print(f'###{toplayer[0]}#{toplayer[1]}#{toplayer[2]}#{toplayer[3]}###')
    print(f'  #{botlayer[0]}#{botlayer[1]}#{botlayer[2]}#{botlayer[3]}#  ')
    print('  #########  ')
    print(f'Energy: {energy}')
    print()

def occupiedHall(hall):
    positions = []
    pods = []
    for i, c in enumerate(hall):
        if c != '.':
            pods.append(c)
            positions.append(i)
            
    return pods, positions

def findRange(p, positions):
    # Add the edges; -1 and 11
    positions = [-1] + positions
    positions.append(11)
    
    # Walk through the positionslist until the position is higher
    i = 1
    while p > positions[i]:
        i += 1
        
    left = positions[i-1]+1
    right = positions[i]
    if p == right:
        right = positions[i+1]
    
    return left, right


def step(heads, seen):
    # Get top of the heap
    energy, rooms, hall = heapq.heappop(heads)
    
    # if top of the heap is a finished state; return answer
    if finished(rooms):
        print('The answer to part 1:', energy)
        heapq.heappush(heads, (energy, rooms, hall))
        return heads, None
    
    # If in seen; continue. Else; add to seen (not energy; only rooms/hall)
    seenstatus = (tuple((tuple(r) for r in rooms)), ''.join(hall))
    if seenstatus in seen:
        return heads, seen
    seen.add(seenstatus)
    
    # Check if anything from the hall can go into the right room
    newhead = checkHall(energy, rooms, hall)
    # If so; do so; add that to heap; continue
    if newhead:
        heapq.heappush(heads, newhead)
        return heads, seen

    # Check if anything from the rooms can go into the right room
    newhead = checkRooms(energy, rooms, hall)
    # If so; do so; add that to heap; continue
    if newhead:
        heapq.heappush(heads, newhead)
        return heads, seen
    
    # Create list of new states:
    # From each room; pick the top pod, and put it on all possible positions
    newheads = exitRooms(energy, rooms, hall)
    # Add all states to heap
    for newhead in newheads:
        heapq.heappush(heads, newhead)
    return heads, seen


def checkHall(energy, rooms, hall):
    pods, positions = occupiedHall(hall)
    for i, pod in enumerate(pods):
        left, right = findRange(positions[i], positions)
        if checkRoomAvailable(pod, left, right, rooms):
            nrooms, nhall = newState(rooms, hall)
            energy, nrooms, nhall = moveIntoRoom(pod, positions[i], energy, nrooms, nhall)
            return (energy, nrooms, nhall)
    return None


def checkRooms(energy, rooms, hall):
    _, positions = occupiedHall(hall)
    for room in range(4):
        if rooms[room]:
            pod = rooms[room][0]
            if rightroom[pod] != room:
                roomposition = roomPosition(room)
                left, right = findRange(roomposition, positions)
                if checkRoomAvailable(pod, left, right, rooms):
                    nrooms, nhall = newState(rooms, hall)
                    energy += (3 - len(nrooms[room])) * cost[pod]
                    pod = nrooms[room].pop(0)
                    energy, nrooms, nhall = moveIntoRoom(pod, roomposition, energy, nrooms, nhall)
                    return (energy, nrooms, nhall)       
    return None


def exitRooms(energy, rooms, hall):
    newheads = []
    # From each room; pick the top pod, and put it on all possible positions
    _, positions = occupiedHall(hall)
    for room in range(4):
        if rooms[room]:
            pod = rooms[room][0]
            if rightroom[pod] != room:
                roomposition = roomPosition(room)
                left, right = findRange(roomposition, positions)
                for position in range(left, right):
                    if position not in (2, 4, 6, 8):
                        nrooms, nhall = newState(rooms, hall)
                        distance = 3 - len(nrooms[room]) + abs(position - roomposition)
                        pod = nrooms[room].pop(0)
                        nhall[position] = pod
                        nenergy = energy + distance * cost[pod]
                        newheads.append((nenergy, nrooms, nhall))
    return newheads

# Return True if the right room is open and within the left-right range
def checkRoomAvailable(pod, left, right, rooms):
    room = rightroom[pod]
    roomposition = roomPosition(room)
    if roomposition in range(left, right):
        if all(p == pod for p in rooms[room]):
            return True
    return False

# Move pod out of the hall into a room. Add the correct energy
def moveIntoRoom(pod, position, energy, rooms, hall):
    hall[position] = '.'
    room = rightroom[pod]
    roomposition = roomPosition(room)
    rooms[room].append(pod)
    
    distance = abs(position - roomposition) + 3 - len(rooms[room])
    energy += distance * cost[pod]
        
    return energy, rooms, hall

# Return a deepcopy of rooms and hall
def newState(rooms, hall):
    return deepcopy(rooms), deepcopy(hall)

def roomPosition(room):
    return (room+1)*2

def finished(rooms):
    for r, room in enumerate(rooms):
        if len(room) != 2:
            return False
        
        for pod in room:
            if rightroom[pod] != r:
                return False
    return True

cost = {'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000}

rightroom = {'A': 0,
             'B': 1,
             'C': 2,
             'D': 3}

# Input
rooms = [['D', 'B'], ['C', 'C'], ['A', 'D'], ['B', 'A']]
hall = list('...........')
energy = 0

status = (energy, rooms, hall)
heads = [status]
seen = set()

while True:   # Until energy of top of the heap > energy of found solution
    heads, seen = step(heads, seen)
    if seen == None:
        break




    
# # Messingaroundtext
# # Input
# rooms = [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]
# hall = list('.....B.....')
# energy = 0

# print(finished(rooms))

# printRoom(0, rooms, hall)

# states = exitRooms(energy, rooms, hall)
# for state in states:
#     printRoom(*state)
