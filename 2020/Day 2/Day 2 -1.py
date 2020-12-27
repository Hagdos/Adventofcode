import re

f = open('Passwords.txt')

errors = 0

for x in f:
    a = 0
    limit = re.findall('\d+' ,x)
    letterloc = re.search(':' ,x)
    letter = x[letterloc.start()-1]
    count = len(re.findall(letter, x))-1
    if count >= int(limit[0]) and count <= int(limit[1]):
        errors += 1
        a = 1
    

print errors
