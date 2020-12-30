import intcode as ic

f = open('code.txt')
code = f.readline().strip().split(',')

mem = ic.codetomem(code)
ic.runintcode(mem)

