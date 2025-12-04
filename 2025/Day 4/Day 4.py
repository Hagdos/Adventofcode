import pyperclip
import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import Tiles

file = open('2025/Day 4/input.txt').read()

grid = Tiles.Tiles(file)
# print(grid)
ans1 = ans2 = 0

heigth, width = grid.get_size()

def remove_rolls(grid):
    removed_rolls = set()

    for x in range(heigth):
        for y in range(width):
            if grid.get_tile((x,y)) == '@':
                neighbours = grid.get_eight_neighbours((x,y))
                occupied_neighbours = 0
                for n in neighbours:
                    if grid.get_tile(n) == '@':
                        occupied_neighbours += 1

                if occupied_neighbours < 4:
                    removed_rolls.add((x,y))

    for roll in removed_rolls:
        grid.set_tile(roll, 'X')
    
    return len(removed_rolls)


removed_rolls = remove_rolls(grid)
ans = removed_rolls

print('The answer to part 1: ', ans)
pyperclip.copy(ans)

while removed_rolls:
    removed_rolls = remove_rolls(grid)
    ans += removed_rolls

print('The answer to part 2: ', ans)
pyperclip.copy(ans)