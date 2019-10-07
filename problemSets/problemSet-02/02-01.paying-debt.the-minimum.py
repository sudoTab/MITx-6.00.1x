#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:18:38 2019

@author: sodatab

MITx: 6.00.1x
"""

"""
02-01 Paying Debt off in a Year - The Minimum
----------------------------------------------
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy
"""

"""Answer Script:"""
## Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#For each month:
months = 1
while months <= 12:
    #Compute the monthly payment, based on the previous month’s balance.
    minPayment = balance * monthlyPaymentRate
    #Update the outstanding balance by removing the payment, then charging interest on the result.
    outstandingBal = balance - minPayment
    interest = (annualInterestRate/12) * outstandingBal
    balance = outstandingBal + interest
    #Keep track of the total amount of paid over all the past months so far.
    months +=1
#Print out the result statement with the total amount paid and the remaining balance.
print('Remaining balance: ' + str(round(balance,2)))
