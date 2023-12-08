def countsteps(start):
    node = start
    pointer = 0
    while node[2] != 'Z':
        node = network[node][directionmap[directions[pointer%directionlength]]]
        pointer += 1
    return pointer

file = open('input.txt')

directions = file.readline().strip()
directionmap = {'L': 0,
                'R': 1}
directionlength = len(directions)
file.readline()

network = dict()

for line in file.readlines():
    node, destinations = line.strip().split(' = ')
    destinations = tuple(destinations[1:-1].split(', '))
    network[node]=destinations

looplengths = [countsteps(key) for key in network if key[2] == 'A' ]

adder = ans2 = looplengths[0]

for n in looplengths[1:]:
    while ans2 % n != 0:
        ans2 += adder
    adder = ans2

print('The answer to part 1: ', countsteps('AAA'))
print('The answer to part 2: ', ans2)