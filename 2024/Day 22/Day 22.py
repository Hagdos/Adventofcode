from collections import defaultdict, deque


def evolve(number):
    # prune = 2**24
    number = (number ^ number << 6) & 2**24-1
    number = (number ^ number >> 5)
    number = (number ^ number << 11) & 2**24-1

    return number


file = open('input2.txt').readlines()

data = [int(x.strip()) for x in file]
ans1 = ans2 = 0

# Dictionary that keeps track of how many bananas can be earned for each possible sequence
sequences = defaultdict(int)

for p, number in enumerate(data):
    deltas = deque([0]*4, maxlen=4)  # Keep track of the last 4 price differences
    prevprice = number % 10

    seen = set()  # Keep track of which sequences we've already seen at this buyer; to prevent buying twice.

    for i in range(2000):
        number = evolve(number)
        price = number % 10
        # deltas.popleft() # No longer necessary with maxlen=4
        deltas.append(price-prevprice)
        prevprice = price

        c = tuple(deltas)
        if i >= 3 and c not in seen:
            seen.add(c)
            sequences[c] += price

    ans1 += number

ans2 = max(sequences.values())

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

