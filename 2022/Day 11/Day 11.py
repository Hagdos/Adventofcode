import time

class Monkey():
    def __init__(self, items, operation, test, nextMonkeys):
        self.items = items
        self.operation = operation
        self.test = test
        self.nextMonkeys = nextMonkeys
        self.inspecteditems = 0


    def playRound1(self, monkeys):
        # self.items = [eval(self.operation) // 3 for old in self.items]
        self.items = [self.operation(old) // 3 for old in self.items]
        self.distributeItems(monkeys)


    def playRound2(self, monkeys, modulo):
        # self.items = [eval(self.operation) % modulo for old in self.items]
        self.items = [self.operation(old) % modulo for old in self.items]
        self.distributeItems(monkeys)


    def distributeItems(self, monkeys):
        while self.items:
            self.inspecteditems += 1
            item = self.items.pop(0)
            if not(item % self.test):
                monkeys[self.nextMonkeys[0]].items.append(item)
            else:
                monkeys[self.nextMonkeys[1]].items.append(item)


def readInput(file):
    monkeydata = open(file).read().split('\n\n')
    monkeys = []
    commonmultiple = 1
    for monkey in monkeydata:
        data = monkey.split('\n')
        items = [int(i) for i in data[1][17:].split(', ')]
        operation = data[2].strip().split(': ')[1].split(' = ')[-1]
        operation = lambda old :eval(operation)
        test = int(data[3].strip().split(' ')[-1])
        commonmultiple *= test
        nextMonkeys = (int(data[4].split(' ')[-1]), int(data[5].split(' ')[-1]))

        monkeys.append(Monkey(items, operation, test, nextMonkeys))
    return monkeys, commonmultiple



def calcScore(monkeys):
    scores = sorted([m.inspecteditems for m in monkeys])
    return scores[-1] * scores[-2]


def Part1(file):
    monkeys, divisor = readInput(file)

    for _ in range(20):
        for m in monkeys:
            m.playRound1(monkeys)

    print(monkeys[0].operation(3))

    return calcScore(monkeys)


def Part2(file):
    monkeys, commonmultiple = readInput(file)

    for _ in range(10000):
        for m in monkeys:
            m.playRound2(monkeys, commonmultiple)

    return calcScore(monkeys)

start = time.time()

print('The answer to part 1: ', Part1('input.txt'))
# print('The answer to part 2: ', Part2('input.txt'))

print(f'This took {time.time()-start} seconds')

# The answer to part 1:  66802
# The answer to part 2:  21800916620
# This took 4.614102363586426 seconds