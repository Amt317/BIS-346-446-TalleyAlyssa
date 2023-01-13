# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:13:26 2023

@author: hzcu
"""

import numpy as np
import statistics as stats

ratings=[1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values,counts=np.unique(ratings,return_counts=True)
values=list(values)
counts=list(counts)
print('Ratings Responses')
for i, count in zip(values,counts):
    print(f'{i}:       {count}')

#min,max,range,mean,median,mode,variance,standard deviation

print('Statistics')
print(f'Minimum: {values[counts.index(min(counts))]}')
print(f'Maximum: {values[counts.index(max(counts))]}')
print(f'Range: {min(counts)} to {max(counts)}')   
print(f'Mean: {stats.mean(counts)}')
print(f'Median: {stats.median(counts)}')   
print(f'Mode: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard Deviation: {stats.pstdev(counts)}')


