#Function for printing of the stack (debug function)
def stack(startpointer, stepsize, n = -1):
    pointer = startpointer
    printstack = []
    if n == -1:                                     #If no n is given; print the entire stack
        for _ in range(min(stacksize, 10)):
            printstack.append(pointer)              #Pointer is equal to the card number, because the deck starts in order and I don't actually shuffle a list
            pointer = step(pointer, stepsize)       #Find next card/pointer
        return printstack[:9]                       #Only the first 10 cards; to prevent console overflow when I forget to uncomment print(stack())
    else:                                           
        pointer = step(pointer, stepsize, n)        #If an n is given; print that card/pointer
        return pointer
        
#Function to find one card in the stack; necessary for Part 1
def findcard(startpointer, stepsize, n):
    pointer = startpointer
    for i in range(stacksize):
        if pointer == n:
            return i
        pointer = step(pointer, stepsize)
    
#Move a pointer one or multiple steps forward; basically finding the next card in the deck
def step(pointer, stepsize, times = 1):
    pointer += stepsize*times
    pointer %= stacksize
    return pointer
    
#Shuffle a new deck (reverse order of the deck)
def new(startpointer, stepsize):
    stepsize *= -1                                 #Reverse the direction
    startpointer = step(startpointer, stepsize)    #Move in step in the new direction; so what was first position is now the last position
    return startpointer, stepsize

#Cut the deck
def cut(startpointer, stepsize, N):
    return step(startpointer, stepsize, N)          #Move the starting pointer N cards forward
    
#Incremental deal. The stepsize needs to increase by 1/N + a*size/N; with a such that this is an integer number
def incr(stepsize, N):
    for m in range(N):
        if (1+m*stacksize)%N==0:
            a = m
            break
    stepsize *= ((1+stacksize*a)//N)
    stepsize %= stacksize
    return stepsize

#Exponential function; but much faster. Making use of the fact that a^(2b) = (a^b)^2
def powerof(a, b, m):
    if b <= 2:
        return (a**b)%m
    elif not b%2:
        return (powerof(a, b//2, m)**2)%m
    else:
        return (powerof(a, (b-1)//2, m)**2*a)%m

def inv(n):
    return pow(n, stacksize-2, stacksize)

p1 = False
    
startpointer = 0
stepsize = 1
filename = 'Dealings.txt'
stacksize = 119315717514047
times = 101741582076661

if p1:
    stacksize = 10007
    times = 1

f = open(filename)
for command in f:
    cmd = command.strip().split(' ')
    if cmd[0] == 'deal':
        if cmd[2] == 'new':
            startpointer, stepsize = new(startpointer, stepsize)
        elif cmd[2] == 'increment':
            stepsize = incr(stepsize, int(cmd[-1]))
    elif cmd[0] == 'cut':
        startpointer = cut(startpointer, stepsize, int(cmd[-1]))

if p1:
    print("Answer to Part 1:", findcard(startpointer, stepsize, 2019))
else:
    stepsize_n = powerof(stepsize,times,stacksize)%stacksize
    startpointer_n = (startpointer * ((1-stepsize_n)%stacksize) * inv(1-stepsize))%stacksize
    print("Answer to Part 2:", stack(startpointer_n, stepsize_n, 2020))