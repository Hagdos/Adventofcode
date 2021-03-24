import re

strings = open('input.txt')

niceStrings = 0    #Counter for number of nice strings

for string in strings:
    vowels = 0
    double = False
    forbiddenString = False
    prevChar = 0
    
    for char in string:
        if char in 'aeiou':
            vowels += 1
        if char == prevChar:
            double = True
        if prevChar == 'a' and char == 'b':
            forbiddenString = True
        elif prevChar == 'c' and char == 'd':
            forbiddenString = True
        elif prevChar == 'p' and char == 'q':
            forbiddenString = True
        elif prevChar == 'x' and char == 'y':
            forbiddenString = True    
    
        prevChar = char
    if vowels >= 3 and double == True and forbiddenString == False:
        niceStrings += 1
    
print('Answer to part 1:', niceStrings)

# =============================================================================
# Part 2
# =============================================================================

strings = open('input.txt')

niceStrings2 = 0

for string in strings:
    string = string.strip()
    if re.search(r'([a-z]{2}).*\1', string):
        if re.search(r'([a-z]).\1', string):

            niceStrings2 += 1
            
            
        # print(string)
    #     print(re.findall('[a-z]{2}', string))
    

print('Answer to part 2:', niceStrings2)
    