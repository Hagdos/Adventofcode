recipes = [3, 7]
elves = [0, 1]

input = '074501'

pt1 = False
pt2 = False
goallength = int(input) + 10
pt2ans = [int(c) for c in input]
while not (pt1 and pt2):
    newrecipe = sum([recipes[i] for i in elves])
    if newrecipe // 10:
        recipes.append(newrecipe // 10)
    recipes.append(newrecipe % 10)

    if not pt1 and len(recipes) >= goallength:
        ans1 = ''.join([str(i) for i in recipes[-10:]])
        print(f'The answer to part 1: {ans1}')
        pt1 = True

    # recipe = ''.join([str(i) for i in recipes[-6:]])
    if not pt2 and (pt2ans == recipes[-7:-1] or pt2ans == recipes[-6:]):
        print(f'The answer to part 1: {len(recipes)-6}')
        pt2 = True

    for elf, r in enumerate(elves):
        elves[elf] += 1 + recipes[r]
        elves[elf] %= len(recipes)
