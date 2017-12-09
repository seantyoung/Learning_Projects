#Blackjack.py
#
#This game is Blackjack

from random import shuffle
global deck
global playerHand
global dealerHand
global card
wins = 0
pushes = 0
losses = 0

def shuffleDeck():
    quarterDeck = [
    ['A', 11],
    ['2', 2],
    ['3', 3],
    ['4', 4],
    ['5', 5],
    ['6', 6],
    ['7', 7],
    ['8', 8],
    ['9', 9],
    ['10', 10],
    ['J', 10],
    ['Q', 10],
    ['K', 10],
]
    oneDeck = quarterDeck + quarterDeck + quarterDeck + quarterDeck
    Deck = oneDeck + oneDeck + oneDeck + oneDeck + oneDeck + oneDeck + oneDeck + oneDeck
    shuffle(Deck)
    return Deck

def Deal(card, stand):
    for i in range(2):
        playerHand.append(card)
        card += 1
        dealerHand.append(card)
        card += 1
    return card

def ShowCards():
    printdealer = "Dealer Hand: "
    for i in range(len(dealerHand)):
        printdealer += "["
        if i == 0 and stand == False: printdealer += " "
        else: printdealer += Deck[dealerHand[i]][0]
        printdealer += "] "
    printplayer = "Player Hand: "
    for i in playerHand:
        printplayer += "["
        printplayer += Deck[i][0]
        printplayer += "] "

    print(printdealer)
    print(printplayer)

def CalcScores():
    dealerPoints = 0
    playerPoints = 0
    for i in range(len(dealerHand)):
        dealerPoints += Deck[dealerHand[i]][1]
    for i in range(len(playerHand)):
        playerPoints += Deck[playerHand[i]][1]
    return dealerPoints, playerPoints


Deck = shuffleDeck()
card = 0 # keeps track of what card we're at in the decks

while True:
    if card > 400:
        shuffleDeck()
        card = 0
    playerHand = []
    dealerHand = []
    stand = False

    #initial deal of cards
    card = Deal(card, stand)
    ShowCards()
    dealerPoints, playerPoints = CalcScores()
    if playerPoints == 21: #determines if player gets blackjack
        print()
        print("Blackjack!")
        print()
        stand = True
    elif dealerPoints == 21:  # determines if dealer gets blackjack
        print()
        print("Dealer blackjack!")
        print()
        stand = True

    while stand == False:
        response = input('Enter "s" to stand or "h" to hit\n').lower()
        if response == "s":
            stand = True
        elif response == "h":
            playerHand.append(card)
            card += 1
            stand = False
            ShowCards()
        dealerPoints, playerPoints = CalcScores()
        if playerPoints > 21:
            Aces = 0
            for i in range(len(playerHand)):
                if Deck[playerHand[i]][1] == 11:
                    Aces += 1
            while Aces > 0 and playerPoints > 21:
                playerPoints -= 10
                Aces -= 1
        if playerPoints > 21:
            print()
            print("You broke")
            print()
            stand = True

    ShowCards()
    dealerDone = False

    if dealerPoints > 17: dealerDone = True #if dealer has 18+ points, done dealing
    elif dealerPoints == 17: #if dealer gets hard 17, done dealing
        for i in range(len(dealerHand)):
            if Deck[dealerHand[i]][1] == 11:
                dealerDone = True

    while dealerDone == False:
        dealerHand.append(card)
        card += 1
        dealerPoints, x = CalcScores()
        if dealerPoints > 21:
            Aces = 0
            for i in range(len(dealerHand)):
                if Deck[dealerHand[i]][1] == 11:
                    Aces += 1
            while Aces > 0 and dealerPoints > 21:
                dealerPoints -= 10
                Aces -= 1
        if dealerPoints > 21:
            dealerDone = True
        elif dealerPoints > 16: dealerDone = True
    print()
    ShowCards()
    print()
    if playerPoints > 21:
        print("You lose!")
        losses += 1
    elif dealerPoints > 21:
        print("You win!")
        wins += 1
    elif dealerPoints > playerPoints:
        print("You lose! womp womp")
        losses += 1
    elif dealerPoints < playerPoints:
        print("You win!")
        wins += 1
    else:
        print("Push")
        pushes += 1

    print("Dealer/Player  wins/pushes/losses")
    print(" ", dealerPoints, "/ ", playerPoints, "    ",wins, " / ",pushes, " / ",losses)

    print()
    endgame = input("Press x to exit or any other key to continue...\n")
    if endgame == 'x': break


#todo add ability to split hands
#todo add betting
#todo add insurance
#todo improve GUI