from collections import defaultdict

class Message():
    def __init__(self, sender, receiver, pulse):
        self.sender = sender
        self.receiver = receiver
        self.pulse = pulse


class Module():
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def sendMessages(self, pulse):
        messages = []
        for o in self.outputs:
            messages.append(Message(self.name, o, pulse))
        return messages


class Flipflop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.state = False
        self.type = 'Flipflop'

    def receiveMessage(self, message):
        if message.pulse == False:
            self.state = not self.state
            return self.sendMessages(self.state)
        return []

class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.type = 'Conjuction'

    def addInputs(self, inputs):
        self.states = {i: False for i in inputs}

    def receiveMessage(self, message):
        self.states[message.sender] = message.pulse

        return self.sendMessages(not all(self.states.values()))

class Broadcast(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.type = 'Broadcast'

    def receiveMessage(self, message):
        return self.sendMessages(message.pulse)


file = open('input.txt').readlines()

inputs = defaultdict(list)
modules = dict()

for line in file:
    name, outputs = line.strip().split(' -> ')
    mtype, name = name[0], name[1:]
    outputs = outputs.split(', ')

    for o in outputs:
        inputs[o].append(name)

    if mtype == '%':
        modules[name] = Flipflop(name, outputs)
    elif mtype == '&':
        modules[name] = Conjunction(name, outputs)
    elif mtype == 'b':
        modules[name] = Broadcast(name, outputs)
    else:
        raise ValueError


for i in inputs.keys():
    if i in modules:
        if modules[i].type == 'Conjuction':
            modules[i].addInputs(inputs[i])

firstMessage = Message('Button', 'roadcaster', False)
highs = lows = 0
iterator = defaultdict(int)

for buttonpresses in range(1, 10000):
    messages = [firstMessage]
    pointer = 0
    while pointer < len(messages):
        message = messages[pointer]
        pointer += 1

        if message.pulse:
            highs += 1
        else:
            lows += 1

        if message.receiver == 'rx':
            continue

        if message.sender in ['tx', 'dd', 'nz', 'ph']:
            if message.pulse:
                iterator[message.sender] = buttonpresses
            if len(iterator) == 4:
                ans2 = 1
                for v in iterator.values():
                    ans2 *= v
                print('The answer to part 2: ', ans2)
                break
        messages += modules[message.receiver].receiveMessage(message)

    if buttonpresses == 999:
        print('The answer to part 1: ', highs*lows)
    if len(iterator) == 4:
        break