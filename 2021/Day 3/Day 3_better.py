file = open('input.txt').readlines()
data = [x.strip() for x in file]

def inverse(data):
    return [x for x in zip(*data)]

def bestbit(data, position):
    return int(inverse(data)[position].count('1') >= len(data)/2)

def worstbit(data, position):
    return int(inverse(data)[position].count('1') < len(data)/2)

def bittoint(array):
    return sum([g*2**i for i, g in enumerate(array[::-1])])

gamma = [bestbit(data, i) for i in range(len(data[0]))]
epsilon = [worstbit(data, i) for i in range(len(data[0]))]

print('The answer to part 1:', bittoint(gamma)*bittoint(epsilon))

oxygen = data.copy()
CO = data.copy()
for p in range(len(data[0])):
    bb = bestbit(oxygen, p)
    oxygen = [o for o in oxygen if int(o[p]) == bb]
    
    
for p in range(len(data[0])):   
    wb = worstbit(CO, p)

    CO = [c for c in CO if int(c[p]) == wb]
    if len(CO) == 1:
        break

print('The answer to part 2:',int(oxygen[0], 2) * int(CO[0], 2))