import time


size = 1000000
# size = 20

cycles = 10000000


start = time.time()

def pop3left():
    pickup = []
    pickup.append(cups[head])
    pickup.append(cups[pickup[0]])
    pickup.append(cups[pickup[1]])
    return pickup
  
def place3(pickup):
    cups[pickup[-1]] = cups[destcup]
    cups[destcup] = pickup[0]


cupsl = [2,4,7,8,1,9,3,5,6] + list(range(10,size+1))
cups = [None]*(size+1)
head = cupsl[0]
for loc, value in enumerate(cupsl[:-1]):
    cups[value] = cupsl[loc+1]
cups[cupsl[-1]] = cupsl[0]
    
pickup = [None]*3

start = time.time()
for _ in range(cycles):
    pickup = pop3left()
print(time.time()-start)

start = time.time()
for _ in range(cycles):
    pickup = []
    pickup.append(cups[head])
    pickup.append(cups[pickup[0]])
    pickup.append(cups[pickup[1]])
print(time.time()-start)

start = time.time()
for _ in range(cycles):
    pickup[0] = cups[head]
    pickup[1] = cups[pickup[0]]
    pickup[2] = cups[pickup[1]]
print(time.time()-start)

start = time.time()
for _ in range(cycles):
    pickup = pop3left()
print(time.time()-start)
start = time.time()


start = time.time()
for _ in range(cycles):
    destcup = head - 1
    if destcup == 0:
            destcup = size
    while destcup in pickup:
        destcup -= 1
        if destcup == 0:
            destcup = size  
print(time.time()-start)

start = time.time()
for _ in range(cycles):
    place3(pickup)
print(time.time()-start)

start = time.time()
for _ in range(cycles):
    head = cups[head]
print(time.time()-start)

