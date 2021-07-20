def dragonstep(a):
    flip = {'1': '0', '0': '1'}
    b = a[::-1]
    b = ''.join([flip[s] for s in b])

    return ''.join([a, '0', b])

def checksum(a):
    check = []
    for i in range(0,len(a), 2):
        if a[i] == a[i+1]:
            check.append('1')
        else:
            check.append('0')
    
    if len(check)%2 == 0:
        return checksum(''.join(check))
    else:
        return ''.join(check)
    
    
    
data = '11101000110010100'
requiredLength = 272
requiredLength = 35651584

while len(data) < requiredLength:
    data = dragonstep(data)
    

print(checksum(data[:requiredLength]))