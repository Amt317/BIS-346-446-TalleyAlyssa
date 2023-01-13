# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:14:22 2023

@author: hzcu
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters=[]
    frequencies=[]
    
    for i in string.lower(): # lower case string
        if i in alphabet:
            if i in letters:
                index=letters.index(i)
                frequencies[index]+=1
            else:
                letters.append(i)
                frequencies.append(1)

    tuples=list(zip(letters,frequencies))
    tuples.sort()
    return tuples


teststring=input("Input Test String. ")
j=summarize_letters(teststring)

for k, count in j:
    print(f'{k}:{count}')

every = True
if len(j) == len(alphabet):
        for item in j:
            if item[0] not in alphabet:
                every = False
                break
else:
        every = False
    
if every:
        print("All letters are present.")
else:
        print("All letters are not present.")
