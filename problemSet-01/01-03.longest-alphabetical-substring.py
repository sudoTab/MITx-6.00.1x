#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 04:27:09 2019

@author: sodatab
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

"""
Solution A.
"""
## Test string
s = 'IaIacthulhufhtagnphngluimglwnafhcthulhurlyehwgahnaglfhtagn'

# current substring
cur = s[0]
# Longest substring
longest = s[0]

# for i in range starting at one through the full length of s
for i in range(1, len(s)):
    # if s indexed at i is greater than or equal to current substring indexed at -1
    if s[i] >= cur[-1]:
        # addstep current substring by s indexed at i
        cur += s[i]
        # if length of current substring is greater than the length of the longest substring.
        if len(cur) > len(longest):
            # longest substring gets reassigned to current substring.
            longest = cur
    # or else s indexed at i is assigned to current substring.
    else:
        cur = s[i]
# print the resulting longest substring.
print('Longest substring in alphabetical order is: ', longest)

        