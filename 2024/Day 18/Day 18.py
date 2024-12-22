import Tiles

file = open('input.txt').readlines()
size = 71
fall = 1024


def checkPath(n):
    tiles = Tiles.Tiles(size=[size, size])

    for d in data[:n]:
        tiles.setTile((d[1], d[0]), '#')

    # return tiles.Astar((0,0), (size-1, size-1))
    return tiles.Dijkstra((0, 0), (size-1, size-1))


data = [[int(i) for i in x.strip().split(',')] for x in file]

print('The answer to part 1: ', checkPath(fall))

minn = 0
maxn = len(data)

while maxn-minn > 1:
    n = (maxn+minn)//2

    if checkPath(n):
        minn = n
    else:
        maxn = n

print('The answer to part 2: ', data[maxn-1])

n = 0
while checkPath(n):
    n += 1
    print(n)