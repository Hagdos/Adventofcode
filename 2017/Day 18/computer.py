class Computer:
    def __init__(self, registernames, instructions):
        self.pointer = 0
        self.registers = {'Counter': 0}
        for name in registernames:
            self.registers[name] = 0
        self.queue = []
        self.instructions = instructions

    def run1(self):
        while True:
            cmd, val1, val2, reg1 = self.decode()
            if cmd == 'snd':
                self.registers['sound'] = val1
            elif cmd == 'set':
                self.registers[reg1] = val2
            elif cmd == 'add':
                self.registers[reg1] += val2
            elif cmd == 'mul':
                self.registers[reg1] *= val2
            elif cmd == 'mod':
                self.registers[reg1] %= val2
            elif cmd == 'rcv':
                return self.registers['sound']
            elif cmd == 'jgz':
                if val1 > 0:
                    self.pointer += val2 - 1
            self.pointer += 1

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
