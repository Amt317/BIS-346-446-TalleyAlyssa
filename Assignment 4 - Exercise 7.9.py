# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 06:38:12 2023

@author: hzcu
"""
import numpy as np
# array integers 1 to 15 as 3x5 
array=np.arange(1,16).reshape(3,5)
print(array)

# a) select row 2
print(array[2])

# b) select column 4**
print(array[:,4])

# c) select rows 0 and 1
print(array[0:2,:])

# d) select columns 2-4
print(array[:,2:5])

# e) select element in row 1 column 4
print(array[1,4])

# f) select all elements in rows 1 and 2 that are in columns, 0,2, and 4
print(array[1:3,[0,2,4]])


