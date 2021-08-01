from random import shuffle
from os import system, name
from time import sleep
from typing import Counter

def clear():
    # Windows
    if name == 'nt':
        system('cls')
    
    # for Mac and Linux
    else:
        system('clear')

cardsDict = {
    '2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten',
    'J':'Jack','Q':'Queen','K':'King','A':'Ace'
}

class FishTank:
    def __init__(self):
        self.deck = list('23456789JQKA'*4)
        for _ in range(4):      #_ is name for unused var and Python wont give any warning
            self.deck.append('10')
        self.remainingCards = len(self.deck)

    def shuffleCards(self):
        shuffle(self.deck)
    
    def getCard(self):
        try:
            card = self.deck[-1]
            self.deck.pop()
            return card
        except IndexError:
            return '-1'

class Player():
    def __init__(self, name, cards = []):
        self.name = name
        self.cards = cards
        self.score = set({})
    
    def amIlying(self,card):
        if card in self.cards:
            return True
        else:
            return False

    """
    Two cases for giving 5 cards:
    1.    Because another player gave to current player certain number of Cards and he has no more cards 

    2.    Because player got 4 of kind and there is no more left 
    """
    def giveFiveCardsToPlayer(self,fishTank):
        if len(self.cards) == 0:
            print(self.name,'got',0,'cards')
            for counter in range(5):
                card = fishTank.getCard()
                if card != '-1':
                    self.cards.append(card)
                else:
                    break
            if counter > 0: 
                print()     
                print(self.name,'got',counter + 1,'cards out fish tank')
                print()
                sleep(2)
                clear()
            else:
                print('Fish tank is empty, can not get more cards')



    def messagePlayer(self, message, card, players, fishTank):
        doICheat = True
        numOfCards = 0
        showCards(self,players)
        while doICheat == True:
            answer = input(message)
            if answer == 'y':
                while card in self.cards:
                    self.cards.remove(card)
                    numOfCards += 1
                clear()
                self.giveFiveCardsToPlayer(fishTank)
                return numOfCards
            else:
                doICheat = self.amIlying(card)
                if doICheat:
                    print('\nYou have',cardsDict[card],"('s)")
                    print('Play fair!\n')
                    sleep(2)
                else:
                    clear()
                    return numOfCards

    def fourOfKind(self,card, fishTank):
        counter = 0
        for temp_card in self.cards:
            if temp_card == card:
                counter += 1
        
        if counter >= 4:
            self.score.add(card)
            for _ in range(counter):
                for temp_card in self.cards:
                    if temp_card == card:
                        self.cards.remove(temp_card)
            self.giveFiveCardsToPlayer(fishTank)

   
    def drawCard(self, card, fishTank):
        drawnCard = fishTank.getCard()
        self.cards.append(drawnCard)

        if card == drawnCard:
            self.fourOfKind(card, fishTank)

    def askPlayerForCard(self, player, card, players, fishTank):
        if self.name != player.name:
            if card in self.cards:
                message = player.name + ", do you have " + cardsDict[card] + "'s?"
                message += '\nYes - y, No - n: '
                clear()
                numOfCards = player.messagePlayer(message, card, players, fishTank) #player who is also class Player will get this message
                if numOfCards > 0:
                    for _ in range(numOfCards):
                        self.cards.append(card) 
                    print("You got",numOfCards,cardsDict[card],"'s")
                    self.fourOfKind(card, fishTank)
                    return False
                else:
                    print('Go Fish')
                    while True:
                        txt = input('Press "d" to draw one card from the top of the deck: ').lower()
                        if(txt == "d"):
                            self.drawCard(card,fishTank)
                            return True #end turn
                        else:
                            print('Wrong input! Please try again.')
            else:
                print('\nYou can not ask for a card you do not own!\n')
        else:
            print('\nYou can not ask yourself for card ;D!\n')

""""
player1 = Player('Nick',['2','2','5'])
player2 = Player('John',['3','3','5'])
fishTank1 = FishTank()
print(fishTank1)
player1.askPlayerForCard(player2,player1.cards[2],fishTank1)
print(player1.cards)
print(player2.cards)

player1 = Player('Nick',['2','2','6','2','2'])
player1.fourOfKind('2')
print(player1.cards)
print(player1.score)
"""

def whoPlayes(players):
    while True:
        print('Who will play first?')
        whoPlayes = input('Enter your name: ').upper()

        i = 0
        for player in players:
            if player.name.upper() == whoPlayes:
                return i
            i += 1
        
        print('Player with name',whoPlayes,'does not exist')

def showCurrentScores(player):
    scoreLen = len(player.score)
    if scoreLen != 0:
        for score in player.score:
            print("Four",cardsDict[score] + "'s ",end='')
        print()
    print('In total:',scoreLen,'points\n')

def showCards(currentPlayer, players):
    for player in players:
        print(player.name,': ',end='')
        for card in player.cards:
            if player.name != currentPlayer.name:
                print('X ',end='')
            else:
                print(cardsDict[card]+' ',end='')
        print()
        showCurrentScores(player)
    print()

def findPlayer(players):
    while True:
        name = input('Enter player name from whom you want the card: ').upper()

        i = 0
        for player in players:
            if player.name.upper() == name:
                return i
            i += 1
        
        print('Player with name',name,'does not exist')

def findCard():
    while True:
        cardName = input('Enter card name you want: ').upper()

        for card in cardsDict:
            if cardsDict[card].upper() == cardName:
                return card
        
        print('Card with name',cardName,'does not exist')
    
def play(playerNum,players,fishTank):
    currentPlayer = players[playerNum]
    #check if alreay player has 4 of kinds
    for card in currentPlayer.cards:
        currentPlayer.fourOfKind(card, fishTank)
    
    finishMyTurn = False
    while finishMyTurn == False:
        showCards(currentPlayer,players)
        print(currentPlayer.name,", it's your turn!",sep='')
            
        num = findPlayer(players)
        card = findCard()

        #askPlayerForCard() func finishes when to current player is said Go Fish
        finishMyTurn = currentPlayer.askPlayerForCard(players[num],card,players,fishTank)
    

def playersHaveCards(players):
    for player in players:
        if len(player.cards) > 0:
            return True
    return False

def gameOver(players):
    print('Game is over!')
    scoreDict = {}
    
    for player in players:
        scoreDict[player.name] = len(player.score)
    
    max = 0
    winner = ''
    for name in scoreDict:
        if scoreDict[name] > 0:
            max = scoreDict[name]
            winner = name
    
    print('Winner is',winner,'who scored',max,'points')


def main():
    fishTank = FishTank()
    fishTank.shuffleCards()

    while True:
        num_of_players = int(input('Enter num of players: '))
        if num_of_players < 2 or num_of_players > 4:
            print('Only 2 or 3 or 4 players can participate!')
        else:
            break
    clear()      

    players = []
    """
    Real func
    for i in range(num_of_players):
        name = input("Enter player's "+ str(i+1) + " name: ")
        cards = []
        print('Giving 5 cards to player', name ,"...")
        for _ in range(5):
            cards.append(fishTank.getCard())
        sleep(1)
        print('Player', name ," has its own 5 cards")
        players.append(Player(name,cards))
    """
    #cheat
    
    players.append(Player('John',[]))
    players.append(Player('Nick',[]))

    firstPlayerNum = whoPlayes(players)
    while playersHaveCards(players):
        clear()
        play(firstPlayerNum,players,fishTank)
        firstPlayerNum += 1
        firstPlayerNum = firstPlayerNum % 2

    players[0].score = {'2','3'}
    gameOver(players)
    """
    add help function :)
    """
main()
    
