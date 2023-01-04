# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 11:04:11 2023

@author: hzcu
"""


passes = 0  # number of passes
failures = 0 # of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while result != 1 and result != 2:  
        print('Incorrect result entered.')
        result = int(input('Enter result (1=pass, 2=fail): '))
        
    if result == 1:
        passes = passes + 1
    if result == 2:
        failures=failures+1 

print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')
    