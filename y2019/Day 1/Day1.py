fuel = [int(int(line)/3)-2 for line in open('fuel.txt').read().split('\n')]
print(sum(fuel))

# ----------- Part 2 -----------

newfuel = []
for f in fuel:
    addedfuel = f
    nfuel = 0
    while addedfuel > 0:
        nfuel += addedfuel
        addedfuel = int(int(addedfuel)/3)-2
    newfuel.append(nfuel)

print(sum(newfuel))