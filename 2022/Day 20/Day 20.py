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

def readInput(filename, key):
    file = open(filename).readlines()

    linkedlist = [LL(int(x)*key) for x in file]
    # length = len(l)-1

    for i in range(len(linkedlist)):
        linkedlist[i-1].right = linkedlist[i]
        linkedlist[i].left = linkedlist[i-1]

        if linkedlist[i].n == 0:
            start = linkedlist[i]

    return linkedlist, start


def findCoords(start):
    ans = 0
    for _ in range(3):
        for _ in range(1000):
            start = start.right
        ans += start.n
    return ans


def mix(l, cycles):
    length = len(l)-1
    for _ in range(cycles):
        for i in l:
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
    return l


l, start = readInput('input.txt', 1)
l = mix(l, 1)
ans1 = findCoords(start)

print('The answer to part 1: ', ans1)

key = 811589153
l, start = readInput('input.txt', key)
l = mix(l, 10)
ans2 = findCoords(start)

print('The answer to part 2: ', ans2)