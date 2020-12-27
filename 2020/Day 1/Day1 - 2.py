f = open("Codes.txt", "r")

Codes = []
i = 0
for x in f:
    Codes.append(int(x))
    i+=1;

i = 0
for x in Codes:
    i+=1
    j = 0
    for y in Codes[i:]:
        j+=1
        for z in Codes[j:]:
            if x+y+z == 2020:
                result = x*y*z



print result
