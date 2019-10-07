#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 01:48:09 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.4-Finger Eval Quadratic
---------------------------
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a⋅x2+b⋅x+c.

This function takes in four numbers and returns a single number. 
"""

"""Answer Script:"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2+b*x+c
