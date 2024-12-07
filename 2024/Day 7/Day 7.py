def concat(n1, n2):
    e = 1
    while n2 // e != 0:
        e *= 10
    return n1 * e + n2


def reverseconcat(n1, n2):
    e = 1
    while n2 // e != 0:
        e *= 10

    if n1 % e == n2:
        return n1//e
    return None


# Slow, dumb way to solve it.
def solve1(data):
    part2 = True
    ans = 0

    for eq in data:
        # print(eq)
        result = int(eq[0])
        numbers = [int(i) for i in eq[1].split()]

        results = {numbers[0]}

        for n in numbers[1:]:
            newresults = set()
            for r in results:
                new = r+n
                if new <= result:
                    newresults.add(new)
                new = r*n
                if new <= result:
                    newresults.add(new)
                if part2:
                    new = concat(r, n)
                    if new <= result:
                        newresults.add(new)
            results = newresults

        if result in results:
            ans += result

    return ans


# Faster way to solve it, going from the result on backwards and only allowing
# moves that are possible
def solve2(data):
    part2 = True
    ans = 0

    for eq in data:
        result = int(eq[0])
        numbers = [int(i) for i in eq[1].split()]

        results = {result}

        for n in numbers[::-1]:
            newresults = set()
            for r in results:
                if r - n >= 0:
                    newresults.add(r-n)
                if r % n == 0:
                    newresults.add(r//n)
                if part2:
                    new = reverseconcat(r, n)
                    if new:
                        newresults.add(new)

            results = newresults

        if 0 in results:
            ans += result

    return ans


file = open('input.txt').readlines()

data = [x.strip().split(": ") for x in file]

print(f'The answer:  {solve1(data)}\nOr Possibly: {solve2(data)}')
