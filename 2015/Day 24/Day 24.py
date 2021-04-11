import itertools

pt2 = True

def prod(iterator):
    answer = 1
    for i in iterator:
        answer *= i
        
    return answer

presents = open('input.txt').read().split()
presents = tuple(int(x) for x in presents)
    
totalMass = sum(presents)
goalMass = totalMass//3

if pt2:
    goalMass = totalMass // 4

options = set()

for n in range(2,len(presents)):
    for combination in itertools.combinations(presents, n):
        if sum(combination) == goalMass:
            options.add(combination)
    
    #Stop if options are found; we are only interested in the smallest groups.
    if options:
        break


# # Check if there is a way to split the remaining presents in a group with the correct mass.
# # Turns out to be true for every option, so can be left out.
# newoptions = set()
# for option in options:
#     print()
#     print(option)
#     found = False
#     remaining = [x for x in presents if x not in option]
#     for n in range(2,len(remaining)):
#         for combination in itertools.combinations(remaining, n):
#             if sum(combination) == goalMass:
#                 print("Combination found")
#                 newoptions.add(option)
#                 found = True
#                 break
#         if found:
#             break
            
            
    
    
lowestQE = 10**30
for option in options:
    QE = prod(option)
    if QE < lowestQE:
        lowestQE = QE
        lowestOption = option
        


print("Answer:", lowestQE)

#101 is too low
    