import re

file = open('input.txt')

replacements = {}

for line in file:
    line = line.strip().split(' => ')
    if len(line) == 2:
        replacements.setdefault(line[0], []).append(line[1]) 
    elif len(line) == 1:
        original = line[0]
    
# options = set()
    
# for key in replacements.keys():
#     positions = re.finditer(key, original)
#     for position in positions:
#         for replacement in replacements[key]:
#             newMolecule = original[:position.span()[0]] +replacement + original[position.span()[1]:]
#             options.add(newMolecule)
        
# print("Answer to part 1:", len(options))

# =============================================================================
#  Part 2
# =============================================================================

steps = 0

molecules = {original: 0}

for _ in range(5):
    for molecule in list(molecules.keys()):
        for key, rlist in replacements.items():
            for replacement in rlist:
                matches = re.finditer(replacement, molecule)
                for m in matches:
                    newMolecule = molecule[:m.span()[0]] + key + molecule[m.span()[1]:]
                    if newMolecule not in molecules.keys() or molecules[newMolecule] > molecules[molecule] + 1:
                        molecules[newMolecule] = molecules[molecule] + 1 #Add 1 to the number of steps to reach this molecule
        del(molecules[molecule])
                

# This runs out of hand very quickly, because there are a lot of double paths (replace 1 first, then 2, instead of 2)
# print(molecules)
    