import sys

class Player:
    def __init__(self, hp, mana, game):
        self.hp = hp
        self.mana = mana
        self.totalMana = 0
        self.game = game
        self.armour = 0
        self.spells = []
    
    def createBoss(self):
        self.boss = Boss(self, self.game)
        return self.boss
    
    def turn(self):
        spell = self.userInput()
        self.spells.append(spell)
        print()
        if spell == '1':
            self.drainMana(53)
            self.boss.hit(4)
        elif spell == '2':
            self.drainMana(73)
            self.boss.hit(2)
            self.hp += 2
        elif spell == '3':
            self.drainMana(113)
            self.game.shieldTimer = 6
        elif spell == '4':
            self.drainMana(173)
            self.game.poisonTimer = 6
        elif spell == '5':
            self.drainMana(229)
            self.game.rechargeTimer = 5
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
        print('2) Drain         (73 mana, 2 damage, heal 2)')
        print('3) Shield        (113 mana, +7 armour for 6 turns)')
        print('4) Poison        (173 mana, 3 damage for 6 turns)')
        print('5) Recharge      (229 mana, +101 mana for 5 turns)')
        print()
        
        return input()
        
    def drainMana(self, mana):
        self.mana -= mana
        # if self.mana < 0:
        #     print("Mana too low:", self.mana, ". Game Over")
        #     sys.exit()
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
            print("Spells used: ", self.player.spells)
            print(self.boss)
            print("Game Over")
            sys.exit()
            return True
        if self.player.mana < 0:
            print("Mana too low")
            print(self.player)
            print("Total Mana spent:", self.player.totalMana)
            print("Spells used: ", self.player.spells)
            print(self.boss)
            print("Game Over")
            sys.exit()
            
        else:
            return False
        
    def __repr__(self):
        return 'ShieldTimer: ' + str(self.shieldTimer) + '\nPoisonTimer: ' + str(self.poisonTimer) + '\nRechargeTimer: ' + str(self.rechargeTimer)
            
# game = Game()
game = Game(True)

#Part 1: 900 (just from playing: poison, recharge, shield,  poison, missile (x4))
#Part 2: 1216 (just from playing: poison, recharge, shield, poison, drain, recharge, poison, missile)