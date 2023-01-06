# -*- coding: utf-8 -*-
#Alyssa Talley
#1/6/2023
#part 1
xPound=0.84 # British pound exchange rate per $1 US
xEuro=0.95 # Euro exchange rate per $1 US
xCanada=1.36 # Canadian dollar exchange rate per $1 US

def conversion(dollars):
       x=int(dollars)
       Pound=x*xPound
       Euro=x*xEuro
       Canada=x*xCanada 
       print("You can exchange to","{:.2f}".format(Pound),"British pounds,","{:.2f}".format(Euro),"Euros, or", "{:.2f}".format(Canada),"Canadian Dollars.")

#part 2

i=input("How many US dollars would you like to convert? Type number with no units or commas.  ")
conversion(i)




