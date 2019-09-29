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

# vowel count
vowelNumb = 0

# the for loop
for letter in s:
    # Block: if statement
    if (str(letter) == 'a' or str(letter) == 'e' or str(letter) == 'i' or str(letter) == 'o' or str(letter) == 'u'):
        # plus step vowel count
        vowelNumb += 1
# once all letters in s are evaluated, loop will exit here and print the following.
print('Number of vowels: ', int(vowelNumb))
