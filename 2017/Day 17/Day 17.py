import time

nsteps = int(open('input.txt').read().strip())
insertions = 2017

buffer = [0]
pointer = 0

for i in range(1, insertions+1):
    # Add the steps:
    pointer += nsteps
    pointer %= i    # The size of the buffer is equal to i.
    
    # Insert the next value
    buffer = buffer[:pointer+1] + [i] + buffer[pointer+1:]

    # Increase the pointer by one, pointing to the new value
    pointer += 1
    
# Find the value after 2017 in the buffer
ans1 = buffer[buffer.index(2017)+1]
print('The answer to part 1: ', ans1)

# Part 2
insertions = 50_000_000
pointer = 0
i = 0

while i < insertions+1:
    # Check how many jumps we can make before hitting the end of the stack (size is i)
    # Add one; so we will go beyond the stack; looping back to the start
    space = (i - pointer)//nsteps + 1
    # Increase the step counter by that many steps.
    i += space
    # Increase the pointer that many times with the stepsize + 1.
    # The plus one is because inserting a value in the stack increments the 
    # stepsize with one as well.
    pointer += (space * (nsteps+1)) - 1
    pointer %= i
    pointer += 1
    
    if pointer == 1:
        ans2 = i

    

print('The answer to part 2: ', ans2)
print('The correct answer  : ', 39289581)

