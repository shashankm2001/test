# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:14:31 2022

@author: SMITHA
"""

tup =(1,)
print(type(tup))
tup=(1,2,3,4,5)
print(len(tup))
lst=[1,2,3,4,5]
print(type(lst))
tup1=tuple(lst)
print(tup1)
days=('mon','tues','wed','thurs','fri','sat','sun')
for day in days:
    print(day,end =" ")
 
print() 
print( 'mon' in days) 
print(len(days)) 