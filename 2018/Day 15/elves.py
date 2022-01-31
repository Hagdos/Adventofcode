import itertools

class Creature:
    id_iter = itertools.count()
    
    def __init__(self):
        self.id = next(self.id_iter)
        self.hp = 200
        self.ap = 3


    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    
    def turn(self, allies, enemies, cavern):
        # If the unit is already in range of a target, it does not move, 
        # but continues its turn with an attack. 
        
        target = self.enemyInRange(allies, enemies)
        if target:
            self.attack(target)
            return
        
        # Otherwise, since it is not in range of a target, it moves.
        
        self.move(allies, enemies, cavern)
        self.attack(self.enemyInRange(allies, enemies))
        
        return
    
    def enemyInRange(self, allies, enemies):
        # Return the first enemy in range. If no enemies in range; return None
        x, y = allies[self]
        for position in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
            if position in enemies.values():
                return findCreature(enemies, position)
        
        return None


    def attack(self, enemy):
        # TODO Attack the given enemy 
        return None

    def move(self, allies, enemies, cavern):
        nextStep, destination = self.findNearestEnemy(allies, enemies, cavern)
        allies[self] = nextStep
            
    def findNearestEnemy(self, allies, enemies, cavern):
        # Finds nearest reachable enemy
        # and returns the first step towards and the open square next to it
        # TODO Change this to deque from collections
        Q = [(allies[self], None)]
        visited = set(allies[self])
        
        while Q:
            pos, firstStep = Q.pop(0)
            print(pos)
            x, y = pos
            for position in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
                if position in enemies.values():
                    return firstStep, (x, y)
                elif (position in cavern and position not in allies.values() 
                      and position not in visited):
                    if not firstStep:
                        firstStep = position
                    visited.add(position)
                    Q.append((position, firstStep))
        return None

def readInput(filename):
    file = open(filename).readlines()
    data = [x.strip() for x in file]
    
    # TODO Change for bidict? Check if these can be ordered.
    goblins = dict()
    elves = dict()
    cavern = set()
    
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '.':
                cavern.add((x,y))
            elif char == 'G':
                cavern.add((x,y))
                goblins[Creature()] = (x, y)
            elif char == 'E':
                cavern.add((x,y))
                elves[Creature()] = (x, y)
    
    xrange = range(x+1)
    yrange = range(y+1)
    
    return cavern, goblins, elves, xrange, yrange


def printmap(cavern, goblins, elves, xrange, yrange):
    line = [' '] + [str(x%10) for x in xrange]
    print(''.join(line))
    
    for y in yrange:
        line = [str(y%10)]
        for x in xrange:
            if (x, y) in elves.values():
                line.append('E')
            elif (x, y) in goblins.values():
                line.append('G')
            elif (x,y) in cavern:
                line.append(' ')
            else:
                line.append('█')
        print(''.join(line))
    print()
    

def findCreature(creatureDict, position):
    for creature, pos in creatureDict.items():
        if pos == position:
            return creature
    return None