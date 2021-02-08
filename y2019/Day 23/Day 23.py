import intcode as ic

class Computer:
    def __init__(self, mem, address):
        self.mem = mem.copy()
        self.address = address
        self.inputs = [address]
        self.inputcounter = 0
        self.counters = [0, 0, 0, 0]
        self.finished = False
        
    #Checks if there's new input for this computer; and adds it to the inputs
    def addinput(self, packages):
        if packages:
            for package in packages:
                self.inputs.append(package)
        #If there are no new packages, it will add -1 to the inputs-list once.
        else:
            if self.inputs[-1] != -1:
                self.inputs.append(-1)
    
    #Run checks if there are new inputs; if there are it runs the int-code with the existing counters and inputs. Otherwise it sets the output to 0; to prevent packages being added to the queues twice
    def run(self):
        if len(self.inputs) > self.inputcounter:
            # self.counters = [self.instruction_pointer, self.relbase, self.inputcounter, 0]
            self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)
            self.inputcounter = self.counters[2]
        else:
            self.outputs = []
    
    def __repr__(self):
        return "Computer " + str(self.address)
        

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)

number_of_computers = 50
computers = []
packages = {}
NAT_Ys = []

#Create the list of computers in the network; and fill the package dictionary with empty lists
for n in range(number_of_computers):
    computers.append(Computer(mem, n))
    packages[computers[n]] = []
    
while(True):
    idle = True         #If not set to false; the computers are idle
    
    #Loop over all computers; handle them 1 by 1
    for computer in computers:
        #Add any packages in their queue to the inputs-list.
        computer.addinput(packages[computer])
        #Clear the package queue
        packages[computer] = []
        computer.run()
        
        #Loop over the outputs of the computer that just ran        
        for p in range(0, len(computer.outputs), 3):
            #If the address is 255; the X-Y-values are stored in the NAT
            if computer.outputs[p] == 255:
                X = computer.outputs[p+1]
                Y = computer.outputs[p+2]
                NAT = [X, Y]
            #Otherwise they are added to the package queue of the relevant computer
            else:
                idle = False            #Set idle to false; outputs are still happening this circle
                packages[computers[computer.outputs[p]]].extend(computer.outputs[p+1:p+3])
    
    #If there are no more packages; the values in the NAT are sent to the first computer
    if idle:
        packages[computers[0]].extend(NAT)
        if NAT[1] in NAT_Ys:                    #Y-value sent for the second time; the value we had to find.
            break
        NAT_Ys.append(Y)                        #Add Y-value that's sent out to the list; to check against next time around

    
print("Answer to Part 1", NAT_Ys[0])

print("Answer to Part 2", NAT_Ys[-1])

# 25305 is too high