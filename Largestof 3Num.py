# -*- coding: utf-8 -*-
"""
Created on Tue May 24 06:56:58 2022

@author: SMITHA
"""

a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))
if(a>b):
    if(a>c):
        print(a ,"is greatest")
    else:
        print(c,"is greatest")
else:
    if(b>c):
        print(b ," is greatest")
    else:
        print(c,"is greatest")
        
    
    