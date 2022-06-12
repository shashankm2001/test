# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:07:06 2022

@author: SMITHA
""" 
list1=[] 
n=int(input("Enter the Number of elements")) 

for i in range(1,n+1):
    ele=int(input("Enter the element"))
    list1.append(ele)
max1=list1[0]
for i in range(1,n):
    if list1[i]>= max1:
        max1=list1[i]
print(" Maximum Element is ",max1)
    
        
  
  