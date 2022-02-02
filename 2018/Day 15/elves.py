import itertools

class Creature:
    id_iter = itertools.count()
    
    def __init__(self, ap):
        self.id = next(self.id_iter)
        self.hp = 200
        self.ap = ap


    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    
    def turn(self, allies, enemies, cavern):
        # Check if unit is still alive (could have been killed this turn)
        if self.hp <= 0:
            return False
        
        # Check if there are enemies at all
        if not enemies:
            return True
            
        # If the unit is already in range of a target, it does not move, 
        # but immediately attacks. 
        target = self.enemyInRange(allies, enemies)
        if target:
            self.attack(target, enemies)
            return False
        
        # Otherwise, since it is not in range of a target, it moves.
        reached = self.move(allies, enemies, cavern)
        
        # If a target is reached; attack
        if reached: 
            target = self.enemyInRange(allies, enemies)
            if target:
                self.attack(target, enemies)
        return False
    
    def enemyInRange(self, allies, enemies):
        # Return the enemy with the lowest hp in range. 
        # At equal hp the first is selected
        # If no enemies in range; return None
        x, y = allies[self]
        target = None
        for position in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
            if position in enemies.values():
                possibleTarget = findCreature(enemies, position)
                if not target or possibleTarget.hp < target.hp:
                    target = possibleTarget
        return target


    def attack(self, enemy, enemies):
        # Attack the given enemy 
        enemy.hp -= self.ap
        # If enemy is dead; remove from list
        if enemy.hp <= 0:
            enemies.pop(enemy)
        return None

    def move(self, allies, enemies, cavern):
        nextStep, destination = self.findNearestEnemy(allies, enemies, cavern)
        allies[self] = nextStep
        return nextStep == destination
            
    def findNearestEnemy(self, allies, enemies, cavern):
        # Finds nearest reachable enemy
        # and returns the first step towards and the open square next to it
        # TODO Change this to deque from collections
        Q = [(allies[self], None)]
        visited = set(allies[self])
        
        while Q:
            pos, firstStep = Q.pop(0)
            x, y = pos
            for position in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
                if position in enemies.values():
                    return firstStep, (x, y)
                elif (position in cavern and position not in allies.values() 
                      and position not in visited):
                    if not firstStep:
                        Q.append((position, position))
                    visited.add(position)
                    Q.append((position, firstStep))
                    
        return allies[self], None

def readInput(filename, ap):
    file = open(filename).readlines()
    data = [x.strip() for x in file]
    
    goblins = dict()
    elves = dict()
    cavern = set()
    
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '.':
                cavern.add((x,y))
            elif char == 'G':
                cavern.add((x,y))
                goblins[Creature(3)] = (x, y)
            elif char == 'E':
                cavern.add((x,y))
                elves[Creature(ap)] = (x, y)
            elif char == ' ':
                break
    
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
