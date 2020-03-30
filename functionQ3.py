# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:15:04 2020

@author: cjdgh
"""


'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''

def power (a,b = 2):
    return a**b

print(f'input of 3 gives {power(3)}')
print(f'input of 3 and 3 gives {power(3,3)}')