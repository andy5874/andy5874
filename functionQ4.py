# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:23:36 2020

@author: cjdgh
"""


'''
Question 4
Create a new file called capitals.txt , store the names of five countries
in the file on the same line.
'''

f = open('countries.txt', 'w')

f.write('korea\naustralia\namerica\nitaly\ngermany')

f.close()