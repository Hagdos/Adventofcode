noElves = 3004953

Elves = range(1,noElves+1)

odd = 1     # To make sure the script starts with elf 1.

#On every loop; take out half of the elves.
while len(Elves)>1:
    old_odd = odd
    odd = (len(Elves)+old_odd)%2
    Elves = Elves[old_odd::2]

print('The answer to part 1:', Elves[0])

# =============================================================================
# Part 2
# =============================================================================

# A linked list; The index is the elves number (starting at 0), the value in the list the next elf.
linkedList = list(range(1, noElves+1))
linkedList[-1] = 0

position = noElves//2-1

linkedList[position] = linkedList[linkedList[position]]

for _ in range(noElves//2):
    position = linkedList[position]
    linkedList[position] = linkedList[linkedList[linkedList[position]]]

print('The answer to part 2:', position+1)