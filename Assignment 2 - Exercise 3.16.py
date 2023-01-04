# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:20:08 2023

@author: hzcu
"""

a=0   
b=0
    
for count in range(10):
    # run for 10 counts
    number=int(input("Enter A Number: "))
    evaluateValue=number
    if evaluateValue>a:
        b=a
        a=evaluateValue
    else:
        if evaluateValue>b:
            b=evaluateValue
 
        
print('The Largest Number is ', a)
print('The Second Largest Number is ', b)
   