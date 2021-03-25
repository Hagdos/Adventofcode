f = open("Codes.txt", "r")

Codes = []
i = 0
for x in f:
    Codes.append(int(x))
    i+=1;

i = 0
for x in Codes:
    i+=1
    for y in Codes[i:]:
        if x+y == 2020:
            result = x*y



print(result)
