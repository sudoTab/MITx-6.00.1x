#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:19:32 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
Midterm-05 Keys with Value
---------------------------
 Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
"""

"""Answer Script"""
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    answer = []
    for i, v in aDict.items():
        if v == target:
            answer.append(i)
    return sorted(answer)

print(keysWithValue({0: 0, 8: 2, 10: 0, 6: 2, 7: 0}, 0))
