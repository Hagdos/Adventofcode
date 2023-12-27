class ingredient:
    def __init__(self, line):
        line = line.strip().split()
        self.name = line[0][:-1]
        self.capacity = int(line[2][:-1])
        self.durability = int(line[4][:-1])
        self.flavor = int(line[6][:-1])
        self.texture = int(line[8][:-1])
        self.calories = int(line[10])

    def __repr__(self):
        return self.name

text = open('input.txt')
pt2 = True

ingredients = []
for line in text:
    ingredients.append(ingredient(line))

# print(ingredients)

recipes = []
for sugar in range(101):
    for sprinkles in range(101-sugar):
        for candy in range(101-sugar-sprinkles):
            chocolate = 100-sugar-sprinkles-candy
            recipes.append((sugar,sprinkles,candy,chocolate))
maxscore = 0
for recipe in recipes:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i, n in enumerate(recipe):
        capacity    += ingredients[i].capacity*n
        durability  += ingredients[i].durability*n
        flavor      += ingredients[i].flavor*n
        texture     += ingredients[i].texture*n
        calories    += ingredients[i].calories*n
    # if calories != 500:
    #     score = 0
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        score = 0
    else:
        score = capacity * durability * flavor * texture
    if score > maxscore:
        maxscore = score
        bestrecipe = recipe
        bestcapacity = capacity

print('Answer to part 1:', maxscore)
