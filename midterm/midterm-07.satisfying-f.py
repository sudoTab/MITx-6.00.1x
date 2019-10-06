#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:42:56 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
Midterm-07 Satisfies F
-----------------------
Write a Python function called satisfiesF that has the specification below. 

Then make the function call run_satisfiesF(L, satisfiesF).

def satisfiesF(L):
    '''
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    '''
    # Your function implementation here

run_satisfiesF(L, satisfiesF)
"""

"""Answer Script:"""
def satisfiesF(L):
    removelist=list()
    for i in range(0, len(L)):
        if f(L[i]) == False:
            removelist.append (L[i])
    if removelist:
        for k in removelist:
            L.remove(k)   
    return len(L)
    
run_satisfiesF(L, satisfiesF)

"""
##Test Function:
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
"""