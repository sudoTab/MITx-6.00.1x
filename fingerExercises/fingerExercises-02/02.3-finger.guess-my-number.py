#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 01:26:40 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02.3-Finger Guess My Number
----------------------------
In this problem, you'll create a program that guesses a secret number!

The program works as follows: 
    
    you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
    
    The computer makes guesses, and you give it input - is its guess too high or too low? 
    
    Using bisection search, the computer will guess the user's secret number!
    
Note:
    
    Your program should use input to obtain the user's input! 
    
    Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, 
you should print out a message to the user explaining you did not understand their input. 

Then, you should re-ask the question, and prompt again for input.
"""

"""Answer Script:"""
high = 100
low = 0

print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
