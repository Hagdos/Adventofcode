from elves import Creature, printmap, readInput, findCreature

cavern, goblins, elves, xrange, yrange = readInput('input.txt')


printmap(cavern, goblins, elves, xrange, yrange)

# print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans2)


# print(list(goblins.keys())[0].findNearestEnemy(goblins, elves, cavern))

print(list(goblins.keys())[0].turn(goblins, elves, cavern))

# # Goblins; elves are stored as dictionary: [Creature] = (x,y)
# print(goblins)

# # Can be sorted as: sorted(goblins.keys(), key = lambda x: (x[1], x[0]))
# print(sorted(goblins.items(), key = lambda x: (x[1][1], x[1][0])))

# # A creature can be found from it's position:
# print(findCreature(goblins, (7, 20)))

# https://adventofcode.com/2018/day/15