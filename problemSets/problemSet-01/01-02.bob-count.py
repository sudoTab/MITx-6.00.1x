#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:05:55 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
01-02 Bob Count
----------------
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
"""

"""Answer script:"""
## Test string
s = 'phngluingboblwnafhcthulhurboobobooblyehwgahnaglfhtagnbobob'

# Number of bobs
bobNumb = 0
# Length of s
l = len(s)

# The 'for' loop
# add '1' to 'l' because range stop is not inclusive of itself.
for i in range(l+1):
    # Block 01: 'if' statement
    # If slice s[start at i , stop at (i+3)] is equal to 'bob'
    if s[i:(i+3)] == 'bob':
        # Add step the bob count by '1'
        bobNumb += 1
# End of our 'for' loop. Print the number of 'bob's
print('Number of times bob occurs is: ', str(bobNumb))

