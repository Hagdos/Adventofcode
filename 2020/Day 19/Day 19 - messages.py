f = open('Rulesreddit.txt')
import re

rules = {}
messages = []

for x in f:
    if ':' in x:
        r = x.strip().split(':')
        rules[int(r[0])] = r[1].strip().split(' ')
    else:
        messages.append(x.strip())
messages.pop(0)    

def createreg(rule):
    if rules[rule][0].islower():
        r = rules[rule][0][1]
    elif '|' in rules[rule]:
        r = ['(?:']
        for i in rules[rule]:
            if i == '|':
                r.append('|')
            else:
                r.append(createreg(int(i)))
        r.append(')')
        r = ''.join(r)
    else:
        r = []
        for i in rules[rule]:
            r.append(createreg(int(i)))
            # print(r)
            # print(''.join(r))
        r = ''.join(r)
    return r
 

# ## Solution is 42+, 31+; with 42+ longer than 31+

regex0 = createreg(0)
regex42 = '\A(?:' + createreg(42) + ')+'
regex31 = '(?:' + createreg(31) + ')+$'
# regex31 = createreg(31,p2)

ans1 = 0
ans2 = 0
for i, m in enumerate(messages[:]):
    # print('Message     = ', m)
    begin = ''
    end = ''
    if re.search(regex42, m):
        begin = re.findall(regex42, m)[0]
    if re.search(regex31, m):
        end =  re.findall(regex31, m)[0]
    if re.search(regex0, m):
        if re.findall(regex0, m)[0] == m:
            print(m)
            ans1+=1
    a = False
    if len(begin)+len(end) >= len(m):
        if len(begin) > 1 and len(end)>1:
            if len(begin) > len(end):
                ans2+=1
                # print(m)
                a = True
                # print('Message     = ', m)
    # if a == True:
    #        print('Message  = ', m)
    #        print('Solution = ', begin, end)
    #        print(i)
                
print('Answer Part 1 = ', ans1)
print('Answer Part 2 = ', ans2)
    
















    # if re.match(regex8, m):
    #     first = re.match(regex8, m)
    #     m = m.replace(first[0], '', 1)
    #     print('First part  = ', first[0])
    #     print('Second part = ', m)
        
    #     if re.search(regex11, m):
    #         second = re.search(regex11, m)
    #         print(second[0])
    #     # print(m)
            # ans += 1
        
        
        

