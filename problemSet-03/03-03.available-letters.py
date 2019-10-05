#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:14:27 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03-03 Printing Out all Available Letters
-----------------------------------------
Next, 
implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. 

This function returns a string that is comprised of 
lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Note that this function should return the letters in alphabetical order

For this function, you may assume that all the letters in lettersGuessed are lowercase.
"""

"""Answer Script:"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letterList = list(string.ascii_lowercase)
    outString = ''
    for letter in lettersGuessed:
        if letter in letterList:            
            letterList.remove(letter)
    for char in letterList:
        outString += char
    return outString 
