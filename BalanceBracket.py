# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:23:27 2020

@author: andy
"""



def balance_brackets(s):
        
    stack = []
    brackets = {'(':')','[':']','{':'}'}
    
    for char in s:
        
        if char in brackets.keys():
            
            stack.append(char)
            
            print('length before is', len(stack))
        else:
            print('length after is ',len(stack))
            if len(stack) == 0 or brackets[stack.pop()] != char:
                
               
                return False
    print(len(stack))        
    return len(stack) == 0

string = '{[()]}'
print(balance_brackets(string))