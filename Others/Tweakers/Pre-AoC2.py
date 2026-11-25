# Challenge: https://gathering.tweakers.net/forum/view_message/86647696

import hashlib
from bisect import bisect_left


file = open('Others/Tweakers/aoc-2026-pre-1-challenge-2.txt').read()
steps = [int(x) for x in file.strip().split()]

# steps = [3, -2, 0, 4] #Trial instructions

pos = 0
taken = []

ans1 = ''

for step in steps[:]:
    pos += step
    letter = pos
    for t in taken: # This only works if taken is sorted
        if t > letter:
            break
        letter += 1

    ans1 += chr(letter%26+ord('A'))

    # index = bisect_left(taken, letter)
    taken.insert(letter-pos, letter) # This can be a lot faster! Part 2 works, but takes a few minutes.


print('The answer to part 1: ', hashlib.sha256(ans1.encode("utf-8")).hexdigest())
print('The answer to part 1: ', 'd93801e79cfa9bd23f0402a6cb475cecc7a5a2c3d8b256daf8227bff465fae26')