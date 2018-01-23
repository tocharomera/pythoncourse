#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:53:53 2018

@author: mariachi
"""
balance = 320000; annualInterestRate = 0.2;
minim = balance / 12
maxim = balance / 12  + ((balance)*(annualInterestRate/12))
paymonthly = (minim+maxim)/2
mainbalance = balance
interest = balance*(annualInterestRate/12) 
def payOff(balance, annualInterestRate, month, inter):
    while month <12:  
       return payOff(balance-paymonthly, annualInterestRate, month+1, inter+(annualInterestRate/12)*balance)
    if month >= 12:
        print("interst "+str(inter))
        print("paybalance "+str(paymonthly))
        return inter
print( str(payOff(balance-paymonthly, annualInterestRate, 0, 0)))

def bisect(balance, minim, maxim, paymonthly):
    while round(balance-(paymonthly*12),2)!=0:
        if round(balance-(paymonthly*12),2)> 0:
            minim = paymonthly
            approx = (minim+maxim)/2
            print(round(paymonthly,2))
            
            return bisect(balance, paymonthly, maxim, approx)
        if round(balance-(paymonthly*12),2)<0:
            maxim = paymonthly
            approx = (minim+maxim)/2
            print(round(paymonthly,2))
            
            return bisect(balance, minim, paymonthly, approx)
    if round(balance-(paymonthly*12),2)==0:
        return print("Lowest Payment : "+str(paymonthly))
#bisect(balance+interest, minim, maxim, paymonthly)