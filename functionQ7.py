# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:50:47 2020

@author: cjdgh
"""


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

def copy_file (file1, file2):
    with open (file1, 'r') as f1:
         with open(file2, "w") as f2:
            f2.write(f1.read()) 
            
copy_file('countries.txt', 'new_countries.txt')