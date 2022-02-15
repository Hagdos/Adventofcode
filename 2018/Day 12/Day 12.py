import time

file = open('2018/Day 12/input.txt')
init = file.readline().strip().split(': ')[1]

# Create initial set of plants
plants = set()
for number, plant in enumerate(init):
    if plant == '#':
        plants.add(number)

# Create look-up table for when a pot will grow a plant
file.readline()
turnsPlant = set(x.strip().split(' => ')[0] for x in file
                 if x.strip().split(' => ')[1] == '#')
turnsPlant = set(tuple(c == '#' for c in row) for row in turnsPlant)

start = time.time()
for turn in range(1000):
    newplants = set()
    for plant in range(min(plants)-2, max(plants)+3):
        neighbours = tuple(p in plants for p in range(plant-2, plant+3))
        if neighbours in turnsPlant:
            newplants.add(plant)
    plants = newplants

    if turn == 20:
        print(f'The answer to part 1: {sum(plants)}')

# After a few hundred cycles the row stabilizes, which each plant moving one
# step to the left each turn
plants = [p + 50000000000 - 1000 for p in plants]
print(f'The answer to part 2: {sum(plants)}')

print(f'This took {time.time()-start} seconds')
