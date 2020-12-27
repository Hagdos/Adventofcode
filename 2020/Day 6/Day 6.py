import re

f = open('Forms.txt')
x = f.read(-1)

Groups = re.split("\n\n", x)
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z']

answers = 0

for group in Groups[0:]:
    persons = re.split('\n', group)
    print(persons)
    for letter in Alphabet:
        if (all(letter in j for j in persons)):
            answers += 1
    print(answers)
    # print(answers)
    
    # print("\n")
    
print(answers)


