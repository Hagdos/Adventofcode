import time
input = [0,8,15,2,12,1,4]
# input = [3,1,2]
end = 30000000

date = 0
numbers = dict()

for i in input[:-1]:
    numbers[i] = date
    date+=1
    
n = input[-1]

start = time.time()


while date<end-1:

    prevdate = numbers.get(n,date)  #Previous date of current number. Returns current date if not in list
    prevn = n
    n = date-prevdate #Age of current number = next number
    numbers[prevn] = date    
    date+=1
    
print(n)
print(time.time()-start)