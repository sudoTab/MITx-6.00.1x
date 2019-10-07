#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:03:33 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.4-Finger Odd Function
----------------
Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean. 
"""

"""Answer Script:"""
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x%2 != 0
    return x%2 == 0
