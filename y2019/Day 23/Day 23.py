import intcode as ic

class Computer:
    def __init__(self, mem, address):
        self.mem = mem
        self.address = address
        self.inputs = [address]
        # self.instruction_pointer = 0
        # self.relbase = 0
        self.inputcounter = 0
        # self.loopcounter = 0
        self.finished = False
        
    def addinput(self, packages):
        if packages:
            for package in packages:
                self.inputs.append(package)
        else:
            self.inputs.append(-1)
                
        
    def run(self):
        self.counters = [0, 0, self.inputcounter, 0]
        self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)
    
    def __repr__(self):
        return "Computer " + str(self.address)
        

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)

number_of_computers = 50
computers = []
packages = {}
new_packages = {}
for n in range(number_of_computers):
    computers.append(Computer(mem, n))
    packages[computers[n]] = []
    
computers[0].addinput([-1])
    
for _ in range(10):
    for computer in computers:
        computer.addinput(packages[computer])
        packages[computer] = []
        computer.run()
        print(computer)
        print(computer.inputs)
        print(computer.outputs)
        print()
        
        for p in range(0, len(computer.outputs), 3):
            packages[computers[computer.outputs[p]]].extend(computer.outputs[p+1:p+3])
            # computers[computer.outputs[p]].addinput(computer.outputs[p+1:p+3])  

    

# inputs = [41, 183922, 29]
# counters = [0, 0, 0, 0]
# mem, outputs, counters, finished = ic.runintcode(mem, inputs, counters)

# print(outputs, finished)