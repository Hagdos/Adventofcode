import hashlib
import re

Pt2 = True

salt = 'yjdafjpo'

reThree = r'(.)\1\1'
reFive = r'(.)\1\1\1\1'

keys = []
Threes = {}

solutionFound = False

for char in range(16):
    Threes[hex(char)[2:]] = []

for index in range(25000):

    value = ''.join([salt, str(index)])
    hash = hashlib.md5(value.encode()).hexdigest()

    if Pt2 is True:
        for _ in range(2016):
            value = hash
            hash = hashlib.md5(value.encode()).hexdigest()

    matchThree = re.search(reThree, hash)
    matchFive = re.findall(reFive, hash)

    if matchThree:
        Threes[matchThree.group(1)].append(index)

    if matchFive:
        print(matchFive)
        for match in matchFive:
            for indexThree in Threes[match]:
                if 0 < index - indexThree <= 1000:
                    keys.append(indexThree)


print('The answer is:', sorted(keys)[63])
