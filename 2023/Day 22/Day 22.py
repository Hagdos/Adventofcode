from collections import defaultdict

class Part:
    def __init__(self, blocks, name):
        self.blocks = blocks
        self.name = name

    def height(self):
        return min([b.height() for b in self.blocks])

    def setheight(self, height):
        delta = height - self.height()
        for b in self.blocks:
            b.z += delta

    def __repr__(self):
        return chr(self.name)

class Block:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def location(self):
        return (self.x, self.y)

    def height(self):
        return self.z

def calcFallingParts(part):
    edge = [part]
    removedparts = set()

    while edge:
        p = edge.pop()
        removedparts.add(p)
        for pabove in partsabove[p]:
            if all([supportingpart in removedparts for supportingpart in partsbelow[pabove]]):
                edge.append(pabove)
                removedparts.add(pabove)

    return len(removedparts)-1


file = open('input.txt').readlines()
ans1 = ans2 = 0

data = [x.strip().split('~') for x in file]

parts = []
name = ord('A')-1

for part in data:
    name += 1
    start = [int(i) for i in part[0].split(',')]
    end = [int(i) for i in part[1].split(',')]

    blocks = []
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            for z in range(start[2], end[2]+1):
                blocks.append(Block(x,y,z))
    parts.append(Part(blocks, name))

parts.sort(key=lambda part: part.height())

ground = defaultdict(int)
highestpart = dict()

nonremovableparts = set()
supportingpartscounter = defaultdict(set)

partsabove = defaultdict(set)
partsbelow = defaultdict(set)

for part in parts:
    # Calculate how far this part will fall,and set it to that height
    newheight = 0
    for block in part.blocks:
        newheight = max(newheight, ground[block.location()]+1)

    part.setheight(newheight)

    # Determine what parts are supporting it
        #If a part is only supported by a single other part, that part cannot be removed, so add it to a list
    supportingparts = set()
    for block in part.blocks:
        if ground[block.location()] > 0 and ground[block.location()] == block.height()-1:
            partsbelow[part].add(highestpart[block.location()])
            partsabove[highestpart[block.location()]].add(part)

    if len(partsbelow[part]) == 1:
        nonremovableparts.add(list(partsbelow[part])[0])

    # Update the ground and part dictionaries:
    for block in sorted(part.blocks, key=lambda block: block.height()):
        ground[block.location()] = block.height()
        highestpart[block.location()] = part

print('The answer to part 1: ', len(parts)-len(nonremovableparts))

for part in parts:
    ans2 += calcFallingParts(part)


print('The answer to part 2: ', ans2)

#  1338 is too low

# set.discard()