# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:55:08 2020

@author: cjdgh
"""


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

import math

class CircleArea (object):
    def __init__ (self, radius):
        self.radius = radius
        
    def get_area(self):
        area = math.pi * self.radius**2
        return area
    
circle = CircleArea(5)