import copy
import heapq


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


def roomAvailable(rooms, pod, maxleft, maxright):
    r = rooms[rightroom[pod]]
    return all(p == pod for p in r) and rightroom[pod]*2+1 in range(maxleft, maxright+1)


def exitRoom(energy, rooms, hall):
    newstates = []
    for n, r in enumerate(rooms):
        if r and rightroom[r[0]] != n:
            newhall = hall.copy()
            newrooms = copy.deepcopy(rooms)
            pod = newrooms[n].pop(0)
            # 2 steps if the room is now empty; else 1
            newenergy = energy + (3 - len(r)) * cost[pod]
            loc = (n+1)*2      # Starting location of the pod
            newstates += moveHallway(newenergy, newrooms, newhall, pod, loc)
    return newstates


def moveHallway(energy, rooms, hall, pod, loc):
    newstates = []
    maxleft = 0
    maxright = len(hall)-1
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
    if roomAvailable(rooms, pod, maxleft, maxright):
        newhall = hall.copy()
        newhall[loc] = '.'
        newrooms = rooms.copy()
        newrooms[rightroom[pod]].append(pod)
        newenergy = energy + abs((rightroom[pod]*2 + 1) - loc) * cost[pod]
        newstates.append((newenergy, newrooms, newhall))
        return newstates

    # Else; try all other positions in the hallway
    for p in range(maxleft, maxright+1):
        if p in (2, 4, 6, 8):
            pass
        else:
            newhall = hall.copy()
            newhall[loc] = '.'
            newrooms = rooms.copy()
            newenergy = energy + abs(p-loc) * cost[pod]
            newhall[p] = pod
            newstates.append((newenergy, newrooms, newhall))
    return newstates


def enterRoom(energy, rooms, hall):
    pods = []
    locs = []
    for p, char in enumerate(hall):
        if char != '.':
            pods.append(char)
            locs.append(p)

    maxleft = 0
    for i, pod in enumerate(pods):
        maxright = locs[i+1] if i+1 < len(pods) else len(hall)-1
        if roomAvailable(rooms, pod, maxleft, maxright):
            pass  # TODO: Move to the room; return state
        maxleft = locs[i]

    return energy, rooms, hall

cost = {'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000}

rightroom = {'A': 0,
             'B': 1,
             'C': 2,
             'D': 3}

hall = list('...........')
rooms = [['D', 'B'], ['C', 'C'], ['A', 'D'], ['B', 'A']]
energy = 0
heads = [(energy, rooms, hall)]

for _ in range(2):
    state = heads.pop()
    newheads = enterRoom(*state)
    if newheads == state:
        newheads = exitRoom(*state)
    # Todo: Check roomAvailables before exitRoom. (make entryRoom?)
for h in heads:
    printRoom(*h)

# Issues:
# #############
# #.......D..B#
# ###.#C#A#.###
#   #B#C#D#A#
#   #########
# Energy: 6030

# -> There's no next step; D could move even one more to the right.
# It's not doing that for popping out; so probably something wrong with
# Calculating the right side


# print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans)

#15182 is wrong
