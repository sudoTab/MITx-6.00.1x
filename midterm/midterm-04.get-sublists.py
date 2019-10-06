#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:42:39 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
Midterm-04 Get Sublists
------------------------
Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

    assume L is not empty
    assume 0 < n <= len(L)

This function returns a list of all possible sublists in L of length n without skipping elements in L. 

The sublists in the returned list should be ordered in the way they appear in L, 
with those sublists starting from a smaller index being at the front of the list.
"""

"""Answer Script:"""
def getSublists(L, n):
    list_of_sublists = [] 	
    for i in range(len(L)-n+1):
        list_of_sublists.append(L[i:i+n])
    return list_of_sublists
