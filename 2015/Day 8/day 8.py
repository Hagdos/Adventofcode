import re

file = open('input.txt')

codeCharacters = 0
strCharacters = 0


for wish in file:
    code = wish.strip()
    codeCharacters += len(code)
    string = code.replace(r'\"', '"').strip('"')
    
    # .replace(r'\\\\', "\\")