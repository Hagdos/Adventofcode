file = open('input.txt').read().splitlines()

# data = [x.strip('\n') for x in file]
data = file.split('\n')

# Define position and direction
position = (0, data[0].find('|'))
direction = [1, 0]
letters = []

for steps in range(1, 1000000):
    newposition = [i + j for i, j in zip(position, direction)]
    if data[newposition[0]][newposition[1]] == ' ':
        direction.reverse()
        newposition = [i + j for i, j in zip(position, direction)]
        if data[newposition[0]][newposition[1]] == ' ':
            direction = [-i for i in direction]
            newposition = [i + j for i, j in zip(position, direction)]
            if data[newposition[0]][newposition[1]] == ' ':
                break
        
    if data[newposition[0]][newposition[1]].isupper():
        letters.append(data[newposition[0]][newposition[1]])
    
    position = newposition
    
              
    # print(position)

print('The answer to part 1: ', ''.join(letters))
print('The answer to part 2: ', steps)

# 16099 is too low