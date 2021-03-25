def solve(connections, cmd):
    if isinstance(cmd, int) or cmd.isdigit():
        return int(cmd)
    
    signal = connections[cmd]
    if len(signal) == 1:
        solution = solve(connections, signal[0])
    elif signal[0] == 'NOT':
        solution = (65535 - solve(connections, signal[1]))
    elif signal[1] == 'LSHIFT':
        solution = (solve(connections, signal[0]) << int(signal[2]))
    elif signal[1] == 'RSHIFT':
        solution = (solve(connections, signal[0]) >> int(signal[2]))
    elif signal[1] == 'AND':
        solution = (solve(connections, signal[0]) & solve(connections, signal[2]))
    elif signal[1] == 'OR':
        solution = (solve(connections, signal[0]) | solve(connections, signal[2]))
    else:
        print("Unknown command", connections[cmd])
        
    connections[cmd] = [solution]    
    return solution

commands = open('input.txt')
connections = dict()

for cmd in commands:
    cmd = cmd.strip().split(' -> ')
    connections[cmd[1]] = cmd[0].split(' ')

a = solve(connections, 'a')

print('Answer to part 1:', a)

commands = open('input.txt')
connections = dict()

for cmd in commands:
    cmd = cmd.strip().split(' -> ')
    connections[cmd[1]] = cmd[0].split(' ')

connections['b'] = [a]

print('Answer to part 2:', solve(connections, 'a'))