# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:37:12 2022

@author: SMITHA
"""

p = int(input("Enter the princile"))
t = int(input("Enter the time"))
r = float(input("Enter the rate of interest"))
si = (p*t*r)/100
print("Simple interest is",si) 
amount = si+p
print("Amount after maturity is",amount)
