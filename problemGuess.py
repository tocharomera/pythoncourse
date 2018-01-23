#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:57:50 2018

@author: mariachi
"""
guess = 50 ;
solution = 0;
minim = 0;
maxim = 100;
print("Please think of a number between 0 and 100!")
ans = input("is your secret number"+ str(guess) + "?")
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    
while(solution == 0):

    if(ans == "h"):
        
        maxim = guess
        guess = int((minim+maxim)/2);
        ans = input("is your secret number"+ str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    elif(ans == "l"):
        minim = guess;
        
        guess = int((minim+maxim)/2);
        ans = input("is your secret number"+ str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    elif(ans == "c"):
        print("Game over. Your secret number was: " + str(guess))
        solution=1
    else:
        print("sorry I didn't understand your answer")
        print("is your secret number"+ str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly", end=" ")
        ans = input()
        