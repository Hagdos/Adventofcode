adapters = [int(j.strip()) for j in open('Day 10/input.txt')]

adapters.sort()
adapters.insert(0, 0)
device = adapters[-1]+3
adapters.append(device)

differences = {1: 0, 2: 0, 3: 0}

for adapter1, adapter2 in zip(adapters[:-1], adapters[1:]):
    difference = adapter2 - adapter1
    differences[difference] += 1


print("The answer to part 1:", differences[1]*differences[3])

arrangements = dict.fromkeys(adapters, 0)
arrangements[0] = 1

for adapter in arrangements:
    for nextAdapter in range(adapter+1, adapter+4):
        if nextAdapter in arrangements:
            arrangements[nextAdapter] += arrangements[adapter]


print("The answer to part 2:", arrangements[device])
