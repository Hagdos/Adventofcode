def workflow(part, flow):

    if flow == 'A':
        return True
    elif flow == 'R':
        return False

    for rule in flows[flow]:
        if len(rule) == 2:
            partvalue = part[rule[0][0]]
            value = int(rule[0][2:])
            if rule[0][1] == '>' and partvalue > value:
                return workflow(part, rule[1])
            elif rule[0][1] == '<' and partvalue < value:
                return workflow(part, rule[1])
        elif len(rule) == 1:
            return workflow(part, rule[0])


def calcScore(partranges):
    score = 1
    for param in partranges.values():
        length = param[1]-param[0]
        score *= length
    return score

def fullflow(partranges, flow):

    global flows
    if flow == 'A':
        return calcScore(partranges)
    elif flow == 'R':
        return 0
    
    score = 0
    for rule in flows[flow]:
        if len(rule) == 2:
            parametername = rule[0][0] # This is 'x', 'm', 'a' or 's'
            partrange = partranges[parametername]
            rulevalue = int(rule[0][2:])

            if rule[0][1] == '<':
                split = rulevalue
                if split <= partrange[0]:
                    continue
                elif partrange [0] < split < partrange[1]:
                    newpartrange = [partrange[0], split]
                    newpartranges = partranges.copy()
                    newpartranges[parametername] = newpartrange
                    score += fullflow(newpartranges, rule[1])
                    partranges[parametername] = [split, partrange[1]]
                    continue
                else:
                    score += fullflow(partranges, rule[1])
                    return score
                     
            if rule[0][1] == '>':
                split = rulevalue + 1
                if split >= partrange[1]:
                    continue
                elif partrange[0] < split < partrange[1]:
                    newpartrange = [split, partrange[1]]
                    newpartranges = partranges.copy()
                    newpartranges[parametername] = newpartrange
                    score += fullflow(newpartranges, rule[1])
                    partranges[parametername] = [partrange[0], split]
                    continue
                else:
                    score += fullflow(partranges, rule[1])
                    return score
        elif len(rule) == 1:
            score += fullflow(partranges, rule[0])
            return score

file = open('Day 19/input.txt').read()

ans1 = ans2 = 0

flows, parts = file.split('\n\n')

inputflows = flows.split('\n')
flows = dict()
for flow in inputflows:
    name, rules = flow.strip('}').split('{')
    rules = rules.split(',')
    flows[name] = [r.split(':') for r in rules]

parts = parts.split('\n')
for p in parts:
    p = p.strip('{}').split(',')
    part = dict()
    for param in p:
        name, value = param.split('=')
        part[name] = int(value)

    accepted = workflow(part, 'in')
    if accepted:
        ans1 += sum(part.values())

print('The answer to part 1: ', ans1)

# Use non-inclusive ranges (start included, end not included, like range())
partranges = {'x': (1, 4001),
              'm': (1, 4001),
              'a': (1, 4001),
              's': (1, 4001),
              }

print('The answer to part 2: ', fullflow(partranges, 'in'))

# 95911175491896 is too low