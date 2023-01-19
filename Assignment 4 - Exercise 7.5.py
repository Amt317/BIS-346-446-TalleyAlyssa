# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 06:37:46 2023

@author: hzcu
"""
import numpy as np

# 2x3 array with first six powers of 2 beginning with 2^0

array1=np.array([2**i for i in range(0,6)]).reshape(2,3)
print(array1)  

# flatten array with "flatten"
print(array1.flatten())
# ravel
print(array1.ravel())
# show unmodified original array
print(array1)
