def divisors(value):
    divisors = set()
    sqrt = round(value**(1/2) + 0.5)
    for i in range(1, sqrt):
        if value%i == 0:
            divisors.add(i)
            divisors.add(value//i)
            
    divisors.add(value)
            
    return divisors

def countPresents(house):
    return sum(divisors(house))*10
    
import time

start = time.time()

threshold = 33100000
house = 0
presents = 0

while presents < threshold:
    house += 2      #Can add up with 2; unlikely that the first house w a lot of presents is an odd number
    presents = countPresents(house)

        
print('Time: ', time.time()-start)
print('House', house, 'has', presents, 'presents')

776160



