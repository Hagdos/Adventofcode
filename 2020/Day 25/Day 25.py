#My input
cardpublickey = 8421034
doorpublickey = 15993936

# Example input
# cardpublickey = 5764801
# doorpublickey = 17807724

sn = 7
rem = 20201227
value = 1
i = 0
tries = 100000000

if False:
    while value != cardpublickey and i < tries:
        i+=1
        value *= sn
        value %= rem
        # print(value)
        
    if i>=tries:
        print('Stopped after',i, 'tries')
    else:
        cardloopsize = i
        print("Card loops =", cardloopsize)
        
    value = 1   
    i = 0
    while value != doorpublickey and i < tries:
        i+=1
        value *= sn
        value %= rem
        # print(value)
        
    if i>=tries:
        print('Stopped after',i, 'tries')
    else:
        doorloopsize = i 
        print('Door loops =', doorloopsize)
else:
    cardloopsize = 5163354
    doorloopsize = 16740460
    
value = 1
sn = doorpublickey
for _ in range(cardloopsize):
    value *= sn
    value %= rem
print(value)
    
value = 1
sn = cardpublickey
for _ in range(doorloopsize):
    value *= sn
    value %= rem
print(value)
    
    