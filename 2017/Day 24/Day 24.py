import time

class Bridge():
    def __init__(self, components, head):
        self.components = components
        self.head = head
        
    def calcstrength(self):
        strength = 0
        for comp in self.components:
            for value in comp:
                strength += value
        
        return strength
    
    def calclength(self):
        return len(self.components)
    
    def __repr__(self):
        l = [str(comp) for comp in self.components]
        return 'Bridge: ' + ', '.join(l) + ', head: ' + str(self.head)

file = open('input.txt').readlines()

comps = [tuple(int(i) for i in x.strip().split('/')) for x in file]

bridges = [Bridge([], 0)]
newbridges = []
allbridges = []

start = time.time()

while(bridges):
    for bridge in bridges:
        # First check if a symmetric component is available. If so; add that 
        # and skip all other versions
        symcomp = (bridge.head, bridge.head)
        if symcomp in comps and symcomp not in bridge.components:        
                newbridges.append(Bridge(bridge.components + [symcomp], bridge.head))
        # Otherwise; check which components fit and are not in the bridge already
        else:
            for comp in comps:
                if bridge.head in comp and comp not in bridge.components:
                    # And create a new bridge with this component added
                    for side in comp:
                        if side != bridge.head:
                            newhead = side
                    newbridges.append(Bridge(bridge.components + [comp], newhead))
        
    allbridges = allbridges + newbridges
    bridges = newbridges
    newbridges = []

ans1 = 0
ans2 = 0
maxlength = allbridges[-1].calclength()
for bridge in allbridges:
    if bridge.calcstrength() > ans1:
        ans1 = bridge.calcstrength()
    if bridge.calclength() >= maxlength:
        if bridge.calcstrength() > ans2:
            ans2 = bridge.calcstrength()



print('This took', time.time()-start, 'seconds')

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
