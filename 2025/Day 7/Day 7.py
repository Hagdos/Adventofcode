import pyperclip
import sys
import os
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

start_time = time.time()

file = open('2025/Day 7/input.txt').read()
grid = Tiles.Tiles(file)
ans1 = ans2 = 0

start = grid.find_start_end(startsymbol='S')
todo = [start]

counter = {start: 1}
seen = set()

while todo:
    position = todo.pop()

    if position in seen:
        continue

    count = counter[position]
    seen.add(position)
    position = grid.step(position, (1, 0))

    if not grid.in_range(position):
        ans2 += count
        continue

    if grid.get_tile(position) == '.':
        todo.append(position)
        counter[position] = counter.get(position, 0) + count

    elif grid.get_tile(position) == '^':
        ans1 += 1
        for d in [-1, 1]:
            side = grid.step(position, (0, d))
            todo.append(side)
            counter[side] = counter.get(side, 0) + count


# print(grid)


print(f"Solved in {(time.time()-start_time)*1000} milliseconds")
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
pyperclip.copy(ans2)
