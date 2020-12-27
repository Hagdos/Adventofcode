import time

# def printdict():
#     nodes = []
#     inodes = []
#     a = head
#     nodes.append(str(a))
#     inodes.append(a)
#     a = cups[a][1]
#     while a is not head:
#         nodes.append(str(a))
#         inodes.append(a)
#         a = cups[a][1]
#     # print(ll)
#     # print(', '.join(nodes))
#     return inodes

def pop3left():
    pickup = []
    pickup.append(cups[head])
    pickup.append(cups[pickup[0]])
    pickup.append(cups[pickup[1]])
    return pickup
    
# def rotate(n):
#     global head
#     if n>0:
#         for _ in range(n):
#             head = cups[head]
#     elif n<0:
#          print("Kan niet")
            
def place3(pickup):
    cups[pickup[-1]] = cups[destcup]
    cups[destcup] = pickup[0]


size = 1000000
# size = 15
cycles = 10000000
    
pickup = [None]*3

cupsl = [2,4,7,8,1,9,3,5,6] + list(range(10,size+1))
# cupsl = [3,8,9,1,2,5,4,6,7] + list(range(10,size+1)) #Test input
cups = [None]*(size+1)
head = cupsl[0]
for loc, value in enumerate(cupsl[:-1]):
    cups[value] = cupsl[loc+1]
cups[cupsl[-1]] = cupsl[0]
    
# printdict()

start = time.time()
for _ in range(cycles):
    # =============================================================================
    #  pick up cups
    # =============================================================================
    pickup[0] = cups[head]
    pickup[1] = cups[pickup[0]]
    pickup[2] = cups[pickup[1]]
    # =============================================================================
    # Find destinationcup
    # =============================================================================
    destcup = head - 1
    if destcup == 0:
            destcup = size
    while destcup in pickup:
        destcup -= 1
        if destcup == 0:
            destcup = size     
    # =============================================================================
    # Place cups, Move first to end of stack,
    # =============================================================================
    cups[pickup[-1]] = cups[destcup]
    cups[destcup] = pickup[0]
    head = cups[head]
    # printdict()

print(time.time()-start)
# ans1 = printdict()

ansa = cups[1]
ansb = cups[cups[1]]

print('Improved answer after' , cycles, 'cycles:', ansa*ansb)
