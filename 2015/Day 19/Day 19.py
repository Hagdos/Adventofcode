import re

file = open('input.txt')

replacements = {}
replacementsCa = {}

for line in file:
    line = line.strip().split(' => ')
    if len(line) == 2:
        replacements.setdefault(line[0], []).append(line[1])
        if 'Ca' in line[1]:
            replacementsCa[line[0]] = line[1]
        
        
    elif len(line) == 1:
        original = line[0]
        
# =============================================================================
#         Part 1
# =============================================================================
    
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

def removeCa(molecule, steps):
    for key, value in replacementsCa.items():
        matches = re.findall(r'Ca', molecule)
        molecule = re.sub(r'Ca', '', molecule)
        steps += len(matches)
    return molecule, steps

molecule = original
steps = 0
# molecule, steps = removeCa(original[:], steps)

molecules = {molecule: steps}

for _ in range(3):
    for molecule in list(molecules.keys()):
        for key, rlist in replacements.items():
            for replacement in rlist:
                matches = re.finditer(replacement, molecule)
                for m in matches:
                    newMolecule = molecule[:m.span()[0]] + key + molecule[m.span()[1]:]
                    if newMolecule not in molecules.keys() or molecules[newMolecule] > molecules[molecule] + 1:
                        molecules[newMolecule] = molecules[molecule] + 1 #Add 1 to the number of steps to reach this molecule
        del(molecules[molecule])
    
    for molecule in list(molecules.keys()):
        newMolecule, newSteps = removeCa(molecule, molecules[molecule])
        if newMolecule != molecule:
            if newMolecule not in molecules.keys() or molecules[newMolecule] > molecules[molecule] + 1:
                molecules[newMolecule] = newSteps 
            del(molecules[molecule])
                

# This runs out of hand very quickly, because there are a lot of double paths (replace 1 first, then 2, instead of 2)
# print(molecules)
    

#Ar is always at the end; I guess we can split it up in pieces that end with Ar?
#CRn is always at the beginning. Both CRn and Ar can't be created. So any solveable molecule has to start with CRn and end with Ar

#Another thing to look at is to "generalize" molecule swaps. From P we can make Ca*(P*SiRnFAr*P*)*Ti* (and SiRnFAr can be used for more shit; but it will start and end with Ca and Ti)