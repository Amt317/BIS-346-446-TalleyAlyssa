# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:35:27 2023

@author: hzcu
"""



print("Celsius \t \t \t Fahrenheit")

for count in range(1,101):
    C=count
    F=(9/5)*C+32 # Celcius Conversion to Fahrenheit
    
    print(C," \t \t \t \t ","{:10.1f}".format(F))


