import re
import itertools

class Player:
    def __init__(self, name, damage, armour, hp, outfit = None):
        self.name = name
        self.damage = damage
        self.armour = armour
        self.hp = hp
        
        if outfit:
            self.outfit = outfit
            self.damage += outfit.damage
            self.armour += outfit.armour
        
    def hit(self, damage):
        self.hp -= max(damage-self.armour, 1)
        
    def __repr__(self):
        return self.name + ', HP: ' + str(self.hp)
    
class Outfit:
    # def __init__(self, weapon, armour, leftring, rightring):
    #     self.weapon = weapon
    #     self.armour = armour
    #     self.leftring = leftring
    #     self.rightring = rightring
    
    def __init__(self, *args):
        self.names = []
        self.cost = 0
        self.damage = 0
        self.armour = 0
        
        for gear in args:
            self.names.append(gear.name)
            self.cost += gear.cost
            self.damage += gear.damage
            self.armour += gear.armour
            
    def __repr__(self):
        return str(self.names)
    
class Gear:
    def __init__(self, name, cost, damage, armour):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour
        
    def __repr__(self):
        return self.name
    
def playGame(player, boss):
    #Player hits first, so one go. After that; player hits and boss hits. If player is still alive when boss is dead; player wins
    boss.hit(player.damage)
    while boss.hp > 0 and player.hp > 0:
        player.hit(boss.damage)
        boss.hit(player.damage)
    
    #True means player won, False means boss won
    return player.hp > 0
    

store = open('input.txt')

for line in store:
    line = line.strip()
    line = re.split(r'  +', line)
    
    if line == ['']:
        continue
    
    elif line[0] == 'Weapons:':
        weapons = []
        current = weapons
        continue
    
    elif line[0] == 'Armor:':
        armours = [Gear('None', 0, 0, 0)]
        current = armours
        continue
    
    elif line[0] == 'Rings:':
        rings = [Gear('None', 0, 0, 0)]
        current = rings
        continue
    
    else:
        current.append(Gear(line[0], int(line[1]), int(line[2]), int(line[3])))
    

outfits = [Outfit(weapon, armour, leftring, rightring) for weapon in weapons for armour in armours for leftring in rings for rightring in rings]

lowestCost = 1000
highestCost = 0

for outfit in outfits:
    player = Player('Player', 0, 0, 100, outfit)
    boss = Player('Boss', 8, 1, 104)
    if playGame(player, boss):
        if player.outfit.cost < lowestCost:
            lowestCost = player.outfit.cost
    else:
        if player.outfit.cost > highestCost:
            highestCost = player.outfit.cost
            highestOutfit = player.outfit
            
            
print('Answer to Part 1: ', lowestCost)

print('Answer to Part 2: ', highestCost)