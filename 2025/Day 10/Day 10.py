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
    # print("Matrix:")
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

            # print(f"Row: {pivotrow}, Column: {pivotcolumn}")
            # print_matrix(M)

            pivotcolumn += 1
            pivotrow += 1

    return M
            

def back_substitute_row(M, button_presses):
    large_value = 1000000
    if not M:
        # print(button_presses)
        return sum(button_presses) 
    
    # M = [r.copy() for r in M]
    
    row = M[-1]
    # row_copy = row.copy()

    if not any(row[:-1]):
        if row[-1] != 0: # Unsolvable equation
            return large_value
        return back_substitute_row(M[:-1], button_presses) # Take out empty rows.

    B = row[-1]
    end = 2
    for b in button_presses: #Calculate the button-presses that are already known
        B -= b * row[-end]
        end += 1

    if row[-end] == 0:    # If the last index is 0; swap the last two columns:
        # Find the first non-empty column:
        i = next(i for i, r in enumerate(row) if r)
        # assert row[-end-1] != 0, (row, i)
        for r in M:
            r[-end], r[i] = r[i],r[-end]

    if not any(row[:-end]): #If it's a row with a single number on the right side; solve that equation
        if B%row[-end] != 0 or B//row[-end] < 0: # We shouldn't be pressing a button a negative number of times or a fractional number of times
            return large_value
        # button_presses.append(B//row[-end])
        return back_substitute_row(M[:-1], button_presses+[B//row[-end]])

    else:
        # Put the row back. Append any feasible number to button_presses; and find the lowest solution]
        # M.append(row_copy)
        max_button_presses = abs(B//row[-end]) # This is not the theoretical maximum; as other values could be negative.
        best = large_value
        for n in range(max_button_presses+random_additor): #TODO +30 is random here. Could theoretically be very large
            a = back_substitute_row(M, button_presses+[n]) #I need a better solution for this than hard-coding. Maybe binary search or something. Almost all solutions aren't actually valid solutions.
            # print(n, a)
            if a < best:
                best = a
                
        return best

start = time.time()
file = open('2025/Day 10/input.txt').readlines()
ans1 = ans2 = 0


random_additor = 5 # 21494
random_additor = 30 # 21469
random_additor = 100 # 21469
random_additor = 500 # 21469


for line in file[:]: 
    # Line 10 is finding an answer now in ~ 2 seconds. 
    # Line 90 is broken; 
    print(line)
    line = line.split()
    lights = [c == '#' for c in line[0][1:-1]]
    buttons = list(set(int(i) for i in b[1:-1].split(',') )for b in line[1:-1])
    joltage = [int(i) for i in line[-1][1:-1].split(',')]

    # ans1 += switch_indicators(lights, buttons)
    
    M=create_matrix(buttons, joltage)

    N = [r.copy() for r in M]
    triangleM=gaussian_elimination(N)
    print_matrix(triangleM)

    # Add another equation: The sum of all button presses should be answer (as low as possible)
    s = max(joltage)-1 # The amount of presses needed will never be less than the lowest joltage
    M.append([1]*(len(M[0])-1)+[s])
    r = 1000000
    while r == 1000000:
        s += 1
        M[-1][-1] = s
        N = [r.copy() for r in M]
        triangleM=gaussian_elimination(N)
        print(s)
        # print_matrix(triangleM)
        r=back_substitute_row(triangleM, [])

    ans2 += r
    print(r)
    # print("Newline")
    # print_matrix(M)


# print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
print(f'{time.time()-start} seconds to run')
pyperclip.copy(ans2)


# It's fixable by math, though the number of buttons and number of indicators are not always the same (sometimes more, sometimes less).
# If there are equal or less buttons than indicators; there's only one way to solve; which can be mathed.
# If there are more buttons than indicators, there are more ways to solve it by definition. Then you'd want to start with the buttons with most indicators first.

# 21494 is too high...
# 