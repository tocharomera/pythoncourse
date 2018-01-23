#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:13:41 2018

@author: mariachi
"""



import math

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

paymonthly = round((balance)/12, -1)
mainbalance = balance
def payOff(balance, annualInterestRate, month, interest):
    inter = interest
    while month <11:        
        return payOff(balance-paymonthly, annualInterestRate, month+1, inter+(annualInterestRate/12)*balance)
    if month >= 11:
        return  "Lowest Payment: "+str(roundup((mainbalance+inter)/12))
        #return payOff(balance, annualInterestRate, month-1)
print(payOff(balance-paymonthly, annualInterestRate, 0, 0))
