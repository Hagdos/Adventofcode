def swap(line, spin):
    return line[-spin:] + line[:-spin]


def exchange(line, A, B):
    if A > B:
        A, B = B, A
    return line[:A] + [line[B]] + line[A+1:B] + [line[A]] + line[B+1:]


def partner(line, A, B):
    A = line.index(A)
    B = line.index(B)
    return exchange(line, A, B)


def naivesolution(line, file):
    for command in file:
        if command[0] == 's':
            line = swap(line, int(command[1:]))
        elif command[0] == 'x':
            A, B = command[1:].split('/')
            line = exchange(line, int(A), int(B))
        elif command[0] == 'p':
            line = partner(line, command[1], command[3])

    return line


def position(line, file):
    for command in file:
        if command[0] == 's':
            line = swap(line, int(command[1:]))
        elif command[0] == 'x':
            A, B = command[1:].split('/')
            line = exchange(line, int(A), int(B))
    return line


def swaps(line, file):
    for command in file:
        if command[0] == 'p':
            line = partner(line, command[1], command[3])
    return line


def solution2(line, file, n):
    # The change of positions (spins and exchanges) is calculated exactly once
    pos = position(list(range(len(line))), file)
    # The swapping of characters (instead of positions) is also calculated
    # exactly once. It is converted to numbers between 0-15 to treat it equal
    # to the positionswaps.
    swp = swaps(list('abcdefghijklmnop'), file)
    swp = [ord(x)-ord('a') for x in swp]
    # This results in an array "pos" that shows where the character at each
    # position comes from after one full iteration of the instructions.
    # This array is used 10 times on a new array; "pos10". This shows where
    # each character should come from after 10 iterations.
    # This new array is used as a new basic "pos" which can now be used for
    # 10 iterations at a time.Using that 10 times again makes it 100 steps, etc

    # The same can be done for swaps.
    while n//10 >= 1:   # The loop increases by a factor 10 every time
        n = n//10
        pos10 = list(range(len(line)))
        swp10 = list(range(len(line)))
        # Create the new position array; 10 loops
        for _ in range(10):
            newpos = [0]*16
            for i, m in enumerate(pos):
                newpos[i] = pos10[m]
            pos10 = newpos
        # Create the new swap array; also 10 loops
            newswp = [0]*16
            for i, m in enumerate(swp):
                newswp[i] = swp10[m]
            swp10 = newswp
        pos = pos10
        swp = swp10

    # Create the actual output line; using the arrays calculated above.
    newline = [20]*16
    for i, m in enumerate(pos):
        newline[i] = line[m]
    line = newline
    for i, m in enumerate(line):
        line[i] = chr(swp[ord(m)-97]+97)
    return line


file = open('Day 16/input.txt').read().split(',')
line = list('abcdefghijklmnop')

iterations = 1000000000
print('The answer to part 1:', ''.join(solution2(line, file, 1)))
print('The answer to part 2:', ''.join(solution2(line, file, iterations)))
