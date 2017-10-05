#Yatzee.py
#
#This game is Yatzee

# TODO add comments on all code

import random
import numpy
import time

def Roll():
     return random.randint(1, 6)

rolled_dice = []

def FirstRoll():
    for n in range(5):
        rolled_dice.append(Roll())
    rolled_dice.sort()
    print("You rolled: " + str(rolled_dice) + "\n")
    return rolled_dice

def NextRoll(original_dice, replace):
    print()
    for d in replace:
        original_dice[d] = Roll()
    original_dice.sort()
    print("You rolled: " + str(original_dice) + "\n")

def RollAgain():
    reroll = 'not yet'
    while reroll == 'not yet':
        ans = input("Would you like to roll again? ").lower()
        if ans == "no":
            reroll = False
            new_dice = []
        elif ans == "yes":
            print("\nWhich dice would you like to roll again?")
            print("(Enter the corresponding numbers separated by")
            reroll_dice = input(" spaces. 1 to 5 with 1 being the far left number)\n")

            new_dice = list(map(int, reroll_dice.split()))
            new_dice[:] = [x - 1 for x in new_dice]
            reroll = True

        else: print('Answer "yes" or "no"')
    return new_dice

x = FirstRoll()
y = RollAgain()
NextRoll(x, y)
y = RollAgain()
NextRoll(x, y)