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
    
options = set()
    
for key in replacements.keys():
    positions = re.finditer(key, original)
    for position in positions:
        for replacement in replacements[key]:
            newMolecule = original[:position.span()[0]] +replacement + original[position.span()[1]:]
            options.add(newMolecule)
        
print("Answer to part 1:", len(options))

# =============================================================================
#  Part 2
# =============================================================================

def solve(molecule, steps):
    molecules = {molecule: steps}
    
    noChanges = False
    while noChanges == False:
        noChanges = True
        for molecule in list(molecules.keys()):
            newFound = False
            for key, rlist in replacements.items():
                for replacement in rlist:
                    matches = re.finditer(replacement, molecule)
                    for m in matches:
                        newFound = True
                        newMolecule = molecule[:m.span()[0]] + key + molecule[m.span()[1]:] #Replace the match with the key.
                        if newMolecule not in molecules.keys() or molecules[newMolecule] > molecules[molecule] + 1:
                            molecules[newMolecule] = molecules[molecule] + 1 #Add 1 to the number of steps to reach this molecule
            if newFound == True:
                noChanges = False
                del(molecules[molecule])
            
    return molecules

molecule = original
steps = 0
molecules = {molecule: steps}

while 'e' not in molecules.keys():
    for molecule in molecules:
        parts = re.split(r'(.*?Ar)', molecule)
        parts = list(filter(None, parts))
        
        options = {'': molecules[molecule]}
        
        for i, p in enumerate(parts):
            newOptions = {}
            solutions = solve(p, 0)
            for option in options.keys():
                for solution in solutions:
                    newOptions[option + solution] = options[option] + solutions[solution]
                    # print(s)
                    
            options = newOptions
    
    molecules = options

print("Answer to part 2:", molecules['e'])