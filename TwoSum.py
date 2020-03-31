# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:59:29 2020

@author: andy
"""


def calculate(number_list):
    '''takes in a number list and iterates to find if two pairseqal to 10'''
    number_pairs = {}
    for i in number_list:
        pair = 10-i
        if pair in number_list:
            number_pairs[i] = pair
    return number_pairs


user_input = input('Please enter a number type exit to stop:> ')
numbers = []
while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('That is not a number! Numbers only please:> ')
        user_input = input('Try again:> ')
    numbers.append(int(user_input))
    user_input = input('Please enter next number:> ')
    
pairs = calculate(numbers)
if len(pairs) ==0:
    print('-1')
else:
    print(pairs)