# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:39:45 2020

@author: andy

Guess the number
"""


import random

number = random.randint(0,100)


user_guess = int(input('guess number between 0 to 100'))
while not str(user_guess).isdigit():
    user_guess = int(input('thats not a number please choose a nubmer'))
    
while user_guess != number:
    if user_guess > number:
        print('lower')
    else:
        print('higher')
            
    user_guess = int(input('input new number'))
    
print(f'your number {user_guess} is the correct number')