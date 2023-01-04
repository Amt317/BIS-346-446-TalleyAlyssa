# -*- coding: utf-8 -*-




import random
tortoise=1 # starting position
hare=1 # starting position
EndRace=70 # winning position
time=0 # starting time (seconds)

print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

while hare < EndRace and tortoise < EndRace: # defines how long to keep running through below logic
    
    i=random.randrange(1,11)
    if i >= 5:
        tortoise = tortoise + 3
    if 6 <= i <= 7:
        if tortoise <= 6:
            tortoise= 1
        else:
            tortoise = tortoise - 6
    if tortoise >=8:
        tortoise = tortoise + 1

    j = random.randrange(1,11)
    if j <=2:
        hare = hare 
    if 3 <= j <= 4:
        hare = hare + 9
    if j == 5:  
        if hare <= 12:
            hare= 1
        else:
            hare = hare - 12
    if 6 <= j <= 8:
        hare = hare + 1
    if 9 <= j <= 10:
        if hare <= 2:
            hare= 1
        else:
            hare = hare - 2
    time=time+1  
    
    if tortoise > 70:
        tortoise = 70
    if hare > 70:
        hare = 70
    
# logic to print tortoise and hare positions each second
    for space in range(1, EndRace+2 ):
        if space == tortoise and space == hare:
            print('OUCH!!!', end='')
        elif space == hare:
            print('H', end='')
        elif space == tortoise:
            print('T', end='')
        else:
            print(' ', end='')
        
    print()

if tortoise > hare:
    print("TORTOISE WINS!!! YAY!!!")
if hare > tortoise:
    print("Hare wins. Yuch.")
if hare == tortoise:
    print("It's a tie.")

print("TIME ELAPSED:", time,"seconds")