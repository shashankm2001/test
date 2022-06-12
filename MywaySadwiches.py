# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:05:40 2022

@author: SMITHA
"""

print(" Welcome to Myway Sandwitches")
print(" 1: Onion 2: Lettuce 3:Tomato 4:Olives 5:Pepper 6: Tomatoes")
print(" Enter your option. Please select only 3 and seperte by commas")
opt=[int(x) for x in input().split(',')]
a = int(input("Enter the  Number of Sandwitches  you want"))
price = a*5
print(" Pay %d Dollars and Enjoy your Sandwitches\nThankyou.Visit again"%price)



     
