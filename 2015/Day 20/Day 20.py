#Function that finds all divisors of a number.
def divisors(value):
    #1 and value are always divisors.
    divisors = {1,value} 
    #We want to loop over the values up to the square root of the number
    sqrt = round(value**(1/2) + 0.5)
    for i in range(2, sqrt):
        if value%i == 0:
            divisors.add(i)
            divisors.add(value//i)
                    
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

# =============================================================================
# Part 2
# =============================================================================

def divisorsPt2(value):
    divisors = {value}
    for i in range(2, 51):
        if value%i == 0:
            divisors.add(value//i)
            
    return divisors

def countPresents2(value):
    return sum(divisorsPt2(value))*11

threshold = 33100000
house = 0
presents = 0

while presents < threshold:
    house += 2      
    presents = countPresents2(house)
    
        
print('Time: ', time.time()-start)
print('House', house, 'has', presents, 'presents')
    
