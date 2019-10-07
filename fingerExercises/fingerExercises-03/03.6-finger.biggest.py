#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 03:31:49 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03.6-Finger Biggest
--------------------
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, 
which returns the key corresponding to the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.

If there are no values in the dictionary, biggest should return None. 
"""

"""Answer Script:"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    counter = 0
    result = None
    if aDict == {}:
        return result
    else:
        for i in aDict.keys():
            if len(aDict[i]) > counter:
                result = i
    return result
