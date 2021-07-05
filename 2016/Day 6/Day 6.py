import string

file = open('input.txt').read().split()

positions = []
for i in range(8):
    positions.append([])

for transmission in file:
    for i in range(8):
        positions[i].append(transmission[i])

message = []
message2 = []
for position in positions:
    maxCount = 0
    minCount = 1000
    bestLetter = '.'
    worstLetter = '.'
    for letter in string.ascii_lowercase:
        if position.count(letter) > maxCount:
            bestLetter = letter
            maxCount = position.count(letter)
        if position.count(letter) < minCount:
            worstLetter = letter
            minCount = position.count(letter)

    message.append(bestLetter)
    message2.append(worstLetter)

print('Answer to Part 1:', ''.join(message))
print('Answer to Part 2:', ''.join(message2))