import re

stream = open('input.txt').read().strip()

ans1 = ans2 = 0

# Remove all cancelled characters
stream = re.sub('!.', '', stream)

# Find all garbage, and count the length of each piece of garbage for part 2
garbage = re.findall('<(.*?)>', stream)
ans2 = sum([len(match) for match in garbage])

# Remove all garbage
stream = re.sub('<.*?>', '', stream)

# Remove all comma's, so only the {} characters remain
stream = re.sub(',', '', stream)

depth = 0
# The value of a group depends on how nested it is. Each { means one nestlevel 
# more, each } goes one level up again.
for char in stream:
    if char == '{':
        depth += 1
        ans1 += depth
    elif char == '}':
        depth -= 1
    else:
        print("Error", char)
        
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)