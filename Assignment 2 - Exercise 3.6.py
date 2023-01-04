# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 11:30:10 2023

@author: hzcu
"""
input("What is your problem?")
response=input("Have you had this problem before (yes or no)?")
if response=='yes':
        print("Well, you have it again.")
if response=='no':
    print("Well, you have it now.")

# This would not exhibit inteligent behavior because the responses are very limited and only related to the yes/no answer, not the original question. 
# Additionally, further questions would show that the computer wasn't programmed for more complex dialog.