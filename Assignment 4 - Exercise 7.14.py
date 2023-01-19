# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 08:46:44 2023

@author: hzcu
"""
import numpy as np

array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])


# part a
array3=np.vstack((array1,array2))
print(array3)

# part b
array4=np.hstack((array1,array2))
print(array4)

# part c
array5=np.vstack((array4,array4))
print(array5)

# part d
array6=np.hstack((array3,array3))
print(array6)

