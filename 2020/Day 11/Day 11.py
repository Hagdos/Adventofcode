# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:08:26 2020

@author: Tom
"""
import copy
import time

f = open('Layout.txt')

Layout = []


for line in f:
    Layout.append(list(line.strip()))
    
V = len(Layout)
H = len(Layout[0])
    
def printlayout(L):
    for row in L:
        print(''.join(row))
    print('\n')
    
def countoccupied(L, v, h):

    count = 0
    for a in range(v-1, v+2):
        for b in range(h-1, h+2):
            if a == v and b == h:
                continue
            if 0<=a<V and 0<=b<H and  L[a][b] == '#':
                count += 1
    return count
                
Layout2 = copy.deepcopy(Layout)
Layoutnew = copy.deepcopy(Layout)

z = 0
t = time.time()

while z < 1000:
    z += 1
    for x in range(len(Layout)):
        for y in range(len(Layout[0])):
            if Layout[x][y] == 'L' and countoccupied(Layout, x, y) == 0:
                Layoutnew[x][y] = '#'
            elif Layout[x][y] == '#' and countoccupied(Layout, x, y) >= 4:
                Layoutnew[x][y] = 'L'

            
    if Layoutnew == Layout:
        print('Found solution')
        s = 0
        for x in Layoutnew:
            s+=(''.join(x).count('#'))
        print(s, '\n')
        break
    else:
        Layout = copy.deepcopy(Layoutnew)

print(time.time()-t)
t = time.time()


# ------------------------------------------ Part 2 ----------------------------------

def checknearestseat(A):
    # print(list(A))
    for i in A:
        if i == '#':
            return 1
        elif i == 'L':
            return 0
        else:
            continue
    return 0

def countoccupied2(L, v, h):
    count = 0
    V = len(L)
    H = len(L[0])
   
    #Look right
    count += checknearestseat(L[v][h+1:])
    
    # #Left
    A = L[v][:h]
    A.reverse()
    count += checknearestseat(A)
    
    # #Up
    count += checknearestseat(i for row in L[v+1:] for i in row[h])
    
    # #Down
    A = list(i for row in L[0:v] for i in row[h])
    A.reverse()
    count += checknearestseat(A)
        
    # Look right-down
    A = (L[i][j] for (i,j) in zip(range(v+1,V),range(h+1,H)))
    count += checknearestseat(A)

        
    # Look left-down   
    A = (L[i][j] for (i,j) in zip(range(v+1,V),range(h-1, -1, -1)))
    count += checknearestseat(A)
        
    # Look right-up   
    A = (L[i][j] for (i,j) in zip(range(v-1, -1, -1),range(h+1,H)))
    count += checknearestseat(A)
    

    # # Look left-up   
    A = (L[i][j] for (i,j) in zip(range(v-1, -1, -1),range(h-1, -1, -1)))
    count += checknearestseat(A)
        
    return count

def checkseat2(L, v, h):
    s = countoccupied2(L, v, h)
    if L[x][y] == '.':
        return '.'
    elif L[x][y] == 'L':
        if s == 0:
            return '#'
        else:
            return 'L'
    elif L[x][y] == '#':
        if s >= 5:
            return 'L'
        else:
            return '#'
    else:
        return 'error'
        print("Something went wrong")


# printlayout(Layout2)

z = 0;
while z < 100:
    # printlayout(Layout2)
    Layoutnew = []
    z += 1
    for x in range(len(Layout2)):
        Layoutnew.append([])
        for y in range(len(Layout2[x])):
            Layoutnew[x].append(checkseat2(Layout2,x,y))
                
            
    if Layoutnew == Layout2:
        print('Found solution')
        print(time.time()-t)
        s = 0
        for x in Layoutnew:
            s+=(''.join(x).count('#'))
        print(s, '\n')
        break
    
    else:
        Layout2 = Layoutnew[:]
    

#     Layoutnew = []
#     z += 1
#     for x in range(len(Layout2)):
#         Layoutnew.append([])
#         for y in range(len(Layout2[x])):
#             Layoutnew[x].append(checkseat2(Layout2,x,y))
      

#     printlayout(Layoutnew)  
      
#     if Layoutnew == Layout2:
#         print('Found solution')
#         s = 0
#         for x in Layoutnew:
#             s+=(''.join(x).count('#'))
#         print(s, '\n')
#         break
#     else:
        
#         Layout2 = Layoutnew[:]

# printlayout(Layout)
# print(countoccupied2(Layout, 9,7))













































