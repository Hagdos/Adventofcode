from collections import defaultdict

def nextStep(snode, path, links, dual):
    newpaths = []
    if snode == 'end':
        return [path]
    
    for n in links[snode]:
        # print(path, dual)
        if n == 'start':
            continue
        # Already visited n; there's already a small we visited twice
        elif n.islower() and n in path and dual:
            continue
        # Already visited n more than twice
        elif n.islower() and path.count(n) >= 2:
            continue

        newpaths += nextStep(n, path + [n], links, (dual or (n.islower() and n in path)))

    return newpaths


file = open('input.txt').readlines()
data = [x.strip().split('-') for x in file]

links = defaultdict(list)
for line in data:
    links[line[0]].append(line[1])
    links[line[1]].append(line[0])
    

allpaths = nextStep('start', ['start'], links, dual=True)
allpaths2 = nextStep('start', ['start'], links, dual=False)

print('The answer to part 1: ', len(allpaths))
print('The answer to part 2: ', len(allpaths2))
