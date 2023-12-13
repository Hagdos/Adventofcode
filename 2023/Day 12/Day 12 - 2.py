# New attempt

# If next is # -> Check if fulfills next group requirement. Replace ? with #'s where necessary.
# If next is . -> Put ., move to next character

# If next is ? -> Check if there are enough question marks and/or #'s for the next group.
# If not, only one option, replace all ?'s in next group with .'s

# Else, two options: Add the new group, or add a dot. Split into two options

# String should always end with a '.' -> Assert

# Check for options with the same length and the same remaining groups -> Add their numberofoptions together, merge.

def returnNextStep(line):

    record, group = line
    if len(group) == 0:
        if '#' in record:
            return None
        else:
            return [('', group)]
    if record:
        if record[0] == '.':
            return [(record[1:], group)]
        elif record[0] == '#':
            if len(record) < group[0]:
                return None
            elif '.' in record[:group[0]]: #Check if there are enough #'s and ?'s for the next group
                return None # If not, impossible option
            elif len(record) == group[0] or record[group[0]] in ['.', '?']: #Check if there's a dot possible after the next group or the record ends there
                return [(record[group[0]+1:], group[1:])]

            else:
                return None # Impossible option
        elif record[0] == '?':
            if '.' in record[:group[0]]: #Check if there are enough #'s and ?'s for the next group
                return [(record[1:], group)]    # TODO: This can be sped up, instead of stepping 1 forward, step to the last point within group[0]
            else:
                # Return both options
                return [('.'+record[1:], group), ('#'+record[1:], group)]

        else:
            raise ValueError('Not a valid option')


def countArrangements(record, group):
    lines = {(record, group): 1}
    nextline = [1]
    while(nextline[0] != ''):
        nextline = max(lines, key=lambda k: len(k[0]))
        count = lines.pop(nextline)
        newlines = returnNextStep(nextline)
        if newlines:
            for newline in newlines:
                if newline in lines.keys():
                    lines[newline] += count
                else:
                    lines[newline] = count

    return lines[('', tuple())]



file = open('input.txt').readlines()
ans1 = ans2 = 0

for line in file:
    record, group = line.strip().split(' ')
    group = tuple(int(i) for i in group.split(','))

    ans1 += countArrangements(record, group)

    record = '?'.join([record]*5)
    group = group * 5

    ans2 += countArrangements(record, group)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)