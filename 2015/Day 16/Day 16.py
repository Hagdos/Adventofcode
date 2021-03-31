text = open('input.txt')

sues = dict()

for line in text:
    line = line.strip().replace(':', '').replace(',', '').split()
    pets = dict()
    for i in range(2,len(line), 2):
        pets[line[i]] = int(line[i+1])
    sues[int(line[1])] = pets

measured = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

correctsue = []

for sue in sues:
    winner = True
    for animal in sues[sue]:
        if sues[sue][animal] != measured[animal]:
            winner = False
    if winner == True:
        print("Answer to part 1:", sue)
        break
        correctsue.append(sue)
        
# =============================================================================
#         Part 2
# =============================================================================

for sue in sues:
    winner = True
    for animal in sues[sue]:
       if animal in ("trees", "cats"):
           if sues[sue][animal] <= measured[animal]:
               winner = False 
       elif animal in ("pomeranians", "goldfish"):
           if sues[sue][animal] >= measured[animal]:
               winner = False 
       else:               
           if sues[sue][animal] != measured[animal]:
               winner = False
    if winner == True:
        print("Answer to part 2:", sue)
        break
        correctsue.append(sue)