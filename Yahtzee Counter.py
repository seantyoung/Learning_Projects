#Roll the Dice.py
#
#This program will roll 5 6 sided dice until a yahtzee is rolled

import random
import numpy

Yatzees = 0
times = int(input("How many yahtzees would you like to roll? "))
yat = []
for t in range(times):
    Yatzee = False
    roll = []
    rolls = 0
    while Yatzee is False:
        rolls += 1
        for r in range(5):
            roll.append(random.randint(1, 6))
        if roll[0] == roll[1] == roll[2] == roll[3] == roll[4]:
            Yatzee = True
            #print("It took %i rolls to get a yahtzee!" % rolls)
            yat.append(rolls)
        else:
            roll = []


#print(yat)
print("Average number of rolls: %i" % int(numpy.mean(yat)))

