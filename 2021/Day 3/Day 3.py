file = open('input.txt').readlines()
data = [x.strip() for x in file]

d = [[] for _ in range(len(data[0]))]


for i, line in enumerate(data):
    for j, char in enumerate(line):
        d[j].append(int(char))
        
    
most = [int(sum(c)>len(data)//2) for c in d]
least = [int(sum(c)<len(data)//2) for c in d]


# gamma = sum([g*2**i for i, g in enumerate(gamma[::-1])])

# e = sum([x*2**i for i, x in enumerate(e[::-1])])

def part2(data, f):
    
    oxygen = data.copy()
    
    for i in range(len(data[0])):
        newoxygen = oxygen.copy()
        bestbit = int(sum([int(number[i]) for number in oxygen]) >= len(oxygen)/2)
        
        for o in oxygen:
            if int(o[i]) != bestbit:
                newoxygen.remove(o)
                if len(newoxygen) == 1:
                    oxans = newoxygen[0]
        
        oxygen = newoxygen.copy()
        


    oxygen = data.copy()
    
    for i in range(len(data[0])):
        newoxygen = oxygen.copy()
        bestbit = int(sum([int(number[i]) for number in oxygen]) < len(oxygen)/2)
        
        for o in oxygen:
            if int(o[i]) != bestbit:
                newoxygen.remove(o)
                if len(newoxygen) == 1:
                    COans = newoxygen[0]
        
        oxygen = newoxygen.copy()


    return oxans, COans

# part2(data,most)

o, c = part2(data, most)

p = sum([int(g)*2**i for i, g in enumerate(o[::-1])])
e = sum([int(g)*2**i for i, g in enumerate(c[::-1])])

print('The answer to part 1: ', p * e)
# print('The answer to part 2: ', p * CO)

# 866761 is wrong
# 2058441 is wrong
# 1127100