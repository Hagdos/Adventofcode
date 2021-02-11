import intcode as ic

#Print display:
def printdisplay(outputs):    
    disp = [[[]]]
    n = 0
    line = 0
    for i, o in enumerate(outputs):
        if o == 10:
            print(''.join(disp[n][line]))
            disp[n].append([])
            line+=1
            if outputs[i-1] == 10:
                disp.append([[]])
                n+=1
                line = 0
        else:
            disp[n][line].append(chr(o))
    print(''.join(disp[n][line]))
    return disp

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)
inputs = []
counters = [0,0,0,0]

directions = ['north', 'south', 'east', 'west']
route = []

while(True):
    #Run intcode
    mem, outputs, counters, finished = ic.runintcode(mem, inputs, counters)
    
    #Display computer output
    printdisplay(outputs)
    
    # print("Current route:", route)
    
    #Request new command; set it to input
    command = input()
    if command == 'quit':
        break
    
    # if command in directions:
    route.append(command)
        
    
    if finished:
        print("Program quit")
        break
    
    for c in command:
        inputs.append(ord(c))
    inputs.append(ord('\n'))
    
    
 # Full route: 
 # ['west',
 # 'take cake',
 # 'west',
 # 'south',
 # 'take monolith',
 # 'north',
 # 'west',
 # 'south',
 # 'east',
 # 'east',
 # 'east',
 # 'take mug',
 # 'west',
 # 'west',
 # 'west',
 # 'north',
 # 'east',
 # 'east',
 # 'east',
 # 'south',
 # 'take coin',
 # 'south',
 # 'west',
 # 'north',
 # 'north',
 # 'north',
 # '']
    
# Do not take :
# do_not_take = ['photons', 'escape pod', 'molten lava', 'infinite loop', 'giant electromagnet']

# Route to weight plate: [south, south, west, north, north, north]
# Other routes:
    # [south, east, south, south]
    # [west, west, west, south, east, south]
    # [west, west, west, south, east, east]
    # [west, west, south]
    # [north]

#Items in your inventory:
# - pointer
# - cake
# - tambourine
# - monolith
# - mouse
# - coin
# - mug

#Correct:
    # [cake, monolith, coin, mug]
     
# Movement via north, south, east, or west.

# To take an item the droid sees in the environment, use the command take <name of item>. 
# For example, if the droid reports seeing a red ball, you can pick it up with take red ball.

# To drop an item the droid is carrying, use the command drop <name of item>. 
# For example, if the droid is carrying a green ball, you can drop it with drop green ball.

# To get a list of all of the items the droid is currently carrying, use the command inv (for "inventory").
