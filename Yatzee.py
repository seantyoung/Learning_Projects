#Yatzee.py
#
#This game is Yatzee

import random
import numpy
import time

def Roll():

    roll = []

    for r in range(5):
        roll.append(random.randint(1, 6))

    return roll[0], roll[1], roll[2], roll[3], roll[4]

print(Roll())