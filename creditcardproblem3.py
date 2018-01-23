#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:21:48 2018

@author: mariachi
"""

balance = 320000; annualInterestRate = 0.2;
minim = balance / 12
maxim = balance / 12 + (balance*(annualInterestRate/12))
paymonthly = (minim + maxim)/2
interest = balance*(annualInterestRate/12) 
mainbalance = balance
  
def payOff(balance, annualInterestRate, month, inter):
    while month <12:  
       return payOff(balance-paymonthly, annualInterestRate, month+1, inter+(annualInterestRate/12)*balance)
    if month >= 12:
        print("inter "+str(inter))
        print("paybalance "+str(paymonthly))
        return  "Lowest Payment: "+str((mainbalance+inter)/12)
    
print(payOff(balance-paymonthly, annualInterestRate, 0, 0))