#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:05:55 2019

@author: sodatab
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
"""

## test sting
s = 'phngluingboblwnafhcthulhurboobobooblyehwgahnaglfhtagnbobob'

# number of bobs
bobNumb = 0
# length of s
l = len(s)

# the for loop
# add 1 to l because range stop is not inclusive of itself.
for i in range(l+1):
    # Block: if statement
    # if slice s[start at i , stop at (i+3)] is equal to 'bob'
    if s[i:(i+3)] == 'bob':
        # add step the bob count by one.
        bobNumb += 1
# end of our for loop. print the number of bobs.
print('Number of times bob occurs is: ', str(bobNumb))

