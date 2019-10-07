#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:17:17 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
01-01 Vowel Count
------------------
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

Note: Do not include input statements or define variables we told you would be given. Our automated testing will provide values for you.
"""

"""Answer script:"""
## Test string
s = 'phngluinglwnafhcthulhurlyehwgahnaglfhtagn'

# Vowel counter
vowelNumb = 0

# The 'for' loop
for letter in s:
    # Block 01: 'if' statement
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        # Add step vowel count by '1'
        vowelNumb += 1
# Once all letters in 's' are evaluated, loop will exit here and print the followig
print('Number of vowels: ' + str(vowelNumb))

