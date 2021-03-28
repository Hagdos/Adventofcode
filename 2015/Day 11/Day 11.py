string = 'hxbxwxba'

#Relevant ascii-codes
a = 97
i = 105
o = 111
l = 108
z = 122

# Create array of ascii-characters
chars = []
for char in string:
    chars.append(ord(char))

passwordFound = False
passwordsFound = False

while not passwordsFound:
    # Check character array for three consecutive letters
    consecutive = False
    for position in range(len(chars)-2):
        if chars[position+2] == chars[position+1]+1 and chars[position+1] == chars[position]+1:
            consecutive = True
            
    # Check character array for i, o, l
    iol = False
    if any(x in chars for x in {i, o, l}):
        iol = True
       
    # Check character array for doubles ('aa')
    doubles = 0
    i = 0
    while i < len(chars)-1:
        if chars[i] == chars[i+1]:
            doubles += 1
            i+=1
        i+=1
        
    if consecutive == True and iol == False and doubles >= 2 and passwordFound == True:
        passwordsFound = True
        password2 = []
        for char in chars:
            password2.append(chr(char))
    
    if consecutive == True and iol == False and doubles >= 2 and passwordFound == False:
        passwordFound = True
        password1 = []
        for char in chars:
            password1.append(chr(char))        
    
    i = -1        
    while True:
        chars[i] += 1
        if chars[i] > z:
            chars[i] = a
            i -= 1
        else:
            break

print("Answer to part 1:", ''.join(password1))
print("Answer to part 2:", ''.join(password2))