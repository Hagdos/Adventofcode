import re

string = '1113222113'
part2 = False

repetitions = 40        # For part 1
if part2 == True:
    repetitions = 50        # For part 2

for _ in range(repetitions):
    newstring = ''
    
    for i in re.findall(r'(([0-9])\2*)', string):
        newstring += str(len(i[0]))+str(i[1])
        
    string = newstring

print('Answer:', len(string))

