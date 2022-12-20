class LL:
    def __init__(self, number):
        self.n = number
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.n)

    def printlist(self, start, l):
        l.append(self.n)
        if start != self.right.n:
            self.right.printlist(start, l)
        else:
            print(l)

file = open('input.txt').readlines()

l = [LL(int(x)) for x in file]
length = len(l)-1

for i in range(len(l)):
    l[i-1].right = l[i]
    l[i].left = l[i-1]

for i in l:
    # l[0].printlist(l[0].n, [])
    if i.n == 0:
        start = i
    # Take i out of the list (link their neighbours)
    i.left.right = i.right
    i.right.left = i.left

    # move it i spaces to the right
    right = i.right
    for _ in range(i.n%length):
        right = right.right

    i.right = right
    i.left = right.left
    i.right.left = i
    i.left.right = i



ans1 = ans2 = 0
# Find answer 1:
for _ in range(3):
    for _ in range(1000):
        start = start.right
    ans1 += start.n

print('The answer to part 1: ', ans1)

key = 811589153
l = [LL(int(x)*key) for x in file]
length = len(l)-1

for i in range(len(l)):
    l[i-1].right = l[i]
    l[i].left = l[i-1]

for _ in range(10):
    for i in l:
        # l[0].printlist(l[0].n, [])
        if i.n == 0:
            start = i
        # Take i out of the list (link their neighbours)
        i.left.right = i.right
        i.right.left = i.left

        # move it i spaces to the right
        right = i.right
        for _ in range(i.n%length):
            right = right.right

        i.right = right
        i.left = right.left
        i.right.left = i
        i.left.right = i


# Find answer 1:
for _ in range(3):
    for _ in range(1000):
        start = start.right
    ans2 += start.n

print('The answer to part 2: ', ans2)

#3577 is too low