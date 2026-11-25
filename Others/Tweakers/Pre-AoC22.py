# Challenge: https://gathering.tweakers.net/forum/view_message/86647696

import hashlib

class BinaryTreeNode:
    def __init__(self):
        self.value = None
        self.size = 0

    def add(self, value):
        self.size += 1
        if self.value:
            if value > self.value:
                self.right.add(value)
            elif value < self.value:
                self.left.add(value)
            else:
                raise ValueError(f'Value already in Tree: {value}')
        else:
            self.value = value
            self.left = BinaryTreeNode()
            self.right = BinaryTreeNode()

    def position(self, value):
        if self.value:
            if value < self.value - self.left.size:
                return self.left.position(value) 
            else:
                value += self.left.size + 1
                return self.left.size + 1 + self.right.position(value)
        else:
            return 0

    def returnsorted(self):
        if self.value:
            l = self.left.returnsorted() if self.left.value else []
            r = self.right.returnsorted() if self.right.value else []
            return l + [self.value] + r

      
file = open('Others/Tweakers/aoc-2026-pre-1-challenge-2.txt').read()
steps = [int(x) for x in file.strip().split()]

pos = 0
taken = BinaryTreeNode()

ans1 = ''

for step in steps[:]:
    pos += step
    letter = pos + taken.position(pos)
    ans1 += chr(letter%26+ord('A'))

    taken.add(letter)


print('The answer to part x: ', hashlib.sha256(ans1.encode("utf-8")).hexdigest())
print('The answer to part 1: ', 'd93801e79cfa9bd23f0402a6cb475cecc7a5a2c3d8b256daf8227bff465fae26')
print('The answer to part 2: ', '78dd4357d2a9bf009290c5c318ce51217b25220cc50f2922ce6357358c1e727d')

# This works on part 1; but not on part 2...