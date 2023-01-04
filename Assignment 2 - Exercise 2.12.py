# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:21:52 2023

@author: hzcu
"""
P= 1000 # principal invested, $
R=0.07 # rate of return
n=10 # number of years
A=P*(1+R)**n
B=int(A) # make A an integer
print("In ", n ,"years, we should have $",B)
n=20 # number of years
A=P*(1+R)**n
B=int(A)  # make A an integer
print("In ", n ,"years, we should have $",B)
n=30 # number of years
A=P*(1+R)**n
B=int(A)  # make A an integer
print("In ", n ,"years, we should have $",B)


