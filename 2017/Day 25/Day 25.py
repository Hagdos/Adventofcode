ans1 = ans2 = 0

ones = set()
cursor = 0
state = 'A'

for _ in range(12629077):
    if state == 'A':
        if cursor not in ones:
            ones.add(cursor)
            cursor += 1
            state = 'B'
        else:
            ones.remove(cursor)
            cursor -= 1
            state = 'B'
    
    elif state == 'B':
        if cursor not in ones:
            cursor += 1
            state = 'C'
        else:
            cursor -= 1
            state = 'B'
    
    elif state == 'C':
        if cursor not in ones:
            ones.add(cursor)
            cursor += 1
            state = 'D'
        else:
            ones.remove(cursor)
            cursor -= 1
            state = 'A'
    
    elif state == 'D':
        if cursor not in ones:
            ones.add(cursor)
            cursor -= 1
            state = 'E'
        else:
            cursor -= 1
            state = 'F'
    
    elif state == 'E':
        if cursor not in ones:
            ones.add(cursor)
            cursor -= 1
            state = 'A'
        else:
            ones.remove(cursor)
            cursor -= 1
            state = 'D'
    
    elif state == 'F':
        if cursor not in ones:
            ones.add(cursor)
            cursor += 1
            state = 'A'
        else:
            cursor -= 1
            state = 'E'            


print('The answer to part 1: ', len(ones))
print('The answer to part 2: ', ans2)
