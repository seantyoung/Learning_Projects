#Roll the Dice.py
#
#This program will roll dice for you. You choose how many dice and how many sides are on each dice.

import random
repeat = True
same = 'n'

while repeat is True:
    while same == 'n':
        rolls = int(input("How many dice would you like to roll? "))
        sides = int(input("How many sides are on each dice? "))
        same = 'reset'

    print("Dice #   Roll")

    for r in range(rolls):
        roll = random.randint(1,sides)
        print("%i        %i " % ((r+1), roll))

    same = 'reset'
    while not (same == 'y' or same == 'n'):
        same = input("Would you like to roll the same dice again? (y or n) ").lower()
        if same == 'n':
            repeat = input("Would you like to roll a new set of dice? (y or n) ")
            if repeat == 'n':
                repeat = False
            else:
                repeat = True
