file = open('input.txt').readlines()
data = [x.strip() for x in file]
ans1 = ans2 = 0

opener = '<[({'
closer = '>])}'

goodlines = []

for line in data:
    corrupt = False
    # Stack of all openers
    stack = []
    for char in line:
        # If the next character is an opening brace; add to the stack
        if char in opener:
            stack.append(char)
        
        # If the next character is a closing brace; compare to the top
        # of the stack.       
        if char in closer:
            o = stack.pop()
            # If the ascii-value is within range 3; it's the correct closer.    
            if ord(char) - ord(o) in range(3):
                continue
            
            # if it's not the correct closer; tag this line corrupt, 
            # and add points to the pt1 answer
            corrupt = True
            if char == ')':
                ans1 += 3
            elif char == ']':
                ans1 += 57
            elif char == '}':
                ans1 += 1197
            elif char == '>':
                ans1 += 25137
            
            
    # If it's not corrupt; it's missing closing symbols. Add the stack to 
    # the list of non-corrupt lines
    if not corrupt:
        goodlines.append(stack)

scores = []

# Check each stack for lone opening symbols
for stack in goodlines:
    score = 0
    # In reverse order; close the latest opener first
    for char in stack[::-1]:
        #Multiply score by 5; and add the corresponding symbol scores
        score *= 5
        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4
    scores.append(score)
    
# Find the median of all scores
scores.sort()
ans2 = scores[len(scores)//2]

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)