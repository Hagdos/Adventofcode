f = open('Code.txt')
import matplotlib.pyplot as plt

def maskval(val, mask):
    b = list(format(val, '#038b'))
    # print(''.join(b))
    # print(' ', mask)
    for i,m in enumerate(mask):
        if m == '1':
            b[i+2] = '1'
        elif m == '0':
            b[i+2] = '0'
    

    # print(''.join(b))
    return ''.join(b)    


code = []

for x in f:
    code.append(x.strip().split(' = '))
    
mem = {}

for x in code:
    # print(x)
    if x[0] == 'mask':
        mask = x[1]
    else:
        loc = x[0].split('[')[1][:-1]
        mem[loc] = maskval(int(x[1]), mask)
        # print(int(mem[loc],2))
    
    # print()
        

ans = 0
for i in mem:
    ans += int(mem[i],2)
    # print(int(mem[i], 2))

# ------ Part 2 -----------

def maskval2(addr, mask):
    b = list(format(addr, '#038b'))
    # print(''.join(b))
    # print(' ', mask)
    for i,m in enumerate(mask):
        if m == '1':
            b[i+2] = '1'
        elif m == 'X':
            b[i+2] = 'X'

    return ''.join(b)  

def floatoptions(addr):
    optionsf = []
    addr = list(addr)
    
    for i,a in enumerate(addr):
        if a == 'X':
            addr[i] = '1'
            # print(''.join(addr))
            optionsf.append(''.join(addr))
            addr[i] = '0'
            optionsf.append(''.join(addr))
            break
        if i == len(addr):
            return optionsf
    return optionsf

def checkoptions(addr):
    options = floatoptions(addr)
    loop = True
    while loop:
        optionsnew = []
        for o in options:
            for i in floatoptions(o):
                optionsnew.append(i)
                options = optionsnew
                
        if 'X' not in options[0]:
            loop = False
    
    return options

mem = {}
mask = 0
memsize = []

for x in code:
    # print(x)
    if x[0] == 'mask':
        mask = x[1]
    else:
        addr = x[0].split('[')[1][:-1]
        addr = maskval2(int(addr), mask)
        # print(addr)
        for a in checkoptions(addr):
            mem[a] = x[1]
    memsize.append(len(mem))

ans = 0
for i in mem:
    ans += int(mem[i])

print(ans)
plt.plot(memsize)



