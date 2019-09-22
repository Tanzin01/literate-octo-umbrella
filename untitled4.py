#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:09:13 2019

@author: tanzin
"""
from goto import goto, label
import random
secretNumber = random.randint(0,20)
print("I am thinking of a number between 1 and 20.!")


print("Take a guess")
guessnumber= int(input())


label .again
if guessnumber > secretNumber:
    print("Too hight")
elif guessnumber < secretNumber:
    print("Too low")
else:
    pass
if guessnumber == secretNumber:
    print("Horrayy, you are ccorrect")
    
else:
    print("The number i was thinking " + str(secretNumber) )

print("To play again enter 1 or to exit enter 2")
input = int(input())
if input == 1:
    goto  .again
else:
    pass

    
