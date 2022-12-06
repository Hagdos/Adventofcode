def findPatternWithoutRepetition(data, length):
    for i in range(len(data)):
        repetition = False
        for j in range(length):
            if data[i+j] in data[i+j+1:i+length]:
                repetition = True
                break
        if not repetition:
            return i+length


data = open('2022/Day 6/input.txt').read().strip()

print('The answer to part 1: ', findPatternWithoutRepetition(data, 4))
print('The answer to part 2: ', findPatternWithoutRepetition(data, 14))
