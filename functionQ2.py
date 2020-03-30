# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:11:38 2020

@author: cjdgh
"""


'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''

def multiply(a,b=2):
    return a*b

print(f'input of 2 gives {multiply(2)} ')
print(f'input of 3 and 4 gives {multiply(3,4)} ')