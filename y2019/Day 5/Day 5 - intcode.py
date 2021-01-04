import sys
if "D:\Mijn Documenten\AdventofCode\y2019" not in sys.path:
    sys.path.append("D:\Mijn Documenten\AdventofCode\y2019")

import intcode as ic

f = open('code.txt')
code = f.readline().strip().split(',')

mem = ic.codetomem(code)
mem, ans, counters, finished = ic.runintcode(mem, [1])

print("Answer Part 1:", ans[-1])

mem = ic.codetomem(code)
mem, ans, counters, finished = ic.runintcode(mem, [5])

print("Answer Part 2:", ans)