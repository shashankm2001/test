# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 18:16:34 2022

@author: SMITHA
"""

dict1={1: "Ramya",2: "Deekshita",3 :"Gagana",4:"Fahad"}
print(dict1)
print(dict1.values())
print(dict1.keys())
k = dict1.keys()
for i in k: 
    print(i)
for i in dict1.values():
    print(i)
print(dict1)
k1=dict1.copy()
print(k1)
k2=dict1.items()
print(k2)
k9=dict1.clear()
print(k9)