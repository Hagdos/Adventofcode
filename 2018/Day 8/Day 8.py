def sumMeta(tree, index):
    nodes = tree[index]
    datas = tree[index+1]
    index += 2
    s = 0

    for node in range(nodes):
        index, ns = sumMeta(tree, index)
        s += ns

    for data in range(datas):
        s += tree[index]
        index += 1

    return index, s


def valueMeta(tree, index):
    value = 0
    nodes = [0] * tree[index]
    datas = tree[index+1]
    index += 2

    for node in range(len(nodes)):
        index, nodes[node] = valueMeta(tree, index)

    if not nodes:
        for data in range(datas):
            value += tree[index]
            index += 1

    else:
        for data in range(datas):
            if tree[index] <= len(nodes):
                value += nodes[tree[index]-1]
            index += 1

    return index, value

file = open('input.txt').read()
rules = list(map(int, file.strip().split()))


_, ans1 = sumMeta(rules, 0)

_, ans2 = valueMeta(rules, 0)

print(f'The answer to part 1: {ans1}')
print(f'The answer to part 2: {ans2}')