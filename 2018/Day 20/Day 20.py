# General idea: Keep a counter of current state, moving it forward by one and state to the list of known rooms.
#
# If there's a '(' or '^' sign, add current location and position to a jumpback list.
# If there's a '|' sign, jump back to the last thing on the jumpback list
# If there's a ')' or $ sign, remove the last thing on the jumpback list.
#
# If the jumpback list is empty, stop.

route = open('2018/Day 20/input.txt').readline().strip()

# State definition: number of steps, x, y
state = [0, 0, 0]
pointer = 0
jumpback = []

rooms = dict()

while pointer < len(route):
    instr = route[pointer]
    if instr in 'NSWE':
        if instr == 'N':
            state[2] -= 1
        elif instr == 'S':
            state[2] += 1
        elif instr == 'W':
            state[1] -= 1
        elif instr == 'E':
            state[1] += 1
        # Add a step to the pathlength, and add it to the list of known rooms
        state[0] += 1
        location = (state[1], state[2])
        if location in rooms.keys():
            if state[0] < rooms[location]:
                rooms[location] = state[0]
        else:
            rooms[location] = state[0]

    elif instr in '^(':
        jumpback.append(state.copy())
    elif instr == '|':
        state = jumpback[-1].copy()
    elif instr in '$)':
        state = jumpback.pop()

    pointer += 1

print(f'The answer to part 1: {max(rooms.values())}')
print(f'The answer to part 2: {sum([x >= 1000 for x in rooms.values()])}')
