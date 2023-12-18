def HASH(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def calcScore(boxes):
    score = 0
    for b, box in enumerate(boxes):
        for l, lens in enumerate(box):
            score += (b+1) * (l+1) * box[lens]
    return score

instructions = open('input.txt').readline().strip().split(',')
ans1 = ans2 = 0

boxes = [dict() for _ in range(256)]
for instruction in instructions:
    ans1 += HASH(instruction)
    if instruction[-1] == '-':
        label = instruction[:-1]
        box = HASH(label)
        boxes[box].pop(label, None)
    else:
        label, focal = instruction.split('=')
        box = HASH(label)
        boxes[box][label] = int(focal)




print('The answer to part 1: ', ans1)
print('The answer to part 2: ', calcScore(boxes))
