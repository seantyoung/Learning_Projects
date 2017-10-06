#Yahtzee.py
#
#This game is Yatzee

import random
import numpy
import time
rolled_dice = [] # place holder for dice

def Roll(): # returns a random number between 1 and 6
     return random.randint(1, 6)

def FirstRoll(): # rolls first 5 dice to begin turn, returns list of 5 integers
    for n in range(5):
        rolled_dice.append(Roll())
    rolled_dice.sort() # sorts dice in numerical order
    print("You rolled: " + str(rolled_dice) + "\n")
    return rolled_dice

def RollAgain(): # determines if player wants to roll again, then asks which dice to roll again
    reroll = 'not yet'
    while reroll == 'not yet': # ensures a correct response has been received
        ans = input("Would you like to roll again? ").lower()
        if ans == "no":
            reroll = False
            new_dice = ['done_rolling'] # used to bypass NextRoll
        elif ans == "yes": # asks which dice to replace, then subtracts 1 to convert to zero based lists
            print("\nWhich dice would you like to roll again?")
            print("(Enter the corresponding numbers separated by")
            reroll_dice = input(" spaces. 1 to 5 with 1 being the far left number)\n")
            valid = False
            while valid == False:
                new_dice = list(map(int, reroll_dice.split())) # converts string to integer list
                if (new_dice[0]>=1 and new_dice[-1]<=5): #ensures replacement locations are 1 to 5
                    valid = True
                else: # provides additional instruction if incorrect number was entered
                    reroll_dice = input("Enter number(s) 1 to 5 with 1 being the far left number and a space between each)\n")
            new_dice[:] = [x - 1 for x in new_dice] # subtracts 1 from each item in list to convert to zero based list
            reroll = True
        else: print('Answer "yes" or "no"')
    return new_dice

def NextRoll(original_dice, replace): # rolls and replaces dices selected in RollAgain, then resorts numerically
    print()
    for d in replace:
        original_dice[d] = Roll()
    original_dice.sort()
    print("You rolled: " + str(original_dice) + "\n")

def OneTurn(): # one players turn, rolls dice up to 3 times
    x = FirstRoll()
    y = RollAgain()
    if y != ['done_rolling']:
        NextRoll(x, y)
        y = RollAgain()
        if y != ['done_rolling']:
            NextRoll(x, y)

def PrintScoreCard():
    print("UPPER SECTION    HOW TO SCORE                Player 1    Player 2")
    print("Aces             Count and add only Aces       %s          %3s  " % (r1[1], r1[4]))
    print("Twos             Count and Add Only Twos       %3s          %3s  " % (r2[1], r2[4]))
    print("Threes           Count and Add Only Threes     %3s          %3s  " % (r3[1], r3[4]))
    print("Fours            Count and Add Only Fours      %3i          %3i  " % (r4[0], r4[1]))
    print("Fives            Count and Add Only Fives      %3i          %3i  " % (r5[0], r5[1]))
    print("Sixes            Count and Add Only Sixes      %3i          %3i  " % (r6[0], r6[1]))
    print("TOTAL SCORE      ------------------------>     %3i          %3i  " % (r16[0], r16[1]))
    print("BONUS (if score > 63)            SCORE 35      %3i          %3i  " % (r17[0], r17[1]))
    print("TOTAL of Upper Section   ---------------->     %3i          %3i  " % (r18[0], r18[1]))
    print("LOWER SECTION    ------------------------------------------------")
    print("3 of a kind      Add Total Of All Dice         %3i          %3i  " % (r7[0], r7[1]))
    print("4 of a king      Add Total Of All Dice         %3i          %3i  " % (r8[0], r8[1]))
    print("Full House                       SCORE 25      %3i          %3i  " % (r9[0], r9[1]))
    print("Sm Straight (seq of 4)           SCORE 30      %3i          %3i  " % (r10[0], r10[1]))
    print("Lg Straight (seq of 5)           SCORE 40      %3i          %3i  " % (r11[0], r11[1]))
    print("YAHTZEE     (5 of a kind)        SCORE 50      %3i          %3i  " % (r12[0], r12[1]))
    print("Chance           Score Total Of All 5 Dice     %3i          %3i  " % (r13[0], r13[1]))
    print("YAHTZEE          X for each bonus               %s           %s  " % (r14[0], r14[1]))
    print(" BONUS           Score 100 per X               %3i          %3i  " % (r15[0], r15[1]))
    print("TOTAL of Lower Section------------------->     %3i          %3i  " % (r19[0], r19[1]))
    print("TOTAL of Upper Section ------------------>     %3i          %3i  " % (r18[0], r18[1]))
    print("GRAND TOTAL ----------------------------->     %3i          %3i  " % (r20[0], r20[1]))

# TODO add in additional elements to identify when each box has been used
# TODO create a second table to display strings in the scorecard instead of ints for better imagining, could be in same array
# P1 score(int), P1 score(str), P1 used, P2 score(int), P2 score(str), P2 used
r1 = [0, "", 0, 0, "", 0]
r2 = [1, "1", 1, 0, "", 0]
r3 = [0, "", 0, 99, "99", 1]
r4 = [0, 0]
r5 = [0, 0]
r6 = [0, 0]
r7 = [0, 0]
r8 = [0, 0]
r9 = [0, 0]
r10 = [0, 0]
r11 = [0, 0]
r12 = [0, 0]
r13 = [0, 0]
r14 = ["", ""]
r15 = [0, 0]
r16 = [0, 0]
r17 = [0, 0]
r18 = [0, 0]
r19 = [0, 0]
r20 = [0, 0]

PrintScoreCard()
