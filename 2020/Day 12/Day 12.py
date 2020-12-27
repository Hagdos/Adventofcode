f = open('Instructions.txt')

instructions = []
directions = ['E', 'S', 'W', 'N']

currentdirection = 0
location = [0, 0]

for x in f:
    instructions.append(x.strip())


for i in instructions:
    # print(i)
    instruction = i[0]
    if instruction == 'L':
        turn = -int(int(i[1:])/90)
        currentdirection = (currentdirection+turn)%4
    elif instruction == 'R':
        turn = int(int(i[1:])/90)
        currentdirection = (currentdirection+turn)%4
    elif instruction == 'F':
        instruction = directions[currentdirection]
        # print(i)
        
    if instruction == 'N':
        location[0] -= int(i[1:])
    elif instruction == 'S':
        location[0] += int(i[1:])       
    elif instruction == 'W':
        location[1] -= int(i[1:])
    elif instruction == 'E':
        location[1] += int(i[1:])  
    # print(location)
    # print(directions[currentdirection], '\n')
    

print('Solution part 1:')
# print(location)
print(abs(location[0])+abs(location[1]))
print()
        
        
    # ----------------- Part 2 ---------------------
    
currentdirection = 0
location = [0, 0]
waypoint = [-1, 10]
waypointn = [0,0]

for i in instructions[:]:
    print(i)
    instruction = i[0]
    
    if instruction == 'N':
        waypoint[0] -= int(i[1:])
    elif instruction == 'S':
        waypoint[0] += int(i[1:])       
    elif instruction == 'W':
        waypoint[1] -= int(i[1:])
    elif instruction == 'E':
        waypoint[1] += int(i[1:]) 
    
    elif instruction == 'L':
        turn = int(int(i[1:])/90)
        for z in range(turn):
            waypointn[0] = -waypoint[1]
            waypointn[1] = waypoint[0]
            waypoint = waypointn[:]
    elif instruction == 'R':
        turn = int(int(i[1:])/90)
        for z in range(turn):
            waypointn[0] = waypoint[1]
            waypointn[1] = -waypoint[0]
            # print(waypoint,waypointn)
            waypoint = waypointn[:]    

    elif instruction == 'F':
        for z in range(int(i[1:])):
            location[0] += waypoint[0]
            location[1] += waypoint[1]
        
 
    print('Waypoint = ', waypoint, 'Location = ', location, '\n')
    # print(waypoint, '\n')

    
    
print(location)
print(abs(location[0])+abs(location[1]))








# t = -times[validIDs[0]]
# solution = False
# start = time.time()
# while not solution and t<100000000000:
#     t+=validIDs[0]
#     # print(t)
#     for ID in validIDs[:]:
#         # print(ID, t+times[ID], (t+times[ID])%ID)
#         if (t+times[ID])%ID !=0:
#             # print('Break')
#             break
#         elif ID == validIDs[-1]:
#             solution = True
#             print('Solutionfound')
#             print(solution)
#             break