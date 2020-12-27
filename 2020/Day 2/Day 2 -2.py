import re

f = open('Passwords.txt')

valid = 0

for x in f:
    a = 0
    limit = re.findall('\d+' ,x)
    letterloc = re.search(':' ,x)
    letter = x[letterloc.start()-1]
    pos1 = letterloc.start()+1

    if (x[pos1+int(limit[0])] == letter) ^ (x[pos1+int(limit[1])] == letter):
        valid += 1
    

print valid
