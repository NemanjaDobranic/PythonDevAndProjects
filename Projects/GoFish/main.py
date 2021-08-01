from random import shuffle
from os import system, name
from time import sleep

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
        card = self.deck[-1]
        self.deck.pop()
        return card

class Player():
    def __init__(self, name, cards = []):
        self.name = name
        self.cards = cards
        self.score = 0
    
    def amIlying(self,card):
        if card in self.cards:
            return True
        else:
            return False


    def messagePlayer(self, message, card):
        doICheat = True
        numOfCards = 0

        while doICheat == True:
            answer = input(message)
            if answer == 'y':
                while card in self.cards:
                    self.cards.remove(card)
                    numOfCards += 1
                clear()
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

    def drawCard(self, card, fishTank):
        drawnCard = fishTank.getCard()
        self.cards.append(drawnCard)

    def askPlayerForCard(self, player, card, fishTank):
        if self.name != player.name:
            if card in self.cards:
                message = player.name + ", do you have " + cardsDict[card] + "'s?"
                message += '\nYes - y, No - n: '
                clear()
                numOfCards = player.messagePlayer(message, card) #player who is also class Player will get this message
                if numOfCards > 0:
                    for _ in range(numOfCards):
                        self.cards.append(card) 
                    print("You got",numOfCards,cardsDict[card],"'s")
                    #CHECK IF WIN func!!! self.check.....
                else:
                    print('Go Fish')
                    while True:
                        txt = input('Press "d" to draw one card from the top of the deck: ')
                        if(txt == "d"):
                            self.drawCard(card,fishTank)
                            return 
                        else:
                            print('Wrong input! Please try again.')
            else:
                print('You can not ask for a card you do not own!')
        else:
            print('You can not ask yourself for card ;D!')

""""
player1 = Player('Nick',['2','2','5'])
player2 = Player('John',['3','3','5'])
fishTank1 = FishTank()
print(fishTank1)
player1.askPlayerForCard(player2,player1.cards[2],fishTank1)
print(player1.cards)
print(player2.cards)
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

def showCards(currentPlayer, players):
    for player in players:
        print(player.name,': ',end='')
        for card in player.cards:
            if player.name != currentPlayer.name:
                print('X ',end='')
            else:
                print(cardsDict[card]+' ',end='')
        print()

def play(playerNum,players,fishTank):
    #while True:
    currentPlayer = players[playerNum]
    showCards(currentPlayer,players)
    print(currentPlayer.name,", it's your turn!",sep='')
    

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
    for i in range(num_of_players):
        name = input("Enter player's "+ str(i+1) + " name: ")
        cards = []
        print('Giving 5 cards to player', i + 1 ,"...")
        for _ in range(5):
            cards.append(fishTank.getCard())
        sleep(1)
        print('Player', i + 1 ," has its own 5 cards")
        players.append(Player(name,cards))
    
    firstPlayerNum = whoPlayes(players)
    clear()
    play(firstPlayerNum,players,fishTank)

main()
    
