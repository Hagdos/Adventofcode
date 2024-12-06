file = open('input.txt').readlines()

lists = [[], []]

for line in file:
    l = line.strip().split()
    for n, x in enumerate(l):
        lists[n].append(int(x))

lists[0].sort()
lists[1].sort()


ans1 = ans2 = 0

for n in range(len(lists[0])):
    ans1 += abs(lists[0][n] - lists[1][n])

for n in lists[0]:
    ans2 += n*lists[1].count(n)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
