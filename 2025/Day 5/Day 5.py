import time

def combine_ranges(ranges):
    # Assumes a sorted list of ranges; sorted by the starting point of each range.
    newrange = []
    r=0
    while r < len(ranges)-1:
        if ranges[r][1] < ranges[r+1][0]: #Doesn't overlap; simply keep the range and continue
            r += 1
        else:    #Ranges overlap; Combine the first starting point with the largest endpoint. Combine the two ranges; remove the next one. Try again.
            ranges[r] = (ranges[r][0], max(ranges[r][1], ranges[r+1][1]))
            ranges.pop(r+1)
            # 
    return ranges

def check_if_in_range(range, ingredient):
    return range[0] <= ingredient <= range[1]


def midpoint(start, end):
    # The module 2 is to ensure rounding up; in case of list length 2.
    # Cheaper solution is to simply add 1. The list always shortens when the endpoint isn't found
    return (end+start)//2 + 1


def binary_search_ingredient(ranges, ingredient):
    # Assumes a sorted; non-overlapping list of ranges.
    start = 0
    end = len(ranges)-1

    while start != end:
        mid = midpoint(start, end)
        if ingredient >= ranges[mid][0]:
            start = mid
        else:
            end = mid-1

    return ranges[start]

start = time.time()

file = open('2025/Day 5/aoc-2025-day-5-challenge-1.txt').read()
file = open('2025/Day 5/testinput.txt').read()
ranges, ingredients = file.split('\n\n')

ranges = [tuple(int(i) for i in x.strip().split('-')) for x in ranges.split('\n')]
ranges.sort()

ingredients = [int(i) for i in ingredients.strip().split('\n')]

ans1 = ans2 = 0

ranges = combine_ranges(ranges)

for ingredient in ingredients:
    
    r = binary_search_ingredient(ranges, ingredient)
    if check_if_in_range(r, ingredient):
        # assert fresh, f"{ingredient, r}"    
        ans1 += 1

for r in ranges:
    ans2 += r[1]-r[0]+1

print(time.time()-start)
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
