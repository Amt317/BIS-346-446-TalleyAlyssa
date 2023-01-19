# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 08:55:54 2023

@author: hzcu
"""

import random
import numpy as np

values=[1,10,100,1000,10000,100000,1000000]
listEtime=[]
arrayEtime=[]

for i in range(0,7):
    print(f'Loop: {i}           Number of Values: {values[i]:,}')
    time_temp = %timeit -o rolls_list = [random.randrange(1,7) for i in range(0,values[i])]
    listEtime.append(time_temp.average)
    time_temp = %timeit -o rolls_array = np.random.randint(1,7,values[i])
    arrayEtime.append(time_temp.average)

   
print(f'Number        List average     array average')
print(f'of values     execution time   execution time')

for i in range (0,7):
    print(f'{values[i]:>9,}       {listEtime[i]:.8f}       {arrayEtime[i]:.8f}') 
