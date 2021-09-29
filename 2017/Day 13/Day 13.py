def calcScannerLocation(depth, time):
    location = time % (depth * 2 - 2)
    if location // depth:
        return 2 * depth - location - 2
    else:
        return location


def calcPrice(firewalls, starttime):
    ans = 0
    for firewall in firewalls.keys():
        if calcScannerLocation(firewalls[firewall], firewall+starttime) == 0:
            ans += firewalls[firewall] * firewall
    return ans


def checkPass(firewalls, starttime):
    for firewall in firewalls.keys():
        if calcScannerLocation(firewalls[firewall], firewall+starttime) == 0:
            return False
    return True


file = open('input.txt').readlines()

firewalls = dict()

for line in file:
    data = line.strip().split(': ')
    firewall = int(data[0])
    firewalls[firewall] = int(data[1])

ans1 = calcPrice(firewalls, 0)

Passed = False
starttime = 0
while not Passed:
    starttime += 1
    Passed = checkPass(firewalls, starttime)

ans2 = starttime

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
