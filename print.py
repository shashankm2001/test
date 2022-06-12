# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:35:42 2022

@author: SMITHA
"""
name = "John"
marks=95.60128
print("Name is %s and  Marks is %.4f"%(name,marks))
print("Name is {} and  Marks is {}".format(name, marks))

print("Enter 3 numbers")
a = [int(x) for x in input().split(',')]
print(a)