tree = "(0 4 0(0 16 88(0 33(2(16))(4(2 88)(2(16))(33)(0 32(3(-1)(3 0(-2)))(4(2(32(16)2))(2(3(16)23))))(0 17 89(1(3(16)(17))(999)(0 16 120(4(2(16))(33)))))))))"
tree = "(0 32(3(-1)(3 0(-2)))(0 4 0(0 33(1(-2)(32(-1)(33(-1)((3 -3 -6)((3 14 16))(3 -6 -7))))0)(0 34(1(32(-1)1)(32(3 -19 -20)(34(((3(3 34((3 17 14)22 11))20)22 19)(-1)((3 -22 -20)))(-2)))-1)(0 37(1(-1)((3 11 11)35(34(-1)10)((3 -13 -13)36(3(-1)((3(3 44(3(3(3 15 10)-6)-3))-3)(35)10))((3 -13 -17)(37((3 53 18)))((3 -2 -4)(32 48((3 54 18)))))))0)(0 38(4((3(3 19 -18)0)(((3 -4(3(3 -19 7)-19))((3 -4 -7)-15 5)-17)))((3 -6 -7)(-1)(((3 16 13)23(3 31 12))(2 44)(38(3(-1)1)(-3)(32(-2)(-3))))0))((3(3 50 16)-4)12 0 1)))))))"

tree = tree.replace('(', ' ( ')
tree = tree.replace(')', ' ) ')
tree = tree.split()

def isint(s):
    if s[0] == '-':
        return s[1:].isdigit()
    return s.isdigit()

def split_branch(branch, pointer):
    l = []
    while pointer < len(branch):
        char = branch[pointer]
        # print(char, l)
        pointer += 1
        if char == '(':
            array, pointer = split_branch(branch, pointer)
            l.append(array)
        elif isint(char):
            l.append(int(char))
        elif char == ')':
            return l, pointer

def resolve_branch(branch):
    first = return_leaf(branch[0])
    if first == 1:
        second = return_leaf(branch[1])
        if second > 0:
            return return_leaf(branch[2])
        else:
            return return_leaf(branch[3])
    elif first == 3:
        return return_leaf(branch[1]) - return_leaf(branch[2])
    else:
        return sum([return_leaf(b) for b in branch])


def return_leaf(leaf):
    if type(leaf) == int:
        return leaf
    else:
        return resolve_branch(leaf)

tree = split_branch(tree, 1)[0]
ans = resolve_branch(tree)

print(ans)