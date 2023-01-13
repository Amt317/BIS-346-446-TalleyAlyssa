# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:02:12 2023

@author: hzcu
"""

invoice = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]

#a
from operator import itemgetter

for partID,description,quantity,price in sorted(invoice,key=itemgetter(0)):
    print(f'{partID:>2} {description:<16}{quantity:>3}{price:7.2f}')


#b
for partID,description,quantity,price in sorted(invoice,key=itemgetter(3)):
    print(f'{partID:>2} {description:<16}{quantity:>3}{price:7.2f}')
    
#c
quantitysort=[(description,quantity) for partID,description,quantity,price in invoice]

for description, quantity in sorted(quantitysort,key=itemgetter(1)):
    print(f'{description:<16}{quantity:>3}')
    
#d

pricesort=[(description,quantity*price) for partID, description, quantity, price in invoice]
for description, value in sorted(pricesort,key=itemgetter(1)):
    print(f'{description:<16}${value:9.2f}')

#e
pricesortE=[(description,quantity*price) for partID, description, quantity, price in invoice\
    if 200 <=quantity*price <= 500]
for description, value in sorted(pricesortE,key=itemgetter(1)):
    print(f'{description:<16}${value:9.2f}')
    
#f
total=sum([(quantity*price) for partID, description, quantity, price in invoice])
print(f'The Total is ${total:.2f}')
