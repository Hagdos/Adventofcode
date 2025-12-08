import pyperclip
import heapq
from collections import defaultdict

def calculate_distance(box1, box2):
    # Returns the squared value of the 3D distance. "Real distance" is the square root of this value; but that's not necessary for comparisons
    d = 0
    for i in range(3):
        d += abs(box1[i] - box2[i])**2
    return d

file = open('2025/Day 8/input.txt').readlines()

boxes = [tuple(int(i) for i  in x.strip().split(',')) for x in file]
ans1 = ans2 = 0

shortest = []
neighbours = defaultdict(set)

for i, box1 in enumerate(boxes):
    neighbours[box1] = set([box1])

    for box2 in boxes[i+1:]:
        
        d = calculate_distance(box1, box2)
        heapq.heappush(shortest, (d, box1, box2))

for i in range(499500):
    d, box1, box2 = heapq.heappop(shortest)

    if i == 999:
        found = set()
        groupsizes = []

        for box in boxes:
            if box not in found:
                group = neighbours[box]
                found.update(group)
                groupsizes.append(len(group))
        
        groupsizes.sort()
        ans1 = groupsizes[-3]*groupsizes[-2]*groupsizes[-1]

    if box2 in neighbours[box1]:
        continue
    
    neighbours[box1].update(neighbours[box2])
    for n in neighbours[box2]:
        neighbours[n] = neighbours[box1]
        
    if len(neighbours[box1]) == 1000:
        ans2 = box1[0]*box2[0]
        break

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
pyperclip.copy(ans2)
