file = open('input.txt').readlines()
data = [x.strip().split(' -> ') for x in file]
ans1 = ans2 = 0

pol = data[0][0]
rules = {i:j for i,j in data[2:]}

# Naive solution. Works for 10; not for 40.
for step in range(10):
    newpol = ''
    
    for combo in zip(pol[:], pol[1:]):
        c = ''.join(combo)
        newpol += combo[0] + rules[c]

        
    newpol += pol[-1]
    pol = newpol

ns1 = {char: pol.count(char) for char in rules.values()}
print('The answer to part 1: ', max(ns1.values()) - min(ns1.values()))

# =============================================================================
# Part 2 
# =============================================================================

pol = data[0][0]
rules = {i:(i[0]+j, j+i[1]) for i,j in data[2:]}

# Initial list of combos; based on the given polymer
combos = {i:0 for i in rules}
for combo in zip(pol[:], pol[1:]):
    c = ''.join(combo)
    combos[c] += 1

for _ in range(40):
    # The new combolist; after this step
    newcombos = {i:0 for i in rules}
        
    for combo in combos:
        for nc in rules[combo]:
            newcombos[nc] += combos[combo] 
        
    combos = newcombos
    
# Empty dict of characters; for counting
ns = {char[0]: 0 for char in rules}

# Count the letters in every combo
for combo in combos:
    ns[combo[0]] += combos[combo]
    ns[combo[1]] += combos[combo]

# Add the first and last letter of the original polymer, because those are
# the only ones that aren't counted twice
ns[pol[0]] += 1
ns[pol[-1]] += 1

# Divide all by two; because letters are counted twice for every combo.
for n in ns:
    ns[n] //= 2
    
print('The answer to part 2: ', max(ns.values()) - min(ns.values()))