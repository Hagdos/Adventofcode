import time

start = time.time()

filename = 'input.txt'
data = open(filename)

data = [line.strip().split(': ') for line in data]

scores = []
ncards = [1]*len(data)
for cardname, numbers in data:
    cardnumber = int(cardname.split()[1])
    winning, numbers = [[int(i) for i in n.split()] for n in numbers.split(' | ')]

    score = len([n for n in numbers if n in winning])
    scores.append(score)

    for cn in range(cardnumber, cardnumber+score):
        ncards[cn] += ncards[cardnumber-1]


ans1 = sum([int(2**(s-1)) for s in scores])

print(f"Took {(time.time()-start)*1000} seconds")

print(ans1)
print(sum(ncards))


