# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:37:57 2020

@author: Tom Kooyman
"""
import copy
test = []

for i in range(3):
    test.append([1, 2, 3])
    
    
testcopy = copy.deepcopy(test)
test[2][2] = 18

print(testcopy)
print(test)