import re
import json

database = open('input.txt').read()
# database = '[1,{"c":"red","b":2},3]'

numbers = re.findall(r'-*[0-9]+', database)

total = 0
for n in numbers:
    total += int(n)
    
print('Answer to part 1:', total)

# =============================================================================
# Part 2
# =============================================================================

database = json.loads(database)

# Iterating function; adding all values that are not in a dictionary that contains a "red"
def readdatabase(data, value):
    if type(data) == list:
        for d in data:
            value += readdatabase(d, 0)
    elif type(data) == dict:
        if 'red' not in data.values():
            for v in data.values():
                value += readdatabase(v, 0)
    elif type(data) == int:
        return data
    elif type(data) == str:
        return 0
    else:
        print(data,type(data))
        return 0
    return value

total2 = readdatabase(database, 0)

print('Answer to part 2:', total2)

