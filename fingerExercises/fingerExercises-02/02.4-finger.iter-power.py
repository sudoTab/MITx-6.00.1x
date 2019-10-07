#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:09:00 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.4-Finger Iterative Power
-----------------------
Write an iterative function iterPower(base, exp) 
that calculates the exponential baseexp by simply using successive multiplication. 

For example, 
iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. 
Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed. 
"""

"""Answer Script:"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        result = base
        while exp > 1:
            result = result*base
            exp-=1
        return result
