# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:45:37 2020

@author: cjdgh
"""


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

def copy_file (file1, file2):
    with open (file1) as f1:
         with open(file2, "w") as f2:
            f2.write(f1.read()) 
            
copy_file('countries.txt', 'new_countries.txt')