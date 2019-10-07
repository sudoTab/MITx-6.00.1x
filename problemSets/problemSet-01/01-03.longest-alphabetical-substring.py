#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 04:27:09 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
01-03 Longest Alphabetical Substring
-------------------------------------
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

"""Answer script:"""
## Test string
s = 'IaIacthulhufhtagnphngluimglwnafhcthulhurlyehwgahnaglfhtagn'

# Current alphabetical substring
currAlph = s[0]
# Longest alphabetical substring
longestAlph = s[0]

# For 'i' in range starting at one through the full length of 's'
for i in range(1, len(s)):
    # If 's' indexed at 'i' is greater than or equal to 'current alphabetical substring' indexed at '-1'
    if s[i] >= currAlph[-1]:
        # Addstep 'current alphabetical substring' by 's' indexed at 'i'
        currAlph += s[i]
        # If length of 'current alphabetical substring' is greater than the length of the 'longest alphabetical substring'
        if len(currAlph) > len(longestAlph):
            # 'Longest alphabetical substring' gets reassigned to 'current alphabetical substring'
            longestAlph = currAlph
    # Or else 's' indexed at 'i' is assigned to 'current alphabetical substring'
    else:
        currAlph = s[i]
# Loop end
# Print the resulting 'longest alphabetical substring'
print('Longest substring in alphabetical order is: ', longestAlph)
