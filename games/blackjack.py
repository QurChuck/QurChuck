import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return f'Deck currently have {len(self.all_cards)} cards left'

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name):
        self.hand = []
        self.name = name

    def draw_card(self,card):
            self.hand.append(card)

    def hand_value(self):
        self.hand_values = []
        recheck = False

        for card in self.hand:
            self.hand_values.append(card.value)

        self.sum_hand = sum(self.hand_values)
        #recheck
        if self.sum_hand > 21 and not recheck:
            for index, item in enumerate(self.hand_values):
                if item == 11:
                    self.hand_values[index] = 1
                else:
                    pass
            recheck = True
            self.sum_hand = sum(self.hand_values)
        return self.sum_hand

    def clear_hand(self):
        self.hand = []
        self.hand_values = []

    def __str__(self):
        sum_hand = self.hand_value()
        string_hand = ''
        for card in self.hand:
            string_hand = string_hand + card.rank + ' of ' + card.suit + ' | '
        string_hand = string_hand[:-3]
        return f'{self.name} hand is [{string_hand}] {self.hand_values} = {sum_hand}'


def game():
    game_on = True
    new_deck = Deck()
    player = Player("Player")
    dealer = Player("Dealer")

    while game_on:
        
        del new_deck
        new_deck = Deck()
        new_deck.shuffle()
        player.clear_hand()
        player_hand_value = 0     
        dealer.clear_hand()
        dealer_hand_value = 0
        player_turn = True
        ask_again = True

        for _ in range(2):
            player.draw_card(new_deck.deal_one())
            dealer.draw_card(new_deck.deal_one())

        while player_turn:
            string_dealer_hand = dealer.hand[0].rank + ' of ' + dealer.hand[0].suit + ' | BLANK'
            print(f'Dealer cards are [{string_dealer_hand}] [{dealer.hand[0].value},*]')
            print(player)

            confirm = False
            player_hand_value = player.hand_value()
            dealer_hand_value = dealer.hand_value()

            while not confirm and player_hand_value < 21:
                
                try:
                    play_next = input("Draw(1) next card or Pass(0)? ")

                except:
                    print("Wrong input! Try again!")

                if play_next == '1':
                    
                    player.draw_card(new_deck.deal_one())                    
                    print(f'Player draws {player.hand[-1]}[{player.hand[-1].value}]')
                    confirm = True

                elif play_next == '0':
                    player_turn = False
                    confirm = True

                else:
                    print("Wrong input, try again!")

                player_hand_value = player.hand_value()       

                if player_hand_value >= 21:
                    print(f'Player draws {player.hand[-1]} that gives {player_hand_value}!')
                    print(player)
                    player_turn = False
                    confirm = True
                    print('..........................')

        if player_hand_value > 21:
            print("Player Busted! Game over! Dealer won!")
        
        else:
            print(dealer)

            while dealer_hand_value <= player_hand_value and dealer_hand_value < 21:
                dealer.draw_card(new_deck.deal_one())
                dealer_hand_value = dealer.hand_value()
                print(f'Dealer draws {dealer.hand[-1]}[{dealer.hand[-1].value}]')
                print(dealer)
            
            if dealer_hand_value > 21:
                print("Dealer Busted! Round over! Player won!")

            elif player_hand_value == dealer_hand_value:
                print("It's a Draw!")

            elif player_hand_value < dealer_hand_value:
                print("Dealer won!")

            else:
                print("Player won!")

        while ask_again:
            quit = input("Do You want play again? (Y/N): ")

            if quit.lower() == 'y':
                game_on = True
                ask_again = False

            elif quit.lower() == 'n':
                game_on = False
                ask_again = False

            else:
                print("Wrong input, try again!")

game()
