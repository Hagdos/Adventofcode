import re

f = open('input.txt')


rulenames = []
rules = []

for x in f:
    if x == '\n':
        break
    r = x.strip().split(': ')
    rulenames.append(r[0])
    rules.append(re.split(' or |-', r[1]))
    

    
for x in f:
    if x == '\n':
        break
    myticket = x.strip().split(',')
    
tickets = []
f.readline() #Skip line with 'Nearby tickets'
for x in f:
    tickets.append(x.strip().split(','))

ans = 0
invalid = []

for i, ti in enumerate(tickets):
    for t in ti:
        t = int(t)
        tfound = False
        for ru in rules:
            # print(ru)
            for r in range(0, len(ru), 2):
                # print(t,r)
                if int(ru[r])<t<int(ru[r+1]):
                    # print('fit')
                    tfound = True
                    break
                # else:
                #     # print('nofit')
            if tfound:
                break
        if not tfound:
            ans += t
            invalid.append(i)
            # print(t, 'was not found')
            # print(i)
            
            
                # re.search(r,t)
print(ans)

# ------------ Part 2 -------------

# Remove invalid tickets from tickets
for i in invalid[::-1]:
    tickets.pop(i)

options = [ [] for _ in range(len(rules)) ]


for r, rule in enumerate(rules):
    for i in range(len(rules)):
        check = True
        for ticket in tickets: #Check if the rule is true for all tickets
            number = int(ticket[i])
            if not (int(rule[0])<=number<=int(rule[1]) or int(rule[2])<=number<=int(rule[3])):
                # print(rule, 'is not true on ', number)
                check = False
                break
        if check:
            options[i].append(r)
            # print('Rule number',r, 'is valid on position', i)



rulepos = [0]*len(rules)
empty = False
l = 0
while not(empty) and l<25:
    l+= 1
    for i in range(len(rules)):
        
        if len(options[i]) == 1:
            print('Position', i, 'can only belong to rule', options[i][0])
            rulepos[options[i][0]] = i
            for j in range(len(options)):
                if i != j and options[i][0] in options[j]: 
                    options[j].remove(options[i][0])
                    
            options[i] = []
            
print(rulepos)

ans = 1
for r, name in enumerate(rulenames):
    if name[0:3] == 'dep':
        print(name, r, rulepos[r], myticket[rulepos[r]])
        ans *= int(myticket[rulepos[r]])
    # print(name)
        
print(ans)































