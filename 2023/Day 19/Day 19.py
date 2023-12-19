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



file = open('input.txt').read()

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
print('The answer to part 2: ', ans2)
