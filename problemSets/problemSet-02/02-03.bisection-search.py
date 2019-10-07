#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:12:26 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02-03 Using Bisection Search to Make the Program Faster
--------------------------------------------------------
The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

Bounds:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent.
(no more multiples of $10) such that we can pay off the debt within a year.

Note: your code only has 30 seconds to run.
"""

"""Answer Script:"""
##Test Case 1:
balance = 320000
annualInterestRate = 0.2

startingBalance = balance
monthlyInterestRate = annualInterestRate/12
monthlyPaymentRate = 0
upperBound = (startingBalance*(1+monthlyInterestRate)**12)/12
lowerBound = startingBalance/12
epsilon = 0.01

while abs(balance) >= epsilon:
    balance = startingBalance
    for i in range(12):
        outstandingBal = balance - monthlyPaymentRate
        balance = outstandingBal + (outstandingBal * monthlyInterestRate)
    if balance > epsilon :
        lowerBound = monthlyPaymentRate
    else:
        upperBound = monthlyPaymentRate
    monthlyPaymentRate = (lowerBound + upperBound) / 2.0

print('Lowest Payment:', round(monthlyPaymentRate,2))
