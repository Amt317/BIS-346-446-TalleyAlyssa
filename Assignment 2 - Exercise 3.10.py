# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:21:52 2023

@author: hzcu
"""
P= 1000 # principal invested, $
R=0.07 # rate of return

for n in range(1,31):
    A=P*(1+R)**n
    print("In ", n ,"years, we should have $",round(A,2))
