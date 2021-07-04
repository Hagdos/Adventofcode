import hashlib

ID = 'ugkcyxxp'
iterations = 50000000
password1 = []
password2 = [0]*8

for i in range(iterations):
    hash = hashlib.md5(''.join([ID, str(i)]).encode()).hexdigest()
    if hash[:5] == '00000':
        print(hash)
        if len(password1) < 8:
            password1.append(hash[5])
        
        try:
            if int(hash[5]) in range(8):
                if password2[int(hash[5])] == 0:
                    password2[int(hash[5])] = hash[6]
        except:
            pass
        
        if 0 not in password2:
            print(i)
            break
        
print('Answer to Part 1:', ''.join(password1))

print('Answer to Part 2:', ''.join(password2))