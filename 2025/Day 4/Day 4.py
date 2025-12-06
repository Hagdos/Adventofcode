import time
import pyperclip
import sys
import os
import heapq as hq
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

start = time.time()

file = open('2025/Day 4/input.txt').read() #0.71 seconds; 9784
file = open('2025/Day 4/aoc-2025-day-4-challenge-1.txt').read() # 6.71 seconds
file = open('2025/Day 4/aoc-2025-day-4-challenge-2.txt').read() # 121.27 seconds -> Down to 11
# file = open('2025/Day 4/aoc-2025-day-4-challenge-3.txt').read() # 1985 seconds -> Down to 1.16

grid = Tiles.Tiles(file)
# print(grid)
ans1 = ans2 = 0

heigth, width = grid.get_size()

def remove_rolls(grid):
    removed_rolls = set()
    ans1 = 0

    for x in range(heigth):
        for y in range(width):
            if grid.get_tile((x,y)) == '@' and (x,y):
                if sum(grid.get_tile(n) == '@' for n in grid.get_eight_neighbours((x,y))) < 4:
                    ans1 += 1
                if (x,y) not in removed_rolls:
                    removed_rolls.update(remove_rolls_BFS(grid, removed_rolls, (x, y)))


    
    return len(removed_rolls), ans1

def remove_rolls_BFS(grid, removed, start):
    Queue = []
    hq.heappush(Queue, start)  # Score, position

    while Queue:
        position = hq.heappop(Queue)

        if position in removed:
            continue

        if grid.get_tile(position) == '@':
            if sum((grid.get_tile(n) == '@' and n not in removed) for n in grid.get_eight_neighbours(position)) < 4:
                removed.add(position)
                for n in grid.get_eight_neighbours(position):
                    if grid.get_tile(n) == '@':
                        hq.heappush(Queue, (n))

    return removed

removed_rolls, ans1 = remove_rolls(grid)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', removed_rolls)

print(f'This took {time.time()-start:.2f} seconds')