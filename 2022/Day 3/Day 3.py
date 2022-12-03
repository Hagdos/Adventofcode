file = open('2022/Day 3/input.txt').readlines()
backpacks = [x.strip() for x in file]

ans1 = ans2 = 0
for pack in backpacks:
    part1 = pack[:len(pack)//2]
    part2 = pack[len(pack)//2:]
    assert part1+part2 == pack
    for item in part1:
        if item in part2:
            if item.isupper():
                ans1 += ord(item)-ord('A')+27
            elif item.islower():
                ans1 += ord(item)-ord('a')+1
            else:
                raise ValueError
            break

# Part 2
for group in range(0, len(backpacks), 3):
    for item in backpacks[group]:
        if item in backpacks[group+1] and item in backpacks[group+2]:
            if item.isupper():
                ans2 += ord(item)-ord('A')+27
            elif item.islower():
                ans2 += ord(item)-ord('a')+1
            break

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
