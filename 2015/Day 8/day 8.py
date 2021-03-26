import re

file = open('input.txt')

codeCharacters = 0
strCharacters = 0

for wish in file:
    code = wish.strip()
    codeCharacters += len(code)
    string = code.strip('"')
    string = string.replace(r'\"', '"')                     #Replace \" with "
    string = string.replace(r'\\', '\\')                    #Replace \\ with \
    string = re.sub(r'\\x[0-9a-f]{2}', 'a', string)         #Replace hexadecimals (\x..) with a
    strCharacters += len(string)
    
print("Answer for part 1:", codeCharacters - strCharacters)

# =============================================================================
# Part 2
# =============================================================================
file = open('input.txt')

codeCharacters = 0
strCharacters = 0

for wish in file:
    string = wish.strip()
    strCharacters += len(string)
    code = string.replace('\\', '\\\\')
    code = code.replace('"', '\\\"')
    codeCharacters += len(code) + 2
    
print("Answer for part 2:", codeCharacters - strCharacters)