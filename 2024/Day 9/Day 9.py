class Block:
    def __init__(self, position, length, value=None):
        self.position = position  # Starting position of the block
        self.length = length
        self.value = value

    def checksum(self):
        return ((self.position + (self.position+self.length-1)) * self.length * self.value)//2


    def __repr__(self):
        return f"{self.position, self.length, self.value}"


data = open('input.txt').read().strip()


ans1 = ans2 = 0

# Part 1
blocks = []
zeroblocks = []
position = 0

for i, length in enumerate(data):
    if i % 2:
        zeroblocks.append(Block(position, int(length)))
    else:
        blocks.append(Block(position, int(length), i//2))
    position += int(length)

movingblock = blocks.pop()
newblocks = []

for zblock in zeroblocks:

    if zblock.position >= movingblock.position:
        blocks.append(movingblock)
        break

    # Add blocks from the left into the empty block
    while movingblock.length <= zblock.length:

        movingblock.position = zblock.position
        zblock.length -= movingblock.length
        zblock.position += movingblock.length

        newblocks.append(movingblock)
        movingblock = blocks.pop()

        if zblock.position >= movingblock.position:
            break

    if zblock.position >= movingblock.position:
        blocks.append(movingblock)
        break

    # For the remainder, split the movingblock into two block
    if zblock.length != 0:
        newblock = Block(zblock.position, zblock.length, movingblock.value)
        newblocks.append(newblock)

        # The current moving block is shortened, but used in the next iteration
        movingblock.length -= zblock.length


for block in blocks + newblocks:
    ans1 += block.checksum()


# Part 2
# data = "12345"
# data = "2333133121414131402"

blocks = []
zeroblocks = []
position = 0

for i, length in enumerate(data):
    if i % 2:
        zeroblocks.append(Block(position, int(length)))
    else:
        blocks.append(Block(position, int(length), i//2))
    position += int(length)

newblocks = []

for block in blocks[::-1]:
    for zblock in zeroblocks:
        if block.position < zblock.position:
            break
        if block.length <= zblock.length:
            block.position = zblock.position
            zblock.length -= block.length
            zblock.position += block.length
            break
    newblocks.append(block)


for block in newblocks:
    ans2 += block.checksum()


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
