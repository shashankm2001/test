# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:38:31 2022

@author: SMITHA
"""

set1={10,20,30,'xyz', 90,78,90,10,20 }

print(type(set1))
set1.update([12,45])
 
print(set1.remove(12))
print(set1)
f=frozenset(set1)
print(f)
#f.update([89,80])
#print(f)
#f.remove(89)
#print(f)
lst = [12,34,56,78]
b = bytes(lst)
print(type(b))
b1=bytearray(b)
print(b1)
b1[1]= 90
