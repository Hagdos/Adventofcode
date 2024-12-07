def reverseconcat(n1, n2):
    e = 10
    while n2 // e != 0:
        e *= 10

    if n1 % e == n2:
        return n1//e
    return None


# Faster way to solve it, going from the result on backwards and only allowing
# moves that are possible
def checkEquation(eq, pt2):
    result = int(eq[0])
    numbers = [int(i) for i in eq[1].split()]

    results = {result}

    for n in numbers[::-1]:
        newresults = set()
        for r in results:
            if r - n >= 0:
                newresults.add(r-n)
            if n != 0 and r % n == 0:
                newresults.add(r//n)
            if pt2:
                new = reverseconcat(r, n)
                if new:
                    newresults.add(new)

        results = newresults

    if 0 in results:
        return result
    return 0


def solve(data):
    ans1 = ans2 = 0

    for eq in data:
        s = checkEquation(eq, False)
        if s:
            ans1 += s
            ans2 += s # If it's true for part 1, it's also true for part 2.
        else:
            ans2 += checkEquation(eq, True)

    return ans1, ans2


# file = open('input.txt').readlines()
file = open('aoc-2024-day-07-challenge-1.txt').readlines()

data = [x.strip().split(": ") for x in file]

ans1, ans2 = solve(data)

print(f'The answer to part 1:  {ans1}')
print(f'The answer to part 2:  {ans2}')