# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:54:40 2023

@author: hzcu
"""

def display_table(rows,width):
    
    indent = len(str(len(rows)))
    print(f'{"":{indent}}', end='')

    for col in range(len(rows[0])):
        print(f'{col:>{width}}', end='')

    print()

    for i, row in enumerate(rows):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{width}}', end='')

        print()
          
lists = [list('abcdef'), 
          list('ghijkl'), 
          list('mnopqr'), 
          list('stuvwx')]

display_table(lists, 3)