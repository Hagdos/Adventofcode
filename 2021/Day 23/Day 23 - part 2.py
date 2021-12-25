import heapq
from copy import deepcopy
import time

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
        print('The answer to part 2:', energy)
        heapq.heappush(heads, (energy, rooms, hall))
        return heads, seen, True
    
    # If in seen; continue. Else; add to seen (not energy; only rooms/hall)
    seenstatus = (tuple((tuple(r) for r in rooms)), ''.join(hall))
    if seenstatus in seen:
        return heads, seen, False
    seen.add(seenstatus)
    
    # Check if anything from the hall can go into the right room
    newhead = checkHall(energy, rooms, hall)
    # If so; do so; add that to heap; continue
    if newhead:
        heapq.heappush(heads, newhead)
        return heads, seen, False

    # Check if anything from the rooms can go into the right room
    newhead = checkRooms(energy, rooms, hall)
    # If so; do so; add that to heap; continue
    if newhead:
        heapq.heappush(heads, newhead)
        return heads, seen, False
    
    # Create list of new states:
    # From each room; pick the top pod, and put it on all possible positions
    newheads = exitRooms(energy, rooms, hall)
    # Add all states to heap
    for newhead in newheads:
        heapq.heappush(heads, newhead)
    return heads, seen, False


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
            if any(rightroom[p] != room for p in rooms[room]):  # Todo: Check for all pods still in the room
                roomposition = roomPosition(room)
                left, right = findRange(roomposition, positions)
                if checkRoomAvailable(pod, left, right, rooms):
                    nrooms, nhall = newState(rooms, hall)
                    energy += (5 - len(nrooms[room])) * cost[pod]
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
            if any(rightroom[p] != room for p in rooms[room]):  # Todo: Check for all pods still in the room
                roomposition = roomPosition(room)
                left, right = findRange(roomposition, positions)
                for position in range(left, right):
                    if position not in (2, 4, 6, 8):
                        nrooms, nhall = newState(rooms, hall)
                        distance = 5 - len(nrooms[room]) + abs(position - roomposition)
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
    
    distance = abs(position - roomposition) + 5 - len(rooms[room])
    energy += distance * cost[pod]
        
    return energy, rooms, hall

# Return a deepcopy of rooms and hall
def newState(rooms, hall):
    return deepcopy(rooms), deepcopy(hall)

def roomPosition(room):
    return (room+1)*2

def finished(rooms):
    for r, room in enumerate(rooms):
        if len(room) != 4:
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
rooms = [['D', 'D', 'D', 'B'], ['C', 'C', 'B', 'C'], ['A', 'B', 'A', 'D'], ['B', 'A', 'C', 'A']]
hall = list('...........')
energy = 0

status = (energy, rooms, hall)
heads = [status]
seen = set()

start = time.time()

found = False
while not found:   # Until energy of top of the heap > energy of found solution
    heads, seen, found = step(heads, seen)

    
print(f'Time taken is: {time.time()-start}')