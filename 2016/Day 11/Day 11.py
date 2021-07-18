import itertools
import copy
import time

class Generator:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ''.join([self.name, 'Gen'])
    
    def __hash__(self):
        return hash((self.name, 1))

    def __eq__(self, other):
        if isinstance(other, Generator):
            if self.name == other.name:
                return True
            else:
                return False


class Microchip:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ''.join([self.name, 'Chip'])
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Microchip):
            if self.name == other.name:
                return True
            else:
                return False


class Floor:
    def __init__(self, components):
        self.components = components
        self.countComponents()
        
    def countComponents(self):
        noGenerators = 0
        noMicrochips = 0
        for comp in self.components:
            if isinstance(comp, Generator):
                noGenerators += 1
            elif isinstance(comp, Microchip):
                noMicrochips += 1
            else:
                raise ValueError("Component in floor; not a generator or microchip")
        self.noGenerators = noGenerators
        self.noMicrochips = noMicrochips

    # Checks if there are microchips without an accompanying Generator on this Floor
    # Todo: Can be 
    def checkFloor(self):
        singleMicrochipPresent = False
        for component in self.components:
            if type(component) is Microchip:
                if Generator(component.name) not in self.components:
                    singleMicrochipPresent = True
                    break

        if self.noGenerators > 0 and singleMicrochipPresent is True:
            return False
        else:
            return True
        
    def __eq__(self, other):
        if isinstance(other, Floor):
            if len(self.components) == len(other.components):
                if self.noGenerators == other.noGenerators and self.noMicrochips == other.noMicrochips:
                    return True
                else:
                    return False
                
                
                # return all([comp in other.components for comp in self.components])
            else:
                return False
            
        else:
            return False
        
    def __repr__(self):
        names = [''.join([str(component), ' ']) for component in self.components]
        return ''.join(sorted(names))
        # return ''.join([''.join([str(component), ' ']) for component in self.components])
    
    def __hash__(self):
        return(hash(tuple(self.components)))


class Diagram:
    def __init__(self, elevatorposition, floors):
        self.elevatorPosition = elevatorposition
        self.floors = floors

    def currentfloor(self):
        return self.floors[self.elevatorPosition]
    
    def checkDiagram(self):
        for floor in self.floors:
            if not floor.checkFloor():
                return False
        return True

    def nextSteps(self):
        nextDias = []
        for newPosition in [self.elevatorPosition - 1, self.elevatorPosition + 1]:
            if newPosition in range(4):
                possibleCombinations = itertools.chain(itertools.combinations(self.currentfloor().components, 2),
                                            itertools.combinations(self.currentfloor().components, 1))
                for elevatorComponents in possibleCombinations:

                    newFloors = []
                    for i, floor in enumerate(self.floors):
                        if i == self.elevatorPosition:
                            components = set([comp for comp in floor.components if comp not in elevatorComponents])
                        elif i == newPosition:
                            components = set(floor.components)
                            [components.add(x) for x in elevatorComponents]
                        else:
                            components = floor.components
                        newFloors.append(Floor(components))
                        
                                           
                    nextDia = Diagram(newPosition, tuple(newFloors))
                    if nextDia.checkDiagram() is True:
                        nextDias.append(nextDia)
                        
        return(nextDias)     

    def checkDiagramFinished(self):
        if len(self.floors[3].components) == 10 and Pt2 is False:
            return True
        elif len(self.floors[3].components) == 14 and Pt2 is True:
            return True
        else:
            return False
    
    def __repr__(self):
        output = []
        for floor in range(3, -1, -1):
            output.append('Floor ')
            output.append(str(floor))
            output.append(':')
            if floor == self.elevatorPosition:
                output.append('*')
            else:
                output.append(' ')
            output.append(str(self.floors[floor]))
            output.append('\n')
            
        return ''.join(output)

    
    def __eq__(self, other):
        if isinstance(other, Diagram):
            if self.elevatorPosition == other.elevatorPosition:
                equalFloors = True
                for i, floor in enumerate(self.floors):
                    if floor != other.floors[i]:
                        equalFloors = False
                        break
                return equalFloors
            else:
                return False
        else:
            return False
                
                    
    
# =============================================================================
#     Create the first diagram
# =============================================================================
start = time.time()
Pt2 = True
file = open('input.txt')
# file = open('testinput.txt')


floors = []
for line in file:
    floorcomponents = set()
    line = line.split(',')
    for component in line:
        component = component.split()
        if component[-1].strip('.') == 'generator':
            floorcomponents.add(Generator(component[-2][0:3]))
        elif component[-1].strip('.') == 'microchip':
            floorcomponents.add(Microchip(component[-2].split('-')[0][0:3]))
    floors.append(Floor(floorcomponents))
    
firstdia = Diagram(0, tuple(floors))

if Pt2 is True:
    firstdia.floors[0].components.add(Generator('ele'))
    firstdia.floors[0].components.add(Microchip('ele'))
    firstdia.floors[0].components.add(Generator('dil'))
    firstdia.floors[0].components.add(Microchip('dil'))
    
# print(firstdia)
# =============================================================================
#   Create array of all visited diagrams, and an array of the diagrams at the front of the search path
# =============================================================================

allDias = [firstdia]
searchList = [(firstdia,  0, [])]

# =============================================================================
#   Loop through the list of diagrams; pick the one with the least steps, and create new ones from there.
# =============================================================================
i = 0
Found = False
while Found == False and i < 3:
    i+= 1
    
    shortestPath = 1000000
    shortestDia = None
    
    for (dia, steps, prevdias) in searchList:
        if steps < shortestPath:
            shortestPath = steps
            shortestDia = dia
            shortestPrevDias = prevdias
        
    newDias = shortestDia.nextSteps()
    
    for newDia in newDias:
        if newDia not in allDias:
            allDias.append(newDia)
            prevdias = copy.deepcopy(shortestPrevDias)
            prevdias.append(shortestDia)
            searchList.append((newDia, shortestPath + 1, prevdias))
            if newDia.checkDiagramFinished() is True:
                Found = True
                print('Solution found, number of steps is: ', shortestPath+1)
                break
            
    searchList.remove((shortestDia, shortestPath, shortestPrevDias))


# =============================================================================
# Testshizzle
# =============================================================================
print("Timing: ", time.time()-start)
