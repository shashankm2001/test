# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:02:20 2022

@author: SMITHA
"""

def quicksort(a,lb,ub):
    if(lb<ub):
        i=lb
        j=ub
        pivot=a[lb]  
        while(i<j):
            while(i<ub and a[i]<=pivot):
                i+=1
            while(a[j]>=pivot and j>lb):
                j-=1
        if(i<j):
            temp=a[i]
            a[i]=a[j]
            a[j]= temp
        
        temp=a[lb]
        a[lb]=a[j]
        a[j]= temp
        quicksort(a,lb,j-1)
        quicksort(a,j+1,ub)
        
print("enter the elements")
a =[int (x) for x in input().split()]
    
high=len(a) 
print(high)
quicksort(a,0,high-1) 
print("Elements in sorted list is")
print(a) 
    