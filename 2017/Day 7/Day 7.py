file = open('input.txt').readlines()


# Function that adds the weight of the program and all programs on top of it
def towerweight(program):
    totalweight = programweights[program]
    for upperprogram in programs[program]:
        totalweight += towerweight(upperprogram)

    return totalweight


# Creates a list of weights of the programs directly on top of the give program
# From this list it figures out which weight is wrong (only in the list once)
# It returns the name of the program that is out of balance, the difference
# in weights and the
def findoutofbalance(program):
    weights = []
    for upperprogram in programs[program]:
        weights.append(towerweight(upperprogram))

    for i, w in enumerate(weights):
        if weights.count(w) == 1:
            try:
                diff = w - weights[i+1]
            except IndexError:
                diff = w - weights[i-1]
            return programs[program][i], diff

    return None, 0


data = [x.strip().split('-> ') for x in file]

programs = dict()
programweights = dict()
alldiscs = []

for program in data:
    name = program[0].split(' ')[0]
    programs[name] = []
    programweights[name] = int(program[0].split(' ')[1][1:-1])

    if len(program) > 1:
        discs = program[1].split(', ')
        programs[name] = discs

        for disc in discs:
            alldiscs.append(disc)

for program in programs.keys():
    if program not in alldiscs:
        bottomprogram = program
        print('The answer to part 1: ', bottomprogram)

nexttower = bottomprogram
sets = []
while nexttower:
    prevtower = nexttower
    nexttower, weights = findoutofbalance(nexttower)
    sets.append((nexttower, weights))

# The last set in sets is a balanced disc.
# So the top unbalanced disc is sets[-2]
# The bad program in this one is given by the findoutofbalance function,
# as well as the difference. The correct answer is the subtraction of these

badprogram = sets[-2][0]
difference = sets[-2][1]

print('The answer to part 2: ', programweights[badprogram] - difference)
