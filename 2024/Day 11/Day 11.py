from collections import defaultdict

def solve(stones, iterations):
    for i in range(iterations):
        newstones = defaultdict(int)
        for stone in stones.keys():

            n = len(str(stone))
            if stone == 0:
                newstones[1] += stones[stone]

            elif n % 2 == 0:
                newstones[stone//10**(n//2)] += stones[stone]
                newstones[stone%10**(n//2)] += stones[stone]

            else:
                newstones[stone*2024] += stones[stone]

        stones = newstones.copy()

    return stones


def solve2(stones, iterations):
    ans = 0
    for stone in stones:
        ans += countStones(stone, iterations)

    return ans


countStonesMemo = {}
def countStones(stone, iterations):
    if iterations == 0:
        return 1

    if (stone, iterations) not in countStonesMemo:
        n = len(str(stone))

        if stone == 0:
            countStonesMemo[(stone, iterations)] = countStones(1, iterations-1)
        elif n % 2 == 0:
            countStonesMemo[(stone, iterations)] = (countStones(stone // 10 ** (n // 2), iterations-1) +
                                                    countStones(stone % 10 ** (n // 2), iterations-1))
        else:
            countStonesMemo[(stone, iterations)] = countStones(stone*2024, iterations-1)

    return countStonesMemo[(stone, iterations)]


file = open('input.txt').read()

stones = {int(x): 1 for x in file.strip().split()}

# ans1 = sum(solve(stones, 25).values())
# ans2 = sum(solve(stones, 75).values())
# print('The answer to part 1: ', ans1)
# print('The answer to part 2: ', ans2)

ans1 = solve2(stones, 25)
ans2 = solve2(stones, 75)
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
