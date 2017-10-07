#Yahtzee.py
#
#This game is Yatzee

import random
from statistics import mode

def Roll(): # returns a random number between 1 and 6
     return random.randint(1, 6)

def FirstRoll(): # rolls first 5 dice to begin turn, returns list of 5 integers
    rolled_dice = []  # place holder for dice
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
    return original_dice

def OneTurn(): # one players turn, rolls dice up to 3 times
    x = FirstRoll()
    y = RollAgain()
    if y != ['done_rolling']:
        z = NextRoll(x, y)
        y = RollAgain()
        if y != ['done_rolling']:
            return NextRoll(x, y)
        else: return z
    else: return x

def PrintScorecard():
    print()
    print(" --------------------------------------------------------------------")
    print("|   UPPER SECTION    HOW TO SCORE                Player 1    Player 2|")
    print("| 1 Aces             Count and Add Only Aces       %s          %s  |" % (r1[1], r1[3]))
    print("| 2 Twos             Count and Add Only Twos       %s          %s  |" % (r2[1], r2[3]))
    print("| 3 Threes           Count and Add Only Threes     %s          %s  |" % (r3[1], r3[3]))
    print("| 4 Fours            Count and Add Only Fours      %s          %s  |" % (r4[1], r4[3]))
    print("| 5 Fives            Count and Add Only Fives      %s          %s  |" % (r5[1], r5[3]))
    print("| 6 Sixes            Count and Add Only Sixes      %s          %s  |" % (r6[1], r6[3]))
    print("|   TOTAL SCORE      ------------------------>     %s          %s  |" % (r16[1], r16[3]))
    print("|   BONUS (if score > 63)            SCORE 35      %s          %s  |" % (r17[1], r17[3]))
    print("|   TOTAL of Upper Section   ---------------->     %s          %s  |" % (r18[1], r18[3]))
    print("|   LOWER SECTION    ------------------------------------------------|")
    print("| 7 3 of a kind      Add Total Of All Dice         %s          %s  |" % (r7[1], r7[3]))
    print("| 8 4 of a king      Add Total Of All Dice         %s          %s  |" % (r8[1], r8[3]))
    print("| 9 Full House                       SCORE 25      %s          %s  |" % (r9[1], r9[3]))
    print("|10 Sm Straight (seq of 4)           SCORE 30      %s          %s  |" % (r10[1], r10[3]))
    print("|11 Lg Straight (seq of 5)           SCORE 40      %s          %s  |" % (r11[1], r11[3]))
    print("|12 YAHTZEE     (5 of a kind)        SCORE 50      %s          %s  |" % (r12[1], r12[3]))
    print("|13 Chance           Score Total Of All 5 Dice     %s          %s  |" % (r13[1], r13[3]))
    print("|   YAHTZEE          X for each bonus              %s          %s  |" % (r14[1], r14[3]))
    print("|    BONUS           Score 100 per X               %s          %s  |" % (r15[1], r15[3]))
    print("|   TOTAL of Lower Section------------------->     %s          %s  |" % (r19[1], r19[3]))
    print("|   TOTAL of Upper Section ------------------>     %s          %s  |" % (r18[1], r18[3]))
    print("|   GRAND TOTAL ----------------------------->     %s          %s  |" % (r20[1], r20[3]))
    print(" --------------------------------------------------------------------")

# [P1 score(int), P1 score(str), P2 score(int), P2 score(str)]
r1 = [0, "   ", 0, "   "]
r2 = [0, "   ", 0, "   "]
r3 = [0, "   ", 0, "   "]
r4 = [0, "   ", 0, "   "]
r5 = [0, "   ", 0, "   ",]
r6 = [0, "   ", 0, "   ",]
r7 = [0, "   ", 0, "   ",]
r8 = [0, "   ", 0, "   ",]
r9 = [0, "   ", 0, "   ",]
r10 = [0, "   ", 0, "   ",]
r11 = [0, "   ", 0, "   ",]
r12 = [0, "   ", 0, "   ",]
r13 = [0, "   ", 0, "   ",]
r14 = ["", "   ", "", "   ",]
r15 = [0, "   ", 0, "   ",]
r16 = [0, "   ", 0, "   ",]
r17 = [0, "   ", 0, "   ",]
r18 = [0, "   ", 0, "   ",]
r19 = [0, "   ", 0, "   ",]
r20 = [0, "   ", 0, "   ",]

#determines if player 1 has already scored the category TODO player 2 scoring determination
p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def markScorecard(dice):
    print()
    print()
    PrintScorecard()
    print()
    print("You rolled: " + str(dice))
    check = False
    while check == False:
        row = int(input("\nWhich row are you scoring? "))
        if (row > 0 and row < 14):
            if p1[row - 1] == 0:
                check = True
                p1[row - 1] = 1
            else: print("You already scored row %i" % row)
        else: print("Enter a value between 1 and 13")
    sum = 0

    # Scoring Selections

    # Select 1 - ones
    if row == 1:
        for d in dice:
            if d == row:
                sum += d
        r1[0] = sum
        r1[1] = str(r1[0]).rjust(3, " ")

    # Select 2 - twos
    if row == 2:
        for d in dice:
            if d == row:
                sum += d
        r2[0] = sum
        r2[1] = str(r2[0]).rjust(3, " ")

    # Select 3 - threes
    if row == 3:
        for d in dice:
            if d == row:
                sum += d
        r3[0] = sum
        r3[1] = str(r3[0]).rjust(3, " ")

    # Select 4 - fours
    if row == 4:
        for d in dice:
            if d == row:
                sum += d
        r4[0] = sum
        r4[1] = str(r4[0]).rjust(3, " ")

    # Select 5 - fives
    if row == 5:
        for d in dice:
            if d == row:
                sum += d
        r5[0] = sum
        r5[1] = str(r5[0]).rjust(3, " ")

    # Select 6 - sixes
    if row == 6:
        for d in dice:
            if d == row:
                sum += d
        r6[0] = sum
        r6[1] = str(r6[0]).rjust(3, " ")

    # Select 7 - Three of a kind
    if row == 7:
        for d in dice:
            if d == mode(dice):
                sum += d
        if sum/mode(dice) >= 3:
            r7[0] = sum
            r7[1] = str(r7[0]).rjust(3, " ")

    # Select 8 - Four of a kind
    if row == 8:
        for d in dice:
            if d == mode(dice):
                sum += d
        if sum/mode(dice) >= 4:
            r8[0] = sum
            r8[1] = str(r8[0]).rjust(3, " ")

    # Select 9 - Full House
    if row == 9:
        if ((dice[0] == dice[1] == dice[2] and dice[3] == dice[4]) or (dice[0] == dice[1] and dice[2] == dice[3] == dice[4])):
            r9[0] = 25
        else: r9[0] = 0
        r9[1] = str(r9[0]).rjust(3, " ")

    # Select 10 - Small Straight (4 in a row)
    if row == 10:
        counter = 0
        for n in range(4):
            if (dice[n] == dice[n+1]-1):
                counter += 1
        if counter >= 3: r10[0] = 30
        else: r10[0] = 0
        r10[1] = str(r10[0]).rjust(3, " ")

    if row == 11:
        if(dice[0] == (dice[1]-1) == (dice[2]-2) == (dice[3]-3) == (dice[4]-4)):
            r11[0] = 40
        else: r11[0] = 0
        r11[1] = str(r11[0]).rjust(3, " ")

    # Select 12 - Yahtzee!
    if row == 12:
        if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
            r12[0] = 50
        else: r12[0] = 0
        r12[1] = str(r12[0]).rjust(3, " ")

    # Select 13 - Chance
    if row == 13:
        for d in dice:
            sum += d
        r13[0] = sum
        r13[1] = str(r13[0]).rjust(3, " ")

def updateScorecard():
    #updates sums and upper section bonus for player 1
    r16[0] = r1[0] + r2[0] + r3[0] + r4[0] + r5[0] + r6[0]
    r16[1] = str(r16[0]).rjust(3, " ")
    if r16[0] > 63:
        r17[0] = 35
        r17[1] = str(r17[0]).rjust(3, " ")
    r18[0] = r16[0] + r17[0]
    r18[1] = str(r18[0]).rjust(3, " ")
    r19[0] = r7[0] + r8[0] + r9[0] + r10[0] + r11[0] + r12[0] + r13[0] + r15[0]
    r19[1] = str(r19[0]).rjust(3, " ")
    r20[0] = r18[0] + r19[0]
    r20[1] = str(r20[0]).rjust(3, " ")
    #TODO update sums for player 2

    PrintScorecard()

print("We're playing 1 player for now..")
PrintScorecard()
for s in range(13):
    markScorecard(OneTurn())
    updateScorecard()