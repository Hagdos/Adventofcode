# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:24:13 2020

@author: Tom
"""

import math


f = open('Map.txt')

locations = []

x = 0
y = 0

for r in f:
    x = 0
    print(r.strip())
    for c in r:
        if c == '#':
            locations.append([x,y])
        x+=1
    y+=1
    
def calcangle(loc1, loc2):
    dx = loc2[0]-loc1[0]
    dy = loc2[1]-loc1[1]
    gcd = math.gcd(dx,dy)
    angle = [dx/gcd, dy/gcd]
    return angle
    
longest = 0
bestloc = 0

for M in locations:
    Angles = set()
    for a in locations:
        if a != M:
            Angles.add(tuple(calcangle(M, a)))
            if len(Angles) > longest:
                longest = len(Angles)
                MonitorAngles = list(Angles)
                location = M
            
print('Answer Part 1 = ',longest)


# ------------------ Part 2 -------------------\

MonitorAngles.sort()
i = 0
Mangle = []
for x,y in MonitorAngles:
    i+= 1
    
    if y < 0:
        if x >= 0:
            a = math.atan(x/-y)/math.pi
        elif x < 0:
            a = math.atan(y/x)/math.pi+1.5
    elif y > 0:
        if x > 0:
            a = math.atan(y/x)/math.pi+0.5
        elif x <= 0:    
            a = math.atan(-x/y)/math.pi+1
            
    Mangle.append((a,x,y))
            
Mangle.sort()

# print(Mangle[199])
# print(Location)
# print(Location[0] + Mangle[199][1], Location[1] + Mangle[199][2])

xloc = location[0] + Mangle[199][1]
yloc = location[1] + Mangle[199][2]

print(location)
print(location[0] + Mangle[199][1], location[1] + Mangle[199][2])
        
print('Answer part 2 = ', (xloc+1)*100+yloc+1)
        
#605 is too low
#10090 is too high








































