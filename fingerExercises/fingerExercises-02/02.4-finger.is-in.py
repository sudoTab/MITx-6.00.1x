#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:35:22 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.4-Finger Is In
------------------
We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.

First, 
test the middle character of a string against the character you're looking for (the "test character"). 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, 
check if the test character is "smaller" than the middle character. 
If so, we need only consider the lower half of the string; 
otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if 
char is in aStr. 
char will be a single character and aStr will be a string that is in alphabetical order. 
The function should return a boolean value. 
"""

"""Answer Script:"""
def isIn(char, aStr):
    if len(aStr) <= 1:
        return [char] == aStr

    half = len(aStr) // 2
    if char == aStr[half]:
        return True
    elif char > aStr[half]:
        return isIn(char, aStr[half:])
    else:
        return isIn(char, aStr[:half])
    