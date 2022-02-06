from collections import defaultdict

file = open('input.txt').readlines()

rules = [(x.strip().split()[1], x.strip().split()[7]) for x in file]

# Values must be done before key
before = defaultdict(list)

# Values can be done after key
after = defaultdict(list)

# Possible is what's possible for the next letter
allLetters = set()

for rule in rules:
    before[rule[1]].append(rule[0])
    after[rule[0]].append(rule[1])
    allLetters.update(*rule)

possible = [letter for letter in allLetters if letter not in before.keys()]

order = ''

for _ in range(len(allLetters)):
    possible.sort()
    
    nextletter = possible.pop(0)
    order += nextletter
    for letter in after[nextletter]:
        if all([x in order for x in before[letter]]):
            possible.append(letter)

print("The answer to Part 1:", order)
    
# =============================================================================
# Part 2
# =============================================================================

def timeNeeded(letter):
    return ord(letter) - 4

nWorkers = 5

workerTimes = [0] * nWorkers
workerLetters = [None] * nWorkers

time = -1
possible = [letter for letter in allLetters if letter not in before.keys()]
order = ''

while len(order) < len(allLetters) and time < 2000:
    time += 1
    # If any worker is done; add their letter to the order and 
    # check all letters if they are possible now
    
    # Add finished letters to the order
    for worker in range(nWorkers):
        if workerLetters[worker] and workerTimes[worker] == 0:
            order += workerLetters[worker]
            workerLetters[worker] = None
            
    # Check for new available letters
    for letter in allLetters:
        if (letter not in order and 
            letter not in workerLetters and
            letter not in possible and
            all([x in order for x in before[letter]])):
            possible.append(letter)
    
    possible.sort()

    # Check if there are workers and letters available, assign new letters
    while possible and any([workerTimes[worker] == 0 for worker in range(nWorkers)]):
        worker = workerTimes.index(0)
        workerLetters[worker] = possible.pop(0)
        workerTimes[worker] = timeNeeded(workerLetters[worker])

    # Have all workertimes decrease with 1
    for worker in range(nWorkers):
        if workerTimes[worker] != 0:
            workerTimes[worker] -= 1   

print(f'The answer to Part 2: {time}')
