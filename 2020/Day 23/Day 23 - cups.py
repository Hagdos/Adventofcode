import time
from collections import deque
from LL import *
# cups = [2,4,7,8,1,9,3,5,6]
# cups = [3,8,9,1,2,5,4,6,7]
# for _ in range(100):
#     # print(cups)
#     currentloc = 0
#     currentcup = cups[currentloc]
#     # =============================================================================
#     # Pick up cups
#     # =============================================================================
#     pickup = []
#     for _ in range(3):
#         pickup.append(cups.pop(currentloc+1))
#     # =============================================================================
#     # Find destinationcup
#     # =============================================================================
#     destcup = currentcup - 1
#     if destcup <= 0:
#             destcup = 9
#     while destcup in pickup:
#         destcup -= 1
#         if destcup <= 0:
#             destcup = 9     
#     # =============================================================================
#     # Place cups, and move 1 location
#     # =============================================================================
#     destloc = cups.index(destcup)+1
#     cups = cups[1:destloc] + pickup + cups[destloc:] + [cups[0]]
    

# # =============================================================================
# # Set in correct order
# # =============================================================================
# s = cups.index(1)
# cups = cups[s+1:] + cups[:s]
# print(''.join(str(c) for c in cups))


# =============================================================================
# Part 2 
# =============================================================================
size = 1000000
cycles = 100
# cups = [2,4,7,8,1,9,3,5,6] + list(range(10,size+1))
# cups = [3,8,9,1,2,5,4,6,7] + list(range(10,size+1))   # Testcups
# print(cups)
# start = time.time()
# for _ in range(cycles):
#     # currentloc = 0
#     currentcup = cups.pop(0)
#     # =============================================================================
#     # Pick up cups
#     # =============================================================================
    
#     pickup = []
#     for _ in range(3):
#         pickup.append(cups.pop(0))
#     # =============================================================================
#     # Find destinationcup
#     # =============================================================================
#     destcup = currentcup - 1
#     if destcup <= 0:
#             destcup = size
#     while destcup in pickup:
#         destcup -= 1
#         if destcup <= 0:
#             destcup = size     
#     # =============================================================================
#     # Place cups, and move 1 location
#     # =============================================================================
#     destloc = cups.index(destcup)+1
#     cups = cups[0:destloc] + pickup + cups[destloc:]
#     cups.append(currentcup)
#     # print(cups)
# ans1 = cups
# print(time.time()-start)

# =============================================================================
# Attempt 2 - Part 2
# =============================================================================
cups = deque([2,4,7,8,1,9,3,5,6] + list(range(10,size+1)))
index = {}
for i, value in enumerate(cups):
    index[value] = i
    
indexoffset = 0
    
print("2nd try")
start = time.time()
# print(cups)
for _ in range(cycles):
    # =============================================================================
    #     Store number of first cup, and move to end of circle
    # =============================================================================
    # currentcup = cups[0]
    cups.rotate(-1)

    # =============================================================================
    # Find destinationcup and location
    # =============================================================================
    destcup = cups[-1] - 1
    if destcup <= 0:
            destcup = size
    while destcup in [cups[0], cups[1], cups[2]]:
        destcup -= 1
        if destcup <= 0:
            destcup = size     
    destloc = cups.index(destcup)
    # =============================================================================
    # Pick up 3 cups and place in correct position
    # =============================================================================
    for _ in range(3):
        pickup = cups.popleft()
        cups.insert(destloc, pickup)


    # print(cups)
print(time.time()-start)

# =============================================================================
# Check if attempt 2 is equal to attempt 1
# =============================================================================

# for i, c  in enumerate(cups):
#     # print(i,c)
#     assert ans1[i] == c
# print("Sucess")