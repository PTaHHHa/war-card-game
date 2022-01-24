"""
Simple implementaion of 'War' card game
"""
import random

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',\
     'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

suits = ('Spades', 'Heards', 'Diamonds', 'Clubs')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five':5, 'Six': 6, 'Seven':7, 'Eight': 8,\
     'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    """
    Hi, this is docstring
    """
    def __init__(self, rank, suit):
        self.rank = rank.capitalize()
        self.suit = suit.capitalize()
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    """
    Hi, this is docstring
    """
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                current_card = Card(rank, suit)
                self.all_cards.append(current_card)
        print('Deck created, but not shuffled')

    def shuffle_deck(self):
        """
        Hi, this is docstring
        """
        print('Deck is shuffled\n')
        random.shuffle(self.all_cards)
        return self.all_cards

    def deal_card(self):
        """
        Hi, this is docstring
        """
        return self.all_cards.pop()

    def __len__(self):
        return len(self.all_cards)

class Player:
    """
    Hi, this is docstring
    """
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """
        Hi, this is docstring
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """
        Hi, this is docstring
        """
        if isinstance(new_cards, list):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self):
        return str(f'Player {self.name} has {len(self.all_cards)}.')


def main():
    """
    Hi, this is docstring
    """
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    deck = Deck()
    deck.shuffle_deck()

    for _ in range(26):
        player1.add_cards(deck.deal_card())
        player2.add_cards(deck.deal_card())
    game_on = True
    war = False
    player1_war_cards = []
    player2_war_cards = []
    player1_card = []
    player2_card = []
    game_round = 0

    while game_on:
        if len(player1.all_cards) == 0:
            print(f'{player2.name} won. {player1.name} is out of cards')
            game_on = False
        elif len(player2.all_cards) == 0:
            print(f'{player1.name} won. {player2.name} is out of cards')
            game_on = False
        else:
            game_round += 1
            print(f'Round: {round}')
            player1_card = player1.remove_one()
            player2_card = player2.remove_one()

            print(f'Player 1 card: {player1_card} {player1_card.value}.\
            \nPlayer 2 card: {player2_card} {player2_card.value}.')
            if player2_card.value < player1_card.value:
                print('Player 1 won!')
                player1.add_cards(player1_card)
                player1.add_cards(player2_card)
                print(f'Player 1 {len(player1.all_cards)} cards left.\
                \nPlayer 2 {len(player2.all_cards)} cards left.\n')
            elif player2_card.value > player1_card.value:
                print('Player 2 won!')
                player2.add_cards(player2_card)
                player2.add_cards(player1_card)
                print(f'Player 1 {len(player1.all_cards)} cards left.\
                \nPlayer 2 {len(player2.all_cards)} cards left.\n')
            elif player2_card.value == player1_card.value:
                war = True
                player1_war_cards.append(player1_card)
                player2_war_cards.append(player2_card)
                while war:
                    print('War!')
                    if len(player1.all_cards) < 2:
                        print(f'{player1.name} has not enough cards. ({len(player1.all_cards)})\
                             {player2.name} won!')
                        war = False
                        game_on = False
                        break
                    elif len(player2.all_cards) < 2:
                        print(f'{player2.name} has not enough cards. ({len(player2.all_cards)})\
                             {player1.name} won!')
                        war = False
                        game_on = False
                        break
                    for _ in range(2):
                        player1_war_cards.append(player1.remove_one())
                        player2_war_cards.append(player2.remove_one())
                    print(f'WAR! Player 1 cards:\
                         {[player.value for player in player1_war_cards]}')
                    print(f'WAR! Player 2 cards:\
                         {[player.value for player in player2_war_cards]}')
                    if sum(player.value for player in player1_war_cards) < sum(player.value for player in player2_war_cards):
                        print('Player 2 won war!')
                        player2.add_cards(player1_war_cards)
                        player2.add_cards(player2_war_cards)
                        print(f'Player 1 {len(player1.all_cards)} cards left.\
                        \nPlayer 2 {len(player2.all_cards)} cards left.\n')
                        player1_war_cards = []
                        player2_war_cards = []
                        break
                    elif sum(player.value for player in player2_war_cards) < sum(player.value for player in player1_war_cards):
                        print('Player 1 won war!')
                        player1.add_cards(player2_war_cards)
                        player1.add_cards(player1_war_cards)
                        print(f'Player 1 {len(player1.all_cards)} cards left.\
                        \nPlayer 2 {len(player2.all_cards)} cards left.\n')
                        player1_war_cards = []
                        player2_war_cards = []
                        break
                    elif sum(player.value for player in player2_war_cards) == sum(player.value for player in player1_war_cards):
                        print('Draw. Another war incoming!')
                        continue


if __name__ == '__main__':
    main()
