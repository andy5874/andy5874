# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:27:36 2020

@author: cjdgh
"""


'''
#Question 5 
#Write some code that requests the user to input another country.
#Add that country to the list of countries countries.txt. Then print the file to
#the screen.
#'''



country = input(' enter a country you d like to add')
f = open('countries.txt', 'a')
f.write('\n' + country)
f.close
    

f = open('countries.txt', 'r')
print(f.read())
f.close

