import re

class Group():
    def __init__(self, text, groupnumber, army):
        self.name = army.name + ' group ' + str(groupnumber)
        split = text.split()
        self.units = int(split[0])
        self.hp = int(split[4])
        self.init = int(split[-1])
        self.damage = int(split[-6])
        self.damtype = split[-5]
        
        vulnerabilities = re.search(r'\(.*\)', text)
        self.weaknesses = []
        self.immunities = []
        
        if vulnerabilities:
            vulnerabilities = vulnerabilities.group(0).strip('()').split()

            for word in vulnerabilities:
                if word == 'weak':
                    currentlist = self.weaknesses
                elif word == 'immune':
                    currentlist = self.immunities
                elif word == 'to':
                    pass
                else:
                    currentlist.append(word.strip(',;'))
            
    def attack(self):
        other = self.target
        if other and self.units:
            power = self.effectivePower()            
            if self.damtype in other.weaknesses:
                power *= 2
            elif self.damtype in other.immunities:
                print('This should not happen')
                power = 0
            other.takedamage(power)
        
    def takedamage(self, damage):
        self.units -= damage // self.hp
        if self.units < 0: self.units = 0

    def effectivePower(self):
        return self.units * self.damage


    def __repr__(self):
        string = self.name +': ' + str(self.units) + ' units'
        return(string)

    
class Army():
    def __init__(self, name):
        self.name = name
        self.groups = []
        
    
    def boost(self, amount):
        for group in self.groups:
            group.damage += amount
    
    def selectTargets(self, other):
        # Sort groups by effective power first, initiative second
        self.groups.sort(key=lambda x: (-x.effectivePower(), -x.init))
        targets = other.groups.copy()
        # Pick target group with weakness first (most damage), then highest
        # effective power; then initiative.
        targets.sort(key=lambda x: (-x.effectivePower(), -x.init))

        for group in self.groups:
            target = None
            # Pick the top other group that has weakness to this attack
            for othergroup in targets:
                 if group.damtype in othergroup.weaknesses:
                     target = othergroup
                     break

            
            # If there are no groups with this weakness; pick the top group 
            # that has no immunity
            if not target:
                for othergroup in targets:
                    if group.damtype not in othergroup.immunities:
                        target = othergroup
                        break
            

            group.target = target
            if target:
                targets.remove(target)
                     
        
    def removeGroups(self):
        self.groups = list(filter(lambda x: x.units > 0, self.groups))
                

    def __repr__(self):
        string = ''
        for group in self.groups:
            string += str(group) + '\n'
                 
        return(string)


def readInput(inputfile):
    file = open(inputfile).readlines()
    data = [x.strip() for x in file]
    
    immune = Army('Immune system')
    infection = Army('Infection')
    
    for line in data:
        if line == 'Immune System:':
            currentarmy = immune
            groupnumber = 1
        elif line == 'Infection:':
            currentarmy = infection
            groupnumber = 1
        elif line == '':
            pass
        else:
            currentarmy.groups.append(Group(line, groupnumber, currentarmy))
            groupnumber += 1            
    return immune, infection


def fight(immune, infection):
    prevunitsum = 0
    while (len(immune.groups) > 0 and len(infection.groups) > 0):
        # Target phase
        immune.selectTargets(infection)
        infection.selectTargets(immune)
        
        # Fighting phase
        allgroups = immune.groups + infection.groups
        allgroups.sort(key=lambda x: -x.init)
        
        unitsum = sum([grp.units for grp in allgroups])
        if unitsum == prevunitsum:
            print('Got stuck in a deadloop')
            return(None, False)            
        prevunitsum = unitsum
    
        for group in allgroups:
            group.attack()
            
        immune.removeGroups()
        infection.removeGroups()

    
    allgroups = immune.groups + infection.groups
    # Returns sum of leftover groups. Returns True if the immune system won
    return(sum([grp.units for grp in allgroups]), len(infection.groups)<len(immune.groups))

## Part 1
immune, infection = readInput('input.txt')
print('The answer to part 1: ', fight(immune, infection))

## Part 2
boost = 10000       # First guess
lower = 0           # Lower bound

for _ in range(100):
    immune, infection = readInput('input.txt')
    immune.boost(boost)
    
    if fight(immune, infection)[1]: # If the immune system wins
        upper = boost               # New upper bound
    else:                           # If the infection wins
        lower = boost               # New lower bound
        
    boost = (upper + lower)//2      # New guess

    if upper - lower == 1:
        immune, infection = readInput('input.txt')
        immune.boost(upper)
        print('The answer to part 2: ', fight(immune, infection))
        break
    print(boost)
