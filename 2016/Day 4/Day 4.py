import re
import string

def findCheckSum(name):
    occurences = []
    for letter in string.ascii_lowercase:
        occurences.append((name.count(letter), letter))
        # occurences[letter] = name.count(letter)
    
    occurences = sorted(occurences, key = sortFunction, reverse=True)
    
    checksum = []
    for value in occurences[0:5]:
        checksum.append(value[1])
        
    
    return ''.join(checksum)

def sortFunction(occurence):
    numbervalue = occurence[0] * 100
    lettervalue = 122 - ord(occurence[1])
    return numbervalue + lettervalue

def decodeName(name, ID):
    realname = []
    for char in name:
        if char == '-':
            realname.append(' ')
        else:
            realname.append(chr(((ord(char)-97+ID)%26)+97))
    
    return ''.join(realname)


file = open('input.txt').read()

regex = r'(.*)-([0-9]*)\[(.*)\]'
split = re.findall(regex, file)

answer = 0

for room in split:
    name = room[0]
    ID = int(room[1])
    checksum = room[2]
    
    if checksum == findCheckSum(name):
        answer += ID
    
        if decodeName(name, ID) == 'northpole object storage':
            print('Answer to part 2:', ID)
    
    
print('Answer to part 1:', answer)



