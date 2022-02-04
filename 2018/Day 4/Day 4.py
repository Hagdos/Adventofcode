from collections import defaultdict

file = open('2018/Day 4/input.txt').readlines()
data = [x.strip() for x in file]

data.sort()
sleeptime = defaultdict(int)
sleepminutes = defaultdict(lambda: defaultdict(int))

guard = None
for line in data:
    words = line.split(' ')
    time = words[1].strip(']').split(':')
    if words[-1] == 'shift':
        guard = int(words[3].strip('#'))
    elif words[-1] == 'asleep':
        tstart = int(time[1])
    elif words[-1] == 'up':
        tend = int(time[1])
        sleeptime[guard] += tend - tstart
        for t in range(tstart, tend):
            sleepminutes[guard][t] += 1

maxsleeptime = 0
maxminutes = 0
for guard in sleeptime.keys():
    if sleeptime[guard] > maxsleeptime:
        maxsleeptime = sleeptime[guard]
        sleepiestGuard = guard
    for minute in sleepminutes[guard].keys():
        if sleepminutes[guard][minute] > maxminutes:
            maxminutes = sleepminutes[guard][minute]
            bestminute2 = minute
            bestguard = guard


# is too low14275

maxminutes = 0
for minute in sleepminutes[sleepiestGuard].keys():
    if sleepminutes[sleepiestGuard][minute] > maxminutes:
        maxminutes = sleepminutes[sleepiestGuard][minute]
        bestminute = minute

print(f'The answer to part 1: {sleepiestGuard*bestminute}')

print(f'The answer to part 2: {bestguard*bestminute2}')
