minrange = 138307
maxrange = 654504

a = 0 

def checknumber(n):
    number = str(n)
    # increasing = True
    adjacent = False
    if len(number) != 6:
        return 0
    for n in range(5):
        if number[n+1] < number[n]:
            return 0
            # increasing = False
        if number[n+1] == number[n]:
            if n == 4:
                if number[n+1] != number[n-1]:
                    adjacent = True
            else:
                if number[n+1] != number[n+2] and number[n+1] != number[n-1]:
                    adjacent = True
    if adjacent:
        return 1
    else:
        return 0
    
ans = 0
for i in range(minrange, maxrange+1):
    ans += checknumber(i)
        
        
print(checknumber(333333))       
        
print(ans)