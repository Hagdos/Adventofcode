import pyperclip
import time
import itertools

def press_button(lights, button):
    l = lights.copy()
    for b in button:
        l[b] = not l[b]
    return l

def switch_indicators(lights, buttons):
    if not any(lights):      # If all lights are off now (pressing the same buttons will get back the original configuration)  
        return 0
    if not buttons:
        return 1000
    
    # Try not pressing the next button
    a1 = switch_indicators(lights, buttons[1:])
  
    # Try pressing the next button
    lights = press_button(lights, buttons[0])
    a2 = switch_indicators(lights, buttons[1:]) + 1

    return min(a1, a2)

def switch_joltage(joltage, buttons):
    # This method works; but is insanely slow.
    if not any(joltage):
        return 0                # Check if joltage is 0 for all numbers

    if not buttons:
        return 1000000

    print(buttons)

    best = switch_joltage(joltage, buttons[1:])

    presses = 0
    while all(j>=0 for j in joltage):
        presses += 1
        # Press the button once; and try
        joltage = [j-1 if i in buttons[0] else j for i,j in enumerate(joltage)]
        best = min(best, switch_joltage(joltage, buttons[1:])+presses)

    return best


def print_matrix(M):
    for row in M:
        print(row)

def create_matrix(buttons, joltage):
    M = []
    for i, j in enumerate(joltage):
        M.append([1 if i in button else 0 for button in buttons])
        M[-1].append(j)

    return M

def gaussian_elimination(M):
    pivotrow = 0
    pivotcolumn = 0

    while pivotrow < len(M) and pivotcolumn < len(M[0]):
        # Find the first row that has True in the current column
        top_row = None

        for r in range(pivotrow, len(M)): #Todo: Not enough to find any row; numbers might be larger or smaller than 1 (I think)
            if M[r][pivotcolumn]:
                top_row = r
                break
        
        if top_row == None: #No pivots in this column, go to next column
            pivotcolumn += 1

        else:
            M[pivotrow], M[top_row] = M[top_row], M[pivotrow]
            for row in range(pivotrow+1, len(M)):
                if M[row][pivotcolumn]:
                    f = M[row][pivotcolumn]
                    for c in range(pivotcolumn, len(M[0])):
                        M[row][c] = M[row][c]*M[pivotrow][pivotcolumn] - M[pivotrow][c]*f

            pivotcolumn += 1
            pivotrow += 1

    return M
            

def back_substitute_row(M, button_presses):
    if not M: 
        return sum(button_presses) 
       
    row = M[-1]

    if not any(row[:-1]): # If all entries in the row are 0; it's either an empty row that can be skipped, or an impossible solution.
        if row[-1] != 0: # Unsolvable equation
            return large_value
        return back_substitute_row(M[:-1], button_presses) 

    B = row[-1]
    end = 2
    for b in button_presses: #Calculate out the button-presses that are already known
        B -= b * row[-end]
        end += 1

    if row[-end] == 0:    # If the last index is 0; swap the last column with the first non-empty column
        # Find the first non-empty column:
        i = next(i for i, r in enumerate(row) if r)
        for r in M:
            r[-end], r[i] = r[i],r[-end]

    if not any(row[:-end]): #If it's a row with a single number on the right side; solve that equation
        if B%row[-end] != 0 or B//row[-end] < 0: # We shouldn't be pressing a button a negative number of times or a fractional number of times
            return large_value
        return back_substitute_row(M[:-1], button_presses+[B//row[-end]])

    else:
        best = large_value
        for n in range(s): # The number of button presses should never be more than the answer s we're looking for in this iteration.
            a = back_substitute_row(M, button_presses+[n]) 
            if a < best:
                best = a
                
        return best

start = time.time()
file = open('2025/Day 10/input.txt').readlines()
ans1 = ans2 = 0

large_value = 1000000

for line in file[:]: 
    line = line.split()
    lights = [c == '#' for c in line[0][1:-1]]
    buttons = list(set(int(i) for i in b[1:-1].split(',') )for b in line[1:-1])
    joltage = [int(i) for i in line[-1][1:-1].split(',')]

    ans1 += switch_indicators(lights, buttons)
    
    M=create_matrix(buttons, joltage)

    N = [r.copy() for r in M]
    triangleM=gaussian_elimination(N)
    # print_matrix(triangleM)

    # Add another equation: The sum of all button presses should be answer (as low as possible)
    # The first sum s that returns an answer is the lowest answer
    s = max(joltage) # The amount of presses needed will never be less than the highest joltage (as the increments are never more than 1 per button)
    M.append([1]*(len(M[0])-1)+[s])
    r = large_value
    while r == large_value:
        M[-1][-1] = s
        N = [r.copy() for r in M]
        triangleM=gaussian_elimination(N)
        r=back_substitute_row(triangleM, [])
        s += 1

    ans2 += r


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
print(f'{time.time()-start} seconds to run')
pyperclip.copy(ans2)


# Todo; find a cleaner way to find a valid value for random_additor?