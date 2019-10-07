#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:45:02 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03.5-Finger Odd Tuples
-----------------------
Write a procedure called oddTuples, 
which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. 

So if test is the tuple 

    ('I', 'am', 'a', 'test', 'tuple'), 
    
then evaluating oddTuples on this input would return the tuple 

    ('I', 'a', 'tuple'). 
"""

"""Answer Script"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    xTup = ()
    index = 0

    while index < len(aTup):
        xTup += (aTup[index],)
        index += 2

    return xTup
