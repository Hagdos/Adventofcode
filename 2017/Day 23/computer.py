class Computer:
    def __init__(self, registernames, instructions):
        self.pointer = 0
        # self.registers = {'Counter': 0}
        self.registers = dict()
        for name in registernames:
            self.registers[name] = 0
        self.queue = []
        self.instructions = instructions
   
# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

    def run1(self, iterations, debug=False):
        ans1 = 0
        counter = 0
        while self.pointer < len(self.instructions) and counter < iterations:
            cmd, val1, val2, reg1 = self.decode()
            if cmd == 'set':
                self.registers[reg1] = val2
            elif cmd == 'sub':
                self.registers[reg1] -= val2
            elif cmd == 'mul':
                self.registers[reg1] *= val2
                ans1 += 1
            elif cmd == 'jnz':
                if val1 != 0:
                    if debug:
                        print(cmd, self.pointer, self.instructions[self.pointer], self.registers)
                    self.pointer += val2
                    counter += 1
                    continue
            else:
                print('unknown command', cmd)
                
            if debug:
                print(cmd, self.pointer, self.instructions[self.pointer], self.registers)    
            self.pointer += 1
            counter += 1
        
            
        
        if counter == iterations:
            return 'Failed', 'Failed'
        
        return ans1, self.registers['h']


    def run2(self, otherqueue):
        while True:
            cmd, val1, val2, reg1 = self.decode()
            if cmd == 'snd':
                self.queue.append(val1)
                self.registers['Counter'] += 1
            elif cmd == 'set':
                self.registers[reg1] = val2
            elif cmd == 'add':
                self.registers[reg1] += val2
            elif cmd == 'mul':
                self.registers[reg1] *= val2
            elif cmd == 'mod':
                self.registers[reg1] %= val2
            elif cmd == 'rcv':
                try:
                    self.registers[reg1] = otherqueue.pop(0)
                except IndexError:
                    return self.queue
            elif cmd == 'jgz':
                if val1 > 0:
                    self.pointer += val2 - 1
            self.pointer += 1

    def decode(self):
        instruction = self.instructions[self.pointer]
        cmd = instruction[0]
        reg1 = instruction[1]
        try:
            value1 = int(reg1)
        except ValueError:
            value1 = self.registers[reg1]
        try:
            value2 = int(instruction[2])
        except ValueError:
            value2 = self.registers[instruction[2]]
        except IndexError:
            value2 = None
        return cmd, value1, value2, reg1

    def __repr__(self):
        return ', '.join([str(i) for i in self.queue])
