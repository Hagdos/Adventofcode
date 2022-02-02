from elves import printmap, readInput

ap = 3
LowLimit = ap
HighLimit = 1000
found = False

while not found:
    print(HighLimit)
    cavern, goblins, elves, xrange, yrange = readInput('input.txt', ap)
    
    for turn in range(500):
        creatures = list(goblins.items()) + list(elves.items())
        creatures.sort(key = lambda x: (x[1][1], x[1][0]))
        
        for creature in creatures:
            creature = creature[0]
            if creature in goblins.keys():
                gameover = creature.turn(goblins, elves, cavern)
            else:
                gameover = creature.turn(elves, goblins, cavern)
    
        if gameover:
            break
    
    if len(elves) < 10:
        LowLimit = ap
    else:
        HighLimit = ap
        totalHP = sum(c.hp for c in goblins) + sum(c.hp for c in elves)
        solution = turn*totalHP
    
    if HighLimit - LowLimit == 1:
        found = True
        print(f"The answer to part 2: {solution}")
    
    ap = (HighLimit + LowLimit)//2
    
    
    

# print(f"The answer to part 1: {turn*totalHP}")

# Should be 10
print(len(elves))


    
        # print(f'Turn: {turn}')
        # printmap(cavern, goblins, elves, xrange, yrange)
        # print(*creatures, sep='\n')

# # Goblins; elves are stored as dictionary: [Creature] = (x,y)
# print(goblins)

# # Can be sorted as: sorted(goblins.keys(), key = lambda x: (x[1], x[0]))
# sorted(goblins.items(), key = lambda x: (x[1][1], x[1][0])))

# # A creature can be found from it's position:
# print(findCreature(goblins, (7, 20)))

# https://adventofcode.com/2018/day/15