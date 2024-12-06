import itertools
import sys

def automaton(rules, occupied):
    # Automaton is a generator that yields a new line for every next()
    # The input rules should be a list of 8 booleans representing b0-b7
    # The set named occupied contains all positions that are currently occupied

    # Because the occupied is a set; there is no limit to the size of the next
    # line. The assumption is that b0 is False; otherwise an infinitely large
    # set of occupied would occur immediately

    # On every next() it returns a set with all occupied spaces
    # for that generation

    LUT = {state: newstate for state, newstate
           in zip(itertools.product([False, True], repeat = 3), rules)}

    while True:
        yield occupied

        newOccupied = set()
        start, stop = min(occupied), max(occupied)
        state = tuple((n in occupied for n in range(start-3, start)))

        for n in range(start-1, stop+2):
            state = tuple(state[1:] + tuple([n+1 in occupied]))
            if LUT[state]:
                newOccupied.add(n)

        occupied = newOccupied

def printGeneration(aGeneration, linewidth):
    line = ['*' if n in generation else ' ' for n in range(linewidth)]
    print(''.join(line))


for i in sys.stdin:
    print(i)

stdin = []
rulesA = [False, True, False, True, True, True, True, False]
rulesB = [False, True, True, False, True, False, True, False]

linewidth = 61
generations = 20

a = automaton(rulesB, {20, 40})
for _ in range(generations):
    generation = next(a)
    printGeneration(generation, linewidth)


#TODO Read from standard input