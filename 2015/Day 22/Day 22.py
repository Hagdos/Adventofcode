import sys

class Player:
    def __init__(self, hp, mana, game):
        self.hp = hp
        self.mana = mana
        self.totalMana = 0
        self.game = game
        self.armour = 0

    
    def createBoss(self):
        self.boss = Boss(self, self.game)
        return self.boss
    
    def turn(self):
        spell = self.userInput()
        print()
        if spell == '1':
            self.boss.hit(4)
            self.drainMana(53)
        elif spell == '2':
            self.boss.hit(2)
            self.hp += 2
            self.drainMana(73)
        elif spell == '3':
            self.game.shieldTimer = 6
            self.drainMana(113)
        elif spell == '4':
            self.game.poisonTimer = 6
            self.drainMana(173)
        elif spell == '5':
            self.game.rechargeTimer = 5
            self.drainMana(229)
        elif spell == 'E':
            self.hp = -10
        else:
            print("Wrong input, try again:")
            self.turn()

       
    def userInput(self):
        print(self.game)
        print(self)
        print(self.boss)
        print("Your turn. Pick a spell:")
        print()                 
        print('1) Magic missile (53 mana, 4 damage)')
        print('2) Drain         (73 mana, 2 damage, heal 2')
        print('3) Shield        (113 mana, +7 armour for 6 turns')
        print('4) Poison        (173 mana, 3 damage for 6 turns')
        print('5) Recharge      (229 mana, +101 mana for 5 turns')
        print()
        
        return input()
        
    def drainMana(self, mana):
        self.mana -= mana
        if mana < 0:
            self.hp = -1
        self.totalMana += mana
       
    def hit(self, damage):
        self.hp -= max(damage-self.armour, 1)
        self.game.checkGameOver()

    def __repr__(self):
        return 'Player, HP: ' + str(self.hp) + ' Mana: ' + str(self.mana)


class Boss:
    def __init__(self, player, game):
        self.damage = 9
        self.hp = 51
        self.player = player
        self.game = game
        
    def turn(self):
        self.player.hit(self.damage)
        
    def hit(self, damage):
        self.hp -= max(damage, 1)
        self.game.checkGameOver()
        
    def __repr__(self):
        return 'Boss, HP: ' + str(self.hp)

       
class Game:
    def __init__(self, pt2 = False):
        self.player = Player(50, 500, self)
        self.boss = self.player.createBoss()
        self.shieldTimer = 0
        self.poisonTimer = 0
        self.rechargeTimer = 0
        self.pt2 = pt2
        self.playgame()
        
    def playgame(self):
        while True:
            self.turn()
        
    def turn(self):
        if self.pt2 == True:
            self.player.hit(1)
            
        self.checkEffects()
        self.player.turn()

        self.checkEffects()
        self.boss.turn()
        
    def checkEffects(self):
        self.checkShield()
        self.checkPoison()
        self.checkRecharge()
        self.checkGameOver()
        
    
    def checkShield(self):
        if self.shieldTimer > 0:
            self.player.armour = 7
            self.shieldTimer -= 1
        else:
            self.player.armour = 0
            self.shieldTimer = 0
            
    def checkPoison(self):
        if self.poisonTimer > 0:
            self.boss.hit(3)
            self.poisonTimer -= 1
            
    def checkRecharge(self):
        if self.rechargeTimer > 0:
            self.player.mana += 101
            self.rechargeTimer -= 1
            
    def checkGameOver(self):
        if self.player.hp <= 0 or self.boss.hp <= 0:
            print(self.player)
            print("Total Mana spent:", self.player.totalMana)
            print(self.boss)
            print("Game Over")
            sys.exit()
            return True
        else:
            return False
        
    def __repr__(self):
        return 'ShieldTimer: ' + str(self.shieldTimer) + '\nPoisonTimer: ' + str(self.poisonTimer) + '\nRechargeTimer: ' + str(self.rechargeTimer)
            

# game = Game()
game = Game(True)

#Part 1: 900 (just from playing: Poison, shield, recharge, poison, missile (x4))

# Part 2: 1080 is too low (running out of mana)
# 1256 is too high...


# Magic missile: 4 damage, 53 mana => 13.25 mana/damage
# 4 damage/turn

# Drain: 2 damage, 2 health, 73 mana => 36.5 mana/damage; or 18.25 mana/damage if health is counted too
# 2 damage/turn

# Shield: 7 armor for 6 turns. Effectively 21 health. 113 mana => 5.38 mana/health => Cheap!

# Poison: 3 damage for 6 turns (18 damage), 173 mana => 9.61 mana/damage
# 6 damage/turn (both turns)

# Recharge: +101 mana for 5 turns (505 mana) costs 229 mana


# -> Shield + Poison are the most effective. Shield is best but doesnt do damage. After that magic missile.

# Boss = 51 Hp and 9 Damage
# Player = 50 Hp

# With always poison (3x); boss dies in 51/3 = 17 turns (8x player, 8x boss, 1x player w/o attack)
# Last poison is "only" 5 turns; still 173/(5*6) = 5.8 mana/damage

# In 8 turns; boss kills you (8*9) with 22 Hp to spare. 
# One shield brings it down to -1 Hp, but takes an extra turn; so -10 Hp

