# Swap two characters in a string, where two positions are given.
def swapposition(string, x, y):
    charx = string[x]
    chary = string[y]
    return swapchar(string, charx, chary)


# Swap two characters in a string, where two characters are given
def swapchar(string, charx, chary):
    table = string.maketrans(charx+chary, chary+charx)
    return string.translate(table)


# Rotate strings. Positive values rotate left
def rotateposition(string, position):
    position %= len(string)
    return string[position:] + string[:position]


# Rotates the string x positions to the right, where
# x is the index of the given character +1 if index < 4, or +2 if index >= 4
def rotatechar(string, char):
    position = string.find(char)
    if position >= 4:
        position += 2
    else:
        position += 1
    return rotateposition(string, -position)


# Reverse of rotatechar()
def rotatechar2(string, char):
    position = string.find(char)
    if position % 2 == 1:
        position = (position - 1)//2 + 1
    elif position == 0:
        position = 1
    else:
        position = (position + 10)//2
    return rotateposition(string, position)


# Reverse part of the string between positions x and y
def reverse(string, x, y):
    x = -len(string) if x == 0 else x
    flipstring = string[y:x-1:-1]
    return string[:x] + flipstring + string[y+1:]


# Moves the letter at position x to position y
def movechar(string, x, y):
    char = string[x]
    smallstring = string[:x] + string[x+1:]
    return smallstring[:y] + char + smallstring[y:]


file = open('input.txt').readlines()
password = "abcdefgh"

for line in file:
    cmd = line.strip().split()
    if cmd[0] == 'swap':
        if cmd[1] == 'position':
            password = swapposition(password, int(cmd[2]), int(cmd[5]))
        elif cmd[1] == 'letter':
            password = swapchar(password, cmd[2], cmd[5])
    elif cmd[0] == 'rotate':
        if cmd[1] == 'left':
            password = rotateposition(password, int(cmd[2]))
        elif cmd[1] == 'right':
            password = rotateposition(password, -int(cmd[2]))
        elif cmd[1] == 'based':
            password = rotatechar(password, cmd[-1])
    elif cmd[0] == 'reverse':
        password = reverse(password, int(cmd[2]), int(cmd[4]))
    elif cmd[0] == 'move':
        password = movechar(password, int(cmd[2]), int(cmd[5]))
    else:
        print("Unknown command:")
        print(cmd)

print('Answer to Part 1:', password)

# Part 2

password = "fbgdceah"
file = open('input.txt').readlines()

for line in file[::-1]:
    cmd = line.strip().split()
    if cmd[0] == 'swap':
        if cmd[1] == 'position':
            password = swapposition(password, int(cmd[2]), int(cmd[5]))
        elif cmd[1] == 'letter':
            password = swapchar(password, cmd[2], cmd[5])
    elif cmd[0] == 'rotate':
        if cmd[1] == 'left':
            password = rotateposition(password, -int(cmd[2]))
        elif cmd[1] == 'right':
            password = rotateposition(password, int(cmd[2]))
        elif cmd[1] == 'based':  # TODO Reverse this bitch
            password = rotatechar2(password, cmd[-1])
    elif cmd[0] == 'reverse':
        password = reverse(password, int(cmd[2]), int(cmd[4]))
    elif cmd[0] == 'move':
        password = movechar(password, int(cmd[5]), int(cmd[2]))
    else:
        print("Unknown command:")
        print(cmd)

print('Answer to Part 2:', password)
