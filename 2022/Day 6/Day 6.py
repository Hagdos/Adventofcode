import time


def findPatternWithoutRepetition(data, length):
    for i in range(len(data)):
        repetition = False
        for j in range(length):
            if data[i+j] in data[i+j+1:i+length]:
                repetition = True
                break
        if not repetition:
            return i+length


def findPatternWithoutRepetition2(data, length):
    for i in range(len(data)):
        s = set(data[i:i+length])
        if len(s) == length:
            return i+length


def findPatternWithoutRepetition3(data, length):
    i = 0
    # for i in range(len(data)):
    while i < len(data):
        # print(i)
        repetition = False
        for j in range(length):
            if data[i+j] in data[i+j+1:i+length]:
                i += j + 1
                repetition = True
                break
        if not repetition:
            return i+length


data = open('2022/Day 6/input.txt').read().strip()

print('The answer to part 1: ', findPatternWithoutRepetition(data, 4))
print('The answer to part 2: ', findPatternWithoutRepetition3(data, 14))
#
start = time.time()
for _ in range(10000):
    findPatternWithoutRepetition(data, 14)
print(time.time()-start)

start = time.time()
for _ in range(10000):
    findPatternWithoutRepetition2(data, 14)
print(time.time()-start)

start = time.time()
for _ in range(10000):
    findPatternWithoutRepetition3(data, 14)
print(time.time()-start)
