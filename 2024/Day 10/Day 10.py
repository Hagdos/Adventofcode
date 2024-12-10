def findTrails2(r, c):
    if tmap[r][c] == 9:
        return 1

    total = 0

    for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if 0 <= r+dr < len(tmap) and 0 <= c+dc < len(tmap[0]):
            if tmap[r+dr][c+dc] == tmap[r][c]+1:
                total += findTrails2(r+dr, c+dc)

    return total

def findTrails(r, c):
    if tmap[r][c] == 9:
        return {(r,c)}

    peaks = set()

    for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if 0 <= r+dr < len(tmap) and 0 <= c+dc < len(tmap[0]):
            if tmap[r+dr][c+dc] == tmap[r][c]+1:
                peaks.update(findTrails(r+dr, c+dc))

    return peaks


file = open('input.txt').readlines()

tmap = [[int(i) for i in x.strip()] for x in file]

ans1 = ans2 = 0

for r in range(len(tmap)):
    for c in range(len(tmap[0])):
        if tmap[r][c] == 0:
            ans1 += len(findTrails(r, c))
            ans2 += findTrails2(r, c)


print(findTrails(10, 1))



print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
