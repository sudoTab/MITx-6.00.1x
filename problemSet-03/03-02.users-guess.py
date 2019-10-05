#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:02:25 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03-02 Getting the User's Guess
-------------------------------
Next, 
implement the function getGuessedWord that takes in two parameters - 
a string, secretWord, and a list of letters, lettersGuessed. 

This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord.

This shouldn't be too different from isWordGuessed!

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

"""Answer Script:"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter
        else:
            ans += '_ '
    return ans
