def findMiddlePage(manual):
    return manual[len(manual)//2]


def checkOrder(manual, drules):
    pages = []
    for page in manual:
        if any([r in pages for r in drules[page]]):
            return False
        pages.append(page)
    return True


def orderManual(manual, drules):
    smanual = set(manual)
    for page in smanual:
        position = len(smanual & drules[page])

        manual[-1-position] = page
    return manual


file = open('input.txt').read()
ans1 = ans2 = 0

rules, manuals = [y.strip().split() for y in file.split("\n\n")]

rules = [[int(i) for i in r.split("|")] for r in rules]
manuals = [[int(i) for i in r.split(',')] for r in manuals]

drules = {}

for rule in rules:
    if rule[0] in drules:
        drules[rule[0]].add(rule[1])
    else:
        drules[rule[0]] = set([rule[1]])

for manual in manuals:
    if checkOrder(manual, drules):
        ans1 += findMiddlePage(manual)
    else:
        manual = orderManual(manual, drules)
        ans2 += findMiddlePage(manual)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

print(f"{ans2=}")

