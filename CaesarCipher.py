# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:02:28 2020

@author: andy
"""



def encrypt(message, key):
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher =''
    new_message = message.lower()
    for char in new_message:
        if char not in alphabet:
            cipher += char
        else:
            index = alphabet.find(char)
            cipher = cipher + alphabet[shift(index + key)]
    return cipher




def shift (shift_amount):
  
    return shift_amount % 26

message = input('what is your message')
key = int(input('whats the number'))

cipher_message = encrypt(message, key)
print (cipher_message)
