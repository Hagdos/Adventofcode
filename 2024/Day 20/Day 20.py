import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

class Tiles(Tiles.Tiles):

    def within_range(self, pos, distance=20):
        r, c = pos
        for dr in range(-distance, distance+1):
            for dc in range(-distance+abs(dr), distance+1-abs(dr)):
                yield (r+dr, c+dc), abs(dr)+abs(dc)


def solve(length, path, scores):

    ans1 = ans2 = 0
    for t1 in path:
        for t2, distance in tiles.within_range(t1):
            if t2 in path:
                if scores[t2] - scores[t1] - distance >= 30:
                    if distance == 2:
                        ans1 += 1
                    ans2 += 1
    return ans1, ans2


file = open('input.txt').read()

tiles = Tiles(file)

start, end = tiles.find_start_end('S', 'E')

length, path, scores = tiles.Dijkstra_path(start, end)

tiles.print_Tiles(path)

ans1, ans2 = solve(length, path, scores)
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
