#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:27:26 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
Midterm-06 Lace Strings Recursion
----------------------------------
Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces together two strings. 

Your procedure should not use any explicit loop mechanism, such as a for or while loop. 

We have provided a template of the code; 
your job is to insert a single line of code in each of the indicated places.

For this problem, you must add exactly one line of code in each of the three places where we specify to write a line of code. 

If you add more lines, your code will not count as correct.

Here is the template you will fill in, for reference:

def laceStringsRecur(s1, s2):
    '''
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    '''
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
        if s2 == '':
            #PLACE A LINE OF CODE HERE
        else:
            #PLACE A LINE OF CODE HERE
    return helpLaceStrings(s1, s2, '')
"""

"""Answer Script:"""
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out+s2
        if s2 == '':
            return out+s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])
    return helpLaceStrings(s1, s2, '')

