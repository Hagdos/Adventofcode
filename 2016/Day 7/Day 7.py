import re

file = open('input.txt').read().split()

character = r'[a-z]'
characters = r'[a-z]*'

# Searches for ABBA
ABBA = (r'([a-z])'      # A single character (group 1)
        r'(?!\1)'   # Not followed by the same character (group 1); so not AA
        r'([a-z])'      # Followed by a differenct character (group 2); AB
        r'\2\1')    # Followed by group 2 and group 1; AB BA

# ABBA2 searches for the same as above, but with [] on the outsides and no ][ in between
ABBA2 = r'\[' + characters + ABBA + characters + r'\]'

# Searches for ABA
ABA = (r'([a-z])'       # A single character (group 1)
        r'(?!\1)'       # Not followed by the same character (group 1); so not AA
        r'([a-z])'      # Followed by a different character (group 2); AB
        r'\1')          # Followed by group 2 and group 1; ABA

# Find an ABA outside of brackets, followed by an BAB inside of brackets
ABABAB = (ABA +         #There's an ABA somewhere
          r'[^\]]*'     #Followed by 0 or more characters that are not closing brackets (check if the first bracket is a [, so ABA is outside of the brackets
          r'\['         #Followed by a square bracket opening
          r'(.*'        #Followed by 0 or more characters (any type)
          r'\[)'        #Followed by a square bracket opening
          r'?'          #The second bracket opening does not have to be there; so that part has to be there 0 or 1 times.
          r'[a-z]*'     #Followed by 0 or more alphabetic characters (so that BAB is within [])
          r'\2\1\2')    #Followed by BAB (group 2, 1, 2 as defined in ABA))


# Find an BAB inside of brackets, followed by an ABA outside of brackets
BABABA = (ABA +         #There's an BAB somewhere (ABA is equal to BAB)
          r'[^\[]*'     #Followed by 0 or more characters that are not opening brackets (check if the first bracket is a ], so BAB is inside of the brackets
          r'\]'         #Followed by a square bracket closing
          r'(.*'        #Followed by 0 or more characters (any type)
          r'\])'        #Followed by a square bracket closing
          r'?'          #The second bracket closing does not have to be there if they're directly after each other; so that part has to be there 0 or 1 times.
          r'[a-z]*'     #Followed by 0 or more alphabetic characters (so that ABA is within ][)
          r'\2\1\2')    #Followed by BAB (group 2, 1, 2 as defined in ABA))


answer = 0
answer2 = 0

for line in file:
    #Search for part 1
    if re.search(ABBA, line):
        if not re.search(ABBA2, line):
            answer += 1
    #Search for part 2
    if re.search(ABABAB, line):
        answer2 += 1
    elif re.search(BABABA, line):
        answer2 += 1

print('The answer to part 1:', answer)
print('The answer to part 2:', answer2)




answer = 0
