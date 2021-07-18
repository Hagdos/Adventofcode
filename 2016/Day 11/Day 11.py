import itertools
import copy

class Generator:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ''.join([self.name, 'Generator'])

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
        return ''.join([self.name, 'Microchip'])

    def __eq__(self, other):
        if isinstance(other, Microchip):
            if self.name == other.name:
                return True
            else:
                return False


class Floor:
    def __init__(self):
        self.components = []

    # Checks if there are microchips without an accompanying Generator on this Floor
    def checkFloor(self):
        generatorPresent = False
        singleMicrochipPresent = False
        for component in self.components:
            if type(component) is Generator:
                generatorPresent = True
            if type(component) is Microchip:
                if Generator(component.name) not in self.components:
                    singleMicrochipPresent = True

        if generatorPresent is True and singleMicrochipPresent is True:
            return False
        else:
            return True


class Diagram:
    def __init__(self):
        self.currentFloor = 0
        self.floors = []

    def currentfloor(self):
        return self.floors[self.currentFloor]

    def nextSteps(self):
        for nextFloor in [self.currentFLoor - 1, self.currentFloor + 1]:
            if nextFloor in range(4):
                for elevatorComponents in itertools.chain(itertools.combinations(self.currentfloor().components, 1),
                                          itertools.combinations(self.currentfloor().components, 2)):

                    nextDia = Diagram()
                    nextDia.floors = copy.deepcopy(self.floors)
                    for component in elevatorComponents:
                        nextDia.currentfloor().components.remove(component)
                        nextDia.floors[nextFloor].components.append(component)




file = open('input.txt')

dia = Diagram()

for line in file:
    floor = Floor()
    line = line.split(',')
    for component in line:
        component = component.split()
        if component[-1].strip('.') == 'generator':
            floor.components.append(Generator(component[-2]))
        elif component[-1].strip('.') == 'microchip':
            floor.components.append(Microchip(component[-2].split('-')[0]))
    dia.floors.append(floor)


# dia.nextSteps()
print(dia.currentfloor().checkFloor())

dia.currentfloor().components.append(Microchip('Bullshit'))
print(dia.currentfloor().components)

dia.currentfloor().components = [comp for comp in dia.currentfloor().components if isinstance(comp, Microchip)]


print(dia.currentfloor().components)
print(dia.currentfloor().checkFloor())
elevatorFloor = 0               #Floor the elevator currently is on
