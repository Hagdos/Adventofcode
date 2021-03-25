commands = open('input.txt')
connections = dict()

for cmd in commands:
    cmd = cmd.strip().split(' -> ')
    connections[cmd[1]] = cmd[0].split(' ')
    
    
#Iterative function; start at a and work down until you find a wire with a value on it.

