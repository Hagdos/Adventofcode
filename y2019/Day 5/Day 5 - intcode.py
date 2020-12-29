import sys
if "D:\Mijn Documenten\AdventofCode\y2019" not in sys.path:
    sys.path.append("D:\Mijn Documenten\AdventofCode\y2019")

import intcode as ic

f = open('code.txt')
code = f.readline().strip().split(',')

mem = ic.codetomem(code)
ic.runintcode(mem)

