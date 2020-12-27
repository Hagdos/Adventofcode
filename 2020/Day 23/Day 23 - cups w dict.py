import time

def printdict():
    nodes = []
    inodes = []
    a = head
    nodes.append(str(a))
    inodes.append(a)
    a = cups[a][1]
    while a is not head:
        nodes.append(str(a))
        inodes.append(a)
        a = cups[a][1]
    # print(ll)
    # print(', '.join(nodes))
    return inodes

def popleft():
    global head
    cups[cups[head][0]][1] = cups[head][1]
    cups[cups[head][1]][0] = cups[head][0]
    head = cups[head][1]
    
def pop3left():
    global head
    global pickup
    pickup = []
    pickup.append(head)
    pickup.append(cups[head][1])
    pickup.append(cups[cups[head][1]][1])
    cups[cups[head][0]][1] = cups[cups[cups[head][1]][1]][1]
    cups[cups[cups[cups[head][1]][1]][1]][0] = cups[head][0]
    head = cups[cups[cups[head][1]][1]][1]
    
def rotate(n):
    global head
    if n>0:
        for _ in range(n):
            head = cups[head][1] 
    elif n<0:
        for _ in range(-n):
            head = cups[head][0] 
            
def place3():
    cups[pickup[0]][0] = destcup
    cups[pickup[-1]][1] = cups[destcup][1]
    cups[cups[destcup][1]][0] = pickup[-1]
    cups[destcup][1] = pickup[0]


size = 1000000
# size = 15
cycles = 10000000

cupsl = [2,4,7,8,1,9,3,5,6] + list(range(10,size+1))
cups = {}
head = cupsl[0]
for loc, value in enumerate(cupsl[:-1]):
    cups[value] = [cupsl[loc-1], cupsl[loc+1]]
cups[cupsl[-1]] = [cupsl[-2], cupsl[0]]
    
# printdict()

start = time.time()
for _ in range(cycles):
    currentcup = head
    # =============================================================================
    # Move first to end of stack, pick up cups
    # =============================================================================
    rotate(1)
    pop3left()
    # =============================================================================
    # Find destinationcup
    # =============================================================================
    destcup = currentcup - 1
    if destcup <= 0:
            destcup = size
    while destcup in pickup:
        destcup -= 1
        if destcup <= 0:
            destcup = size     
    # =============================================================================
    # Place cups
    # =============================================================================
    place3()
    # printdict()

print(time.time()-start)
# ans1 = printdict()

ansa = cups[1][1]
ansb = cups[cups[1][1]][1]

print('Original answer after' , cycles, 'cycles:', ansa*ansb)
