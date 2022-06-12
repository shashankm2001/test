# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:19:58 2022

@author: SMITHA
"""
c=0
n = int(input("Enter a Number"))
while(n!=0):
    n=n//10
    c+=1
print("Number of digits is",c)    
