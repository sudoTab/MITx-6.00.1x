#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 03:13:04 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03.5-Finger Apply to Each 02
-----------------------------
 Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

Assume that

testList = [1, -4, 8, -9]

For each of the following questions 
(which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), 
provide an expression using applyToEach, so that after evaluation testList has the indicated value. 

Question 02:
print(testList)
  [2, -3, 9, -8]
"""

"""Answer Script:"""
def addOne(b):
        return b + 1

applyToEach(testList, addOne)
