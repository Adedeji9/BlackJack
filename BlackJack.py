import collections
import numpy as np
from random import choice
import sys

Card = collections.namedtuple('Card', ['rank','suit'])

#### Create Pack of Cards
class Cards:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    #### Initiating Cards decks
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    #### Check the length of deck
    def __len__(self):
        return len(self._cards)

    #### Get the card at a position
    def __getitem__(self,position):
        return self._cards[position]





#### Calculating the value of Hand for dealer and Player
def Hand(Pack):
    Val = 0
    Ace = 0

    #### Iterating through Cards in Pack for either Player of dealer
    for i in Pack:

        ### Checking for Jack, Queens and King
        if i.rank in list('JQK'):
             Val += 10
        else:

            ### Checking for Ace and delaying its addition so as to check its effect on Val
            if i.rank == 'A':
                Ace = 11;
            else:
                ### Adding the rank of other Cards
                Val += int(i.rank)

    ### Checking the effects of the ace of val and picking the most favourable out come for dealer or player             
    if Val + Ace < 21:
        Val += Ace
    else:
        Val += 1

    return Val

#### Logo
def Logo():
    print('\n                            **************************************************')
    print('\n                            **    Basic BlackJack implemented in Python     **')
    print('\n                            **    Written By Dr. Adedeji Aremu 2018         **')
    print('\n                            **************************************************')







### Reveal The Cards for Either Player of Dealer                        
def Reveal(Pack,ind,message):
    print('\n{}'.format(message))
    for i in ind:
        print(Pack[i])


#### Test for who won after a series of Stands
def Who_Won(P1,D1,Player,Dealer):
     if P1 > D1:
        print('\nCongratulations you won !!! Dealer lost.')        
     if P1 < D1:
        print('\nSorry you lost !!! Dealer won.')
     if P1 == D1:         
        print('\nIt was a draw')
     Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player:')
     Reveal(Dealer,np.arange(len(Dealer)),'Revealing Cards on Dealer:')
     sys.exit()
                          




#### Entry point to code
if __name__ == "__main__":

    Logo()
    
    #### Initiate Deck of Cards
    Deck = Cards()
    Game = 'On'

    #### Select 2Cards for Player
    Player = [choice(Deck) for i in np.arange(2)]

    #### Select 2Cards for Dealer
    Dealer = [choice(Deck) for i in np.arange(2)]

    #### Reveal Player Cards
    Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player')

    #### Reveal One Card on Dealer
    Reveal(Dealer,np.arange(1),'Revealing One Card on Dealer, other Card is Hidden')

    #### Initiating Stand Counter
    D_Cnt = 0
    P_Cnt = 0
    Std_Rnd = 2 #### Number of rounds to allow stand before end of Game
    
    #### Continue Game until Game is set to Over
    while True:
        
        P1 = Hand(Player)

        Key = ' '
        
        if 8 < P1 and P1 < 12:
            ### if player has a stake between 9-11 offer to Double and the Player has to stand till game ends
            while Key not in ['Y','N','E']:
                Key = input('\nWould you like to double your Stake (Y/N or E to exit game) ?')
            if Key == 'Y':
                Player.extend([choice(Deck)])
                Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player')
                P_Cnt += 20 ###  Used to Stand the Player for the rest of the Game
            if Key == 'E':
                print('\n Bye for now')
                break
            
        else:
            ### Natural Black Jack Check
            if P1 == 21 and D1 != 21:
                print('\nCongratulations !! you achieved a Natural Black Jack !!')
                print('\nPlease receive 2.5 times your Stack !!')
                Game = 'Over'
                Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player:')
                Reveal(Dealer,np.arange(len(Dealer)),'Revealing Cards on Dealer:')
                break
            else:
                
        
                Key = ' '
                      
                ### Stick/Stand or Hit/Twist
                if P_Cnt < 20:
                    while Key not in ['H','S','E']:
                        Key = input('\nHit(H) or Stand(S) or Exit(E):')

                    if Key == 'H':
                        Player.extend([choice(Deck)])
                        Reveal(Player,np.arange(len(Player)),'Players Cards:')
                        P1 = Hand(Player)

                        #### Bust Check
                        if P1 > 21:
                              print('\nDealer won !! You were Busted !!')
                              Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player:')
                              Reveal(Dealer,np.arange(len(Dealer)),'Revealing Cards on Dealer:')
                              break
                    else:
                        if Key == 'E':
                              print('\nHope you enjoyed the game. Bye...')
                              break
                        else:
                              #### Increasing the Stand counter when player Stands
                              if Key == 'S':
                                    Reveal(Player,np.arange(len(Player)),'Player Cards:')
                                    P_Cnt += 1

                #### Check Dealer's Hand and Hit Dealer if < 17
                D1 = Hand(Dealer)
                if D1 < 17:
                      Dealer.extend([choice(Deck)])
                      D1 = Hand(Dealer)
                      if D1 > 21:
                          print('\nDealer just went Bust ! You Won !!!')
                          Reveal(Player,np.arange(len(Player)),'Revealing Cards on Player:')
                          Reveal(Dealer,np.arange(len(Dealer)),'Revealing Cards on Dealer:')
                          break
                      else:
                          Who_Won(P1,D1,Player,Dealer)
                else:
                      #### Dealer Stands and this is counted
                      D_Cnt += 1


                #### If both Dealer and Player Stands for Std_Rnd
                      
                if P_Cnt > Std_Rnd and D_Cnt>Std_Rnd:
                      P1 = Hand(Player)
                      D1 = Hand(Dealer)
                      Who_Won(P1,D1,Player,Dealer)

                      

                      
                      
                    

        
