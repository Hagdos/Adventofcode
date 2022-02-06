import time

def insertRight(marbles, current, toplace):
    left = current
    right = marbles[current][1]

    marbles[toplace] = [left, right]
    marbles[left][1] = toplace
    marbles[right][0] = toplace

    return toplace

def removeMarble(marbles, toremove):
    left = marbles[toremove][0]
    right = marbles[toremove][1]

    marbles[left][1] = right
    marbles[right][0] = left

    marbles[toremove] = [-1, -1]

    return right

# Move n marbles to the left
def moveLeft(marbles, current, n):
    for _ in range(n):
        current = marbles[current][0]

    return current

current = 0
currentPlayer = 0

players = 435
last = 71184
last2 = last * 100

marbles = [[-1, -1] for _ in range(last2+1)]
marbles[0] = [0, 0]

scores = [0] * players

start = time.time()

for marble in range(1, last2+1):
    currentPlayer += 1
    currentPlayer %= players

    if marble % 23:
        current = marbles[current][1]
        current = insertRight(marbles, current, marble)
    else:
        scores[currentPlayer] += marble

        current = moveLeft(marbles, current, 7)
        scores[currentPlayer] += current
        current = removeMarble(marbles, current)

    if marble == last:
        print(f'The answer to part 1: {max(scores)}')

print(f'The answer to part 2: {max(scores)}')
print(f'{time.time() - start}')