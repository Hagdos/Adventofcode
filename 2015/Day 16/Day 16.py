text = open('input.txt')

sues = dict()

for line in text:
    line = line.strip().replace(':', '').replace(',', '').split()
    pets = dict()
    for i in range(2,len(line), 2):
        pets[line[i]] = int(line[i+1])
    sues[int(line[1])] = pets
