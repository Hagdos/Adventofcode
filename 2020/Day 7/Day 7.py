import re
import matplotlib

contentsearch = ['shiny gold bag']

for i in range(100):
    size1 = len(contentsearch)
    f = open('Rulestest.txt')
    # print(contentsearch)
    # print('\n')
    # print(i)
    for x in f:
        container = re.findall('^[\w\s]+? bag', x)[0]
        content = re.findall(' (\w+ \w+ bag)', x)
        
        
        for s in contentsearch:
            if s in content and container not in contentsearch:
                contentsearch.append(container)
    if size1 == len(contentsearch):
        break

            
# print(contentsearch)
# print(len(contentsearch)-1)



# ---- Part 2 ----

def countcontent(container):
    index = containers.index(container)
    amount = 0
    
    for x in content[index]:
        amount += int(x[0])
        amount += countcontent(x[1])*int(x[0])
        
    return amount

f = open('Rules.txt')

containers = []
content = []

for x in f:
        containers.append(re.findall('^[\w\s]+? bag', x)[0])
        content.append(re.findall(' (\d) (\w+ \w+ bag)', x))

# print(containers[7], '\n',  content[7])

size = []
for x in containers:
    size.append(countcontent(x))

    
# print(countcontent('shiny gold bag'))    
print(max(size))

matplotlib.pyplot.plot([1])

    
    
    
    
    
