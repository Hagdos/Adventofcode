snafu2intSymbols = {'2': 2,
                '1': 1,
                '0': 0,
                '-': -1,
                '=': -2}

int2snafuSymbols = {2: '2',
                    1: '1',
                    0: '0',
                    -1: '-',
                    -2: '='}

def snafu2int(s):
    s = s[::-1]
    i = 0
    for n, char in enumerate(s):
        i += snafu2intSymbols[char] * (5 ** n)

    return i


def int2snafu(i):
    s = []
    while i != 0:
        n = i % 5
        if n > 2:
            n -= 5


        s.append(int2snafuSymbols[n])
        i -= n
        i = i // 5

    s = ''.join(s[::-1])
    return s


def part1(filename):
    file = open(filename).readlines()

    integers = [snafu2int(s.strip()) for s in file]

    return int2snafu(sum(integers))


print(part1('input.txt'))
