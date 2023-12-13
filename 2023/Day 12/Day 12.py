import re

def checkValidity(record, group):
    groups = re.split('\.+', record.strip('.'))
    return group == tuple(len(g) for g in groups)

def fillQuestionmarks(record, numberOfBrokensNeeded):
    numberOfBrokens = record.count('#')
    if numberOfBrokens >= numberOfBrokensNeeded:
        return {record.replace('?', '.')}
    elif numberOfBrokens + record.count('?') <= numberOfBrokensNeeded:
        return {record.replace('?', '#')}
    else:
        r1 = record.replace('?', '.', 1)
        r2 = record.replace('?', '#', 1)
        records = fillQuestionmarks(r1, numberOfBrokensNeeded)
        records.update(fillQuestionmarks(r2, numberOfBrokensNeeded))

        return records

def checkValidOptions(options, group):
    ans = 0
    for o in options:
        if checkValidity(o, group):
            ans += 1
    return ans

file = open('input.txt').readlines()
ans1 = ans2 = 0

for line in file:
    record, group = line.strip().split(' ')
    group = tuple(int(i) for i in group.split(','))

    missingBrokens = sum(group) - record.count('#')

    options = fillQuestionmarks(record, sum(group))
    ans1 += checkValidOptions(options, group)



print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
