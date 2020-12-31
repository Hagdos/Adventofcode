import intcode as ic

f = open('code.txt')
code = f.readline().strip().split(',')

mem = ic.codetomem(code)
inputs = [1]
mem, output = ic.runintcode(mem, inputs)
        
print(output)

# =============================================================================
# part 2
# =============================================================================

mem = ic.codetomem(code)
inputs = [2]
mem, output = ic.runintcode(mem, inputs)

print(output)
