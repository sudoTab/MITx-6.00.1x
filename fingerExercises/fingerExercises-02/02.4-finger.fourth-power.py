#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 01:52:53 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.4-Finger Fourth Power
-------------------------
Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise (you don't need to redefine square in this box; when you call square, the grader will use our definition).

This function takes in one number and returns one number. 
"""

"""Answer Script:"""
def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))
