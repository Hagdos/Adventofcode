import time

def calcPrice(firewalls, starttime):
    ans = 0
    for firewall in firewalls.keys():
        if (firewall+starttime) % (firewalls[firewall] * 2 - 2) == 0:
            ans += firewalls[firewall] * firewall
    return ans


def checkPass(firewalls, starttime):
    for firewall in firewalls.keys():
        if (firewall+starttime) % (firewalls[firewall] * 2 - 2) == 0:
            return False
    return True


file = open('input.txt').readlines()

firewalls = dict()

for line in file:
    data = line.strip().split(': ')
    firewall = int(data[0])
    firewalls[firewall] = int(data[1])

ans1 = calcPrice(firewalls, 0)

start = time.time()

Passed = False
starttime = 0
while not Passed:
    starttime += 1
    Passed = checkPass(firewalls, starttime)

ans2 = starttime

print(time.time()-start)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
