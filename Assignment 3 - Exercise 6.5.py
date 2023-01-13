# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:42:47 2023

@author: hzcu
"""

sentence=input("Write a Sentence.  ")
words={}

for word in sentence.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

print(f'{"Word":<8} Count')

for word,count in sorted(words.items()):
        if count >1:
            print(f'{word:<10}{count}')
      
        
