from sys import path
if "D:\Mijn Documenten\AdventofCode\y2019" not in path:
    path.append("D:\Mijn Documenten\AdventofCode\y2019")
import intcode as ic

f = open('code.txt')
code = f.readline().strip().split(',')

size = 50
chart = []
ans1 = 0
outfile = open("chart.txt","w") 
for y in range(size):
    line = []
    for x in range(size):
        inputs = [x,y]
        mem = ic.codetomem(code)
        _, outputs, counters, finished = ic.runintcode(mem, inputs)
        line.append(outputs[0])
        ans1 += outputs[0]
        # print(outputs[0])
    # print(line)
    outfile.write(''.join([str(int) for int in line]))
    outfile.write('\n')
    # chart.append(line)
    
print("Answer part 1: ", ans1)
outfile.close()

# =============================================================================
# Part 2
# =============================================================================

def checkloc(loc):
    mem = ic.codetomem(code)
    _, outputs, _, _= ic.runintcode(mem, loc)
    return outputs[0]

x = 0
y = 10

while(True):
    if not checkloc([x, y]):
        x += 1
    else:
        if not checkloc([x+99,y]):
            y += 1
        else:
            if not checkloc([x,y+99]):
                x += 1
            else:
                print("Answer part 2:", x*10000+y)
                break
            