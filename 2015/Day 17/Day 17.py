import itertools

containers = (43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38)

variations = 0
variations2 = 0
minimumFound = False

for r in range(len(containers)):
    for combination in itertools.combinations(containers, r):
        if sum(combination) == 150:
            variations += 1
            
            if minimumFound == False:
                minimum = r
                minimumFound = True
            
            if r == minimum:
                variations2 += 1
            
print("The answer to part 1:", variations)
print("The answer to part 2:", variations2)

# print(len(containers))