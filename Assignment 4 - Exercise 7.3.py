# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:00:03 2023

@author: hzcu
"""
import numpy as np


# 3x3 array with even integers 2 to 18

array1=np.arange(2,19,2).reshape(3,3)
print(array1)

# 3x3 array with integers 9 to 1

array2=np.arange(9,0,-1).reshape(3,3)
print(array2)

# multiply first array by second

array3=array1*array2
print(array3)
