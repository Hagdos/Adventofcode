class Bot:
    def __init__(self, botNumber):
        self.chips = []
        self.outputs = [None, None]
        self.botNumber = botNumber
        
    def addOutputs(self, outputs):
        self.outputs = outputs
        if len(self.chips) >= 2:
            self.giveChips()
    
    def addChip(self, chip):
        self.chips.append(chip)
        if self.chips == [61, 17]:
            print('The answer to Part 1:', self.botNumber)
                
        if len(self.chips) >= 2 and None not in self.outputs:
            self.giveChips()

    
    def giveChips(self):
        self.giveChip(self.outputs[0], min(self.chips))
        self.giveChip(self.outputs[1], max(self.chips))
        self.chips = []
    
    
    def giveChip(self, output, chip):
        # print(self.outputs)
        outputType = output[0]
        outputValue = int(output[1])
        
        if outputType == 'bot':
            # print(outputValue)
            bots[outputValue].addChip(chip)
        elif outputType == 'output':
            outputs[outputValue] = chip
                
        
#Set up the empty bots and the empty output
bots = []
outputs = []

for i in range(210):
    bots.append(Bot(i))
    outputs.append(None)
    
file = open('input.txt')

for line in file:
    # print(line)
    line = line.strip().split()
    
    if line[0] == 'value':
        botnumber = int(line[-1])
        chip = int(line[1])
        bots[botnumber].addChip(chip)
        
    if line[0] == 'bot':
        botnumber = int(line[1])
        bots[botnumber].addOutputs([line[5:7], line[-2:]])
        # bots[botnumber].outputs = [line[5:7], line[-2:]]
            
ans2 = outputs[0]*outputs[1]*outputs[2]
print("The answer to Part 2:", ans2)