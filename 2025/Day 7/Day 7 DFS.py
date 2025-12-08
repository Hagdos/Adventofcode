import pyperclip
import sys
import os
import heapq as hq
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

def count_timelines(grid, position):
    global ans1

    if position in cache:
        return cache[position]
    
    position = grid.step(position, (1, 0))

    if not grid.in_range(position):
        return 1
    elif grid.get_tile(position) == '.':
        ans = count_timelines(grid, position)
        cache[position] = ans
        return ans
    else:
        # assert grid.get_tile(position) == '^', position
        ans1 += 1
        ans = count_timelines(grid, grid.step(position, (0,-1))) + count_timelines(grid, grid.step(position, (0,1)))
        cache[position] = ans
        return ans
    

start_time = time.time()

file = open('2025/Day 7/input.txt').read()
grid = Tiles.Tiles(file)
ans1 = ans2 = 0


cache = {}
start = grid.find_start_end(startsymbol='S')
ans2 = count_timelines(grid, start)

print(f"Solved in {(time.time()-start_time)*1000} milliseconds")
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
pyperclip.copy(ans2)
