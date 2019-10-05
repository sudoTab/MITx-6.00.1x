#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:22:08 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
03-04 The Game
---------------
Now you will implement the function hangman, which takes one parameter - 
the secretWord the user is to guess. 

This starts up an interactive game of Hangman between the user and the computer. 

Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
"""

"""Answer Script:"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    wrongGuess, lettersGuessed = 0, []
    while 8 - wrongGuess > 0:
        alph = getAvailableLetters(lettersGuessed)
        print('-------------')
        print('You have ' +  str(8 - wrongGuess) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        userGuess = input('Please guess a letter: ')
        lettersGuessed.append(userGuess)
        if userGuess in secretWord and userGuess in alph:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        elif userGuess not in secretWord and userGuess in alph:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            wrongGuess +=1
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            break
    print('------------')
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)