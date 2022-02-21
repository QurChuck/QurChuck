import random
from tkinter import Y
#import pdb
#import sys

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Class Card must be already defined
                self.all_cards.append(Card(suit,rank))

    def shuffle_cards(self):
        # doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

class Player:

    def __init__(self,name):
        self.deck = []
        self.name = name

    def __str__(self):
        return "Player " + self.name + " has " + str(len(self.deck)) + " cards left"

    def draw_card(self,new_cards):
        if type(new_cards) == type([]):
            self.deck.extend(new_cards) #append will add one item to the list, example: [A, B, C] append([X,Y]) = [A,B,C,[X,Y]], extend will merge lists to [A,B,C,X,Y]
        else:
            self.deck.append(new_cards)

    def remove_card(self):
        return self.deck.pop(0)

def game():
    
    game_init = True
    game_on = True

    while game_on:
        if game_init == True:
            game_round = 0
            new_deck = Deck()
            new_deck.shuffle_cards()

            player1 = Player("One")
            player2 = Player("Two")

            for _ in range(26):
                player1.draw_card(new_deck.deal_one())
                player2.draw_card(new_deck.deal_one())
        game_init = False

        game_round+=1
        print(f'Round {game_round}: ')
        print(player1)
        print(player2)

        if len(player1.deck) == 0:
            print(f'Player {player2.name} won the game!')
            game_on = False
            #break
        elif len(player2.deck) == 0:
            print(f'Player {player1.name} won the game!')
            game_on = False
            #break
        else:
            player1_cards = []
            player1_cards.append(player1.remove_card())

            player2_cards = []
            player2_cards.append(player2.remove_card())

            at_war = True

            while at_war:
                disp_p1_card = player1_cards[-1]
                disp_p2_card = player2_cards[-1]

                if player1_cards[-1].value > player2_cards[-1].value:

                    player1.draw_card(player1_cards)
                    player1.draw_card(player2_cards)
                    at_war = False
                    print(f'Player {player1.name} plays {disp_p1_card} which beats {disp_p2_card}\n({player1_cards[-1].value} > {player2_cards[-1].value})')

                elif player1_cards[-1].value < player2_cards[-1].value:

                    player2.draw_card(player1_cards)
                    player2.draw_card(player2_cards)
                    at_war = False
                    print(f'Player {player2.name} plays {disp_p2_card} which beats {disp_p1_card}\n({player1_cards[-1].value} < {player2_cards[-1].value})')

                else:
                    print(f'WAR MODE ON! - {disp_p1_card} vs {disp_p2_card} - WAR MODE ON!')
                    # This occurs when the cards are equal.
                    # We'll grab another card each and continue the current war.

                    # First check to see if player has enough cards

                    # Check to see if a player is out of cards:
                    if len(player1.deck) < 5:
                        print(f'Player {player1.name} unable to play war! Game Over at War')
                        print(f'Player {player2.name} Wins! Player {player1.name} Loses!')
                        game_on = False
                        at_war = False
                        #break

                    elif len(player2.deck) < 5:
                        print(f'Player {player2.name} unable to play war! Game Over at War')
                        print(f'Player {player1.name} Wins! Player {player2.name} Loses!')
                        game_on = False
                        at_war = False
                        #break
                    # Otherwise, we're still at war, so we'll add the next cards
                    else:
                        for _ in range(5):
                            player1_cards.append(player1.remove_card())
                            player2_cards.append(player2.remove_card())

                if game_round >= 5000:
                    print("Stuck in a infinite loop. Game has been ended")
                    game_on = False
                    break
        
        if not game_on:
            pick = False
            while not pick:
                again = input("Do You want to play again? (Y/N): ")

                if again.lower() == 'y':
                    game_on = True
                    pick = True
                    game_init = True

                elif again.lower() == 'n':
                    pick = True

                else:
                    print("Wrong Input! Try again!")

game()
#pdb.pm()
