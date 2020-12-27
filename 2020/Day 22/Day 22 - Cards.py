import time

f = open('Cards.txt')

# =============================================================================
# Read input
# =============================================================================
p1 = []
p2 = []
two = False
for c in f:
    if c[0] == '\n':
        two = True
    elif two:
        try:
            p2.append(int(c.strip()))
        except:
            pass
    else:
        try:
            p1.append(int(c.strip()))
        except:
            pass
        
p12 = p1[:]
p22 = p2[:]
# print(p1)
# print(p2)
# # =============================================================================
# # Play game - Part 1
# # =============================================================================

while len(p1)>0 and len(p2)>0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1>c2:
        p1.extend([c1, c2])
    elif c2>c1:
        p2.extend([c2, c1])
    else:
        assert False
# =============================================================================
# Calculate answer
# =============================================================================
# print(p1)
ans = 0
for i,c in enumerate(p1[::-1]):
    ans+=(i+1)*c
    # print(i,c)
    
print("Answer to part 1 = ", ans)

# =============================================================================
# Play game - Part 2
# =============================================================================
p1 = p12
p2 = p22

def rcombat(p1, p2, game):
    # print("One layer deeper!")
    combinations = set()
    r = 1
    while len(p1)>0 and len(p2)>0 and r<200000:
        # print('---Round', r, '(Game ', game, ')---')
        # print(p1)
        # print(p2)
        # print()
        r+=1
        
        if tuple(p1 + ['\n'] + p2) in combinations:
            # print("Repetition")
            return 1
        combinations.add(tuple(p1 + ['\n'] + p2))
        # print(hash(tuple(p1 + ['\n'] + p2)))
        
        c1 = p1.pop(0)
        c2 = p2.pop(0)
                
        if c1 <= len(p1) and c2 <= len(p2):
            # print(c1, p1, c2, p2)
            p1s = p1[:c1]
            p2s = p2[:c2]
            if max(p1s) > max(p2s):
                winner = 1
            else:
                winner = rcombat(p1s, p2s, game+1)
            if winner == 1:
                p1.extend([c1, c2])
            elif winner == 2:
                p2.extend([c2, c1])
            else:
                return 0 
        else:    
            if c1>c2:
                p1.extend([c1, c2])
            elif c2>c1:
                p2.extend([c2, c1])
            else:
                assert False
    if len(p2)==0:
        # print("Winner of subgame", game, "is p1")
        return 1
    elif len(p1)==0:
        # print("Winner of subgame", game, "is p2")
        return 2
    else:
        # print("Something went wrong in Game", game, 'round', r)
        return 0
                
            
now = time.time()            
winner = rcombat(p1,p2, 1)
print(time.time()-now)
# # =============================================================================
# Calculate answer
# =============================================================================
# print(p1)
ans = 0
if winner == 1:
    w = p1
elif winner == 2:
    w = p2
    
for i,c in enumerate(w[::-1]):
    ans+=(i+1)*c
    # print(i,c)
    
print("Answer to part 2 = ", ans)
            
# Answer is 35676
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            