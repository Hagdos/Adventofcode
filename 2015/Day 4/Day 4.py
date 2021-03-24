import hashlib

key = b'ckczppom'

P1_found = False

for number in range(10000000):
    data = key + str(number).encode()
    result = hashlib.md5(data).digest().hex()[0:6]
    if result[0:5] == '00000' and not P1_found:
        print("Answer to part 1:", number)
        P1_found = True
    if result == '000000':
        print("Answer to part 2:", number)
        break
        