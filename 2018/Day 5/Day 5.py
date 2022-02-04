def shortenPolymer(M):
    i = 0
    newM = ''
    while i < len(M):
        if i == len(M)-1:
            newM += M[i]
            i += 1
        elif (M[i].upper() == M[i+1].upper() and
              M[i].isupper() ^ M[i+1].isupper()
              ):
            i += 2
        elif (newM and M[i].upper() == newM[-1].upper() and
              M[i].isupper() ^ newM[-1].isupper()
              ):
            newM = newM[:-1]
            i += 1
        else:
            newM += M[i]
            i += 1
    return len(newM), newM


def removeChar(M, c):
    newM = ''
    for char in M:
        if not char.upper() == c:
            newM += char
    return newM


M = open('2018/Day 5/input.txt').read().strip()

char = set()
for c in M:
    char.add(c.upper())

length, _ = shortenPolymer(M)
print(f'The answer to part 1: {length}')

shortestlength = length

for c in char:
    Ms = removeChar(M, c)
    length = shortenPolymer(Ms)[0]
    if length < shortestlength:
        shortestlength = length


print(f'The answer to part 2: {shortestlength}')
