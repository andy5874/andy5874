# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:39:30 2020

@author: cjdgh
"""


'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''


class Account(object):
    ''' bank account details'''
    
    def __init__ (self, balance = 0.0):
       
        self.balance = balance
    
    def withdraw(self):
        amount = float(input('how much would you like to withdraw'))
        if amount > self.balance:
            print('you dont have enough balance')
        else:
            self.balance -= amount
            print(f'you withdrew {amount} and have {self.balance} left')
            
    def deposit (self):
        amount = float(input('how much would you like to deposit'))
        self.balance += amount
        print(f'you deposited {amount} and have {self.balance} in your account')
        
    def show_balance (self):
        print(f'you have {self.balance} in your account')
        
andy = Account (1000)
