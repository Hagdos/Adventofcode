from copy import deepcopy

p1 = True
p1 = False
f = open('fuel.txt')

inputs = {}
for x in f:
    i = x.strip().split(' => ')
    key = i[1].split(' ')[1]
    cont = [i[1].split()[0]] + i[0].replace(',', '').split()
    inputs[key] = cont

    
    

    
def checkifingredient(inputs, output, ing):
    iningredients = False
    for i in inputs:
        if i != output:
            for ingredient in inputs[i][2::2]:
                # print(ingredient)
                if ing == ingredient:
                    iningredients = True
                    return iningredients
    return iningredients
            



def countore(inputs):
    fuel = 'COOL'
    start = 0
    while(len(inputs[fuel])>3 or start<1):
        start = 1
        for i, ing in enumerate(inputs[fuel][2::2]):
            if not checkifingredient(inputs, fuel, ing):
                if ing == 'ORE':
                    break
                index = inputs[fuel].index(ing)
                required = int(inputs[fuel][index-1])
                created = int(inputs[ing][0])
                replace = required//created + (required%created > 0)
                
                inputs[fuel].pop(index-1)
                inputs[fuel].pop(index-1)
                
                for j, y in enumerate(inputs[ing][2::2]):
                    if y in inputs[fuel]:
                        amountadded = int(inputs[ing][j*2+1])*replace
                        loc = inputs[fuel].index(y)-1
                        inputs[fuel][loc] = int(inputs[fuel][loc]) + amountadded
                        # print(y, loc, amountadded)
                    else:
                        inputs[fuel].append(int(inputs[ing][j*2+1])*replace)
                        inputs[fuel].append(inputs[ing][j*2+2])
                
                # print(inputs[fuel])
                # inputs[fuel] = inputs[fuel] + inputs[ing][1:]
                del inputs[ing]
    return inputs[fuel][1]




    
if p1:
    amountoffuelcreated = 1
    inputs['COOL'] = [1, amountoffuelcreated, 'FUEL']
    print("Answer part 1:", countore(inputs))
else:
    amountoffuelcreated = 2371690
    for _ in range(20):
        inputs2 = deepcopy(inputs)
        inputs2['COOL'] = [1, amountoffuelcreated, 'FUEL']
        ore = countore(inputs2)
        if ore < 1000000000000:
            print(amountoffuelcreated, "is too little. Ore:", ore)
            amountoffuelcreated += 1
        else:
            print(amountoffuelcreated, "is too much. Ore:", ore)
            amountoffuelcreated += -1


# 2371 is too low
