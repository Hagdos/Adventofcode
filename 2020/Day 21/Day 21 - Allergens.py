f = open('food.txt')

ai = {}
allingredients = []
ia = {}

for x,line in enumerate(f):
    sides = line.strip().split(' (')
    ingredients = sides[0].split(' ')
    allergens = sides[1][9:-1].split(', ') 
    allingredients = allingredients + ingredients
    
    for a in allergens:
        if a not in ai:
            ai[a] = set(ingredients)
        else:
            newingredients = set()
            for i in ingredients:
                if i in ai[a]:
                    newingredients.add(i)
            ai[a] = newingredients
        
possiblybad = set()
good = set(allingredients)
for a in ai:
    for i in ai[a]:
        possiblybad.add(i)
        good.discard(i)

ans = 0
ans2 = 0
for i in allingredients:
    if i not in possiblybad:
        ans+=1
    if i in good:
        ans2+=1
        
print(ans, ans2)

for a in ai:
    print('\n', a, ': ', ai[a], '\n')


# =============================================================================
# # ----------------- Part 2
# =============================================================================

for _ in range(10):
    for a in ai:
        if len(ai[a]) == 1:
            for b in ai:
                if b!= a:
                    ai[b].discard(list(ai[a])[0])
            # print(list(ai[a])[0])
# print(ai)

keys = list(ai.keys())
keys.sort()
ans = []
for k in keys:
    ans.append(list(ai[k])[0])
    
    
print(','.join(ans))
# print(keys)