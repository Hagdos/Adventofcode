PASS = 0
CORRECT = 1
FALSE = 2


def compareIntegers(l, r):
    if l > r:
        return FALSE
    elif l < r:
        return CORRECT
    else:
        return PASS


def comparelistlengths(l, r):
    return compareIntegers(len(l), len(r))


def comparePackets(pair):
    left = pair[0]
    right = pair[1]
    c = 0
    while(c < len(left) and c < len(right)):
        l = left[c]
        r = right[c]

        if isinstance(l, int) and isinstance(r, int):
            result = compareIntegers(l, r)

        elif isinstance(l, list) or isinstance(r, list):
            # Make integers into lists; keep lists the same
            l = [l] if isinstance(l, int) else l
            r = [r] if isinstance(r, int) else r
            result = comparePackets((l, r))

        else:
            print("Something went wrong")
            raise ValueError

        if result in [CORRECT, FALSE]:
            return result
        else:
            c += 1

    # Full list length has been compared:
    return comparelistlengths(left, right)


def part1(filename):
    file = open(filename).read().split('\n\n')
    # pairs = [tuple(eval(y) for y in x.strip().split('\n')) for x in file]
    pairs = [tuple(listParser(y) for y in x.strip().split('\n')) for x in file]
    ans1 = 0

    for i in range(len(pairs)):
        if comparePackets(pairs[i]) == CORRECT:
            ans1 += i+1

    return ans1


def part2(filename):
    file = open(filename).read().split('\n')
    packets = []
    for line in file:
        if line:
            packets.append(listParser(line))
    # packets.append([[2]])
    # packets.append([[6]])
    p1 = p2 = 1
    for packet in packets:
        if comparePackets((packet, [[2]])) == CORRECT:
            p1 += 1
        if comparePackets((packet, [[6]])) == CORRECT:
            p2 += 1

    if comparePackets(([[2]], [[6]])) == CORRECT:
        p2 += 1
    else:
        p1 += 1

    return p1 * p2


def listParser(string, i=0):
    currentList = []
    currentNumber = []
    while(i < len(string)):
        i += 1
        char = string[i]
        # print(char)
        if char == '[':
            list, i = listParser(string, i)
            currentList.append(list)
        elif char.isnumeric():
            currentNumber.append(char)
        elif char in [',', ']']:
            if currentNumber:
                currentList.append(int(''.join(currentNumber)))
                currentNumber = []
            if char == ']':
                return currentList, i


print('The answer to part 1: ', part1('2022/Day 13/input.txt'))
print('The answer to part 2: ', part2('2022/Day 13/input.txt'))
