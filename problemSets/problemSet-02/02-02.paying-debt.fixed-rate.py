#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:29:53 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02-02 Paying Debt off in a Year - Fixed Rate
---------------------------------------------
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

 The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year
 
 Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months.
 Notice that it is possible for the balance to become negative using this payment scheme, which is okay.
 """
 
"""Answer Script:"""
##Test Case 1:
balance = 3329
annualInterestRate = .2

startingBalance = balance
monthlyPaymentRate = 0
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        outstandingBal = balance - monthlyPaymentRate
        balance = outstandingBal + (outstandingBal * monthlyInterestRate)
    if balance <= 0:
        break
    else:
        monthlyPaymentRate += 10
        balance = startingBalance

print('Lowest Payment:', monthlyPaymentRate)
