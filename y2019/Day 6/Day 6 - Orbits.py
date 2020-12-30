f = open('orbits.txt')

moons = {}

for line in f:
    (key, value) = line.strip().split(')')
    if key in moons:
        moons[key].append(value)
    else:
        moons[key] = [value]

orbits = {}
paths = {}

def calcplanets(motherplanet):
    for planet in moons[motherplanet]:
        orbits[planet] = orbits[motherplanet] + 1
        paths[planet] = [motherplanet] + paths[motherplanet]
        if planet in moons: 
            calcplanets(planet)
            
        # if planet in planetpaths:
        #     planetpaths[planet]
        
orbits['COM'] = 0
paths['COM'] = []
calcplanets('COM')

ans = 0
for o in orbits:
    ans += orbits[o]
    
# print(ans)

for steps, planet in enumerate(paths['YOU']):
    if planet in paths['SAN']:
        # print(steps, planet)
        break
    

steps2 = paths['SAN'].index(planet)

print(steps + steps2)


# =============================================================================
# Part 2 
# =============================================================================

