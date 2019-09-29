#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:17:17 2019

@author: sodatab
"""
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

Note: Do not include input statements or define variables we told you would be given. Our automated testing will provide values for you.
"""

# test sting
s = 'phngluinglwnafhcthulhurlyehwgahnaglfhtagn'
# vowel count
vowelNumb = 0

# the for loop
for letter in s:
    # Block: if statement
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        # add step vowel count one
        vowelNumb += 1
# once all letters in s are evaluated, loop will exit here and print the following.
print('Number of vowels: ' + str(vowelNumb))
