#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:33:09 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
Midterm-03 Closest Power
-------------------------
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
"""

"""Answer Script:"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    assert base > 1
    assert num > 0
    
    exponent = 0
    
    while True:
        if base**exponent > num:
            if abs(num - base**(exponent - 1)) == abs(base**exponent - num):
                return exponent - 1 
                break
            else:
                return exponent
                break
        elif base**exponent == num:
            return exponent
            break            
        else:
            exponent += 1
    
    return exponent
