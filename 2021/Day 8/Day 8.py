file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

# 7-segment LCDs, with segments numbered like this:
    
#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

# Lookup table from number to segments
segments =  {0: [0, 1, 2, 4, 5, 6],
             1: [2, 5],
             2: [0, 2, 3, 4, 6],
             3: [0, 2, 3, 5, 6],
             4: [1, 2, 3, 5],
             5: [0, 1, 3, 5, 6],
             6: [0, 1, 3, 4, 5, 6],
             7: [0, 2, 5],
             8: [0, 1, 2, 3, 4, 5, 6],
             9: [0, 1, 2, 3, 5, 6],
             }

for line in data:
    # Note the possible segments a letter could be
    opt = {char: [0,1,2,3,4,5,6] for char in 'abcdefg'}
    i, o = line.split('|')
    ins = i.split()
    os = o.split()
    
    
    # Gather the three inputs that are six long, 
    # and could be part of a six, a nine or a zero
    sixninezero = []
    for t in ins:
        if len(t) == 6:
            sixninezero.append(t)
    
    # Count how often each letter appears in the three inputs.
    # Segments 2, 3 and 4 are missing from the 6, 0 and 9; so they'll only 
    # appear twice. This brings down the options for each letter
    sixninezero = ''.join(sixninezero)
    for char in 'abcdefg':
        if sixninezero.count(char) == 2:
            opt[char] = [2, 3, 4]
        elif sixninezero.count(char) == 3:
            opt[char] = [0, 1, 5, 6]
    
    # Check for length that can only be one number. Remove all options
    # that are not in that number
    for t in ins:
        # Length 2 can only be a one
        if len(t) == 2:
            for char in t:
                # This line is an and between the existing options and the 
                # options in the look-up-table
                opt[char] = [c for c in opt[char] if c in segments[1]]
        # Length 4 can only be a four
        if len(t) == 4:
            for char in t:
                opt[char] = [c for c in opt[char] if c in segments[4]]
        # Length 3 can only be a seven
        if len(t) == 3:
            for char in t:
                opt[char] = [c for c in opt[char] if c in segments[7]]
                
    
    # Loop until each character is mapped to a single segment
    while not all(len(i)==1 for i in opt.values()):
        for char in opt:
            # Single out characters that can only be one segment
            if len(opt[char]) == 1:
                # Remove that segment as an option from all other characters
                for c in opt:
                    if opt[char][0] in opt[c] and c != char:
                        opt[c].remove(opt[char][0])
    
    
    # For each output; work out the number belonging to it.
    number = ''
    for o in os:
        
        # Part 1
        if len(o) in [2, 4, 3, 7]:
            ans1 += 1
    
        # Part 2
        # Get the right segment from the character; and sort them
        os = [opt[c][0] for c in o]
        os.sort()
        
        # Check which number has the same segments; that is the number we're looking for
        for s in segments:
            if segments[s] == os:  
                number += str(s)
    
    ans2 += int(number)
    
print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
