#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:11:40 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
01.2-Finger varA varB
----------------------
 Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

    "string involved" if either varA or varB are strings

    "bigger" if varA is larger than varB

    "equal" if varA is equal to varB

    "smaller" if varA is smaller than varB
"""

"""Answer Script:"""
meow = 0

if type(varA) == type('string'):
    print('string involved')
    meow = 1
elif type(varB) == type('string'):
    print('string involved')
    meow = 1
elif meow == 0:
    if varA > varB:
        print("bigger")
    elif varA < varB:
        print("smaller")
    elif varA == varB:
        print("equal")
