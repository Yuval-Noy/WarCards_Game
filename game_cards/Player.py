import random as rnd
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class Player:
    # Object of the player name, player's deck of cards and player's number of cards
    # The number of cards will be chosen in the beginning, default is 26
    # The number of cards won't be higher than 26 and lower than 10

    def __init__(self, name, number_of_cards=26):
        """Object constructor, receives player name and his number of cards, initializes a list of deck of cards"""

        if type(name) != str:
            # name must be a string
            raise TypeError("Name must be a string!")

        if type(number_of_cards) != int:
            # number_of_cards must be an integer
            raise ValueError("Cards number must be int!")

        if number_of_cards < 10 or number_of_cards > 26:
            # Number of cards won't be higher than 26 and lower than 10
            number_of_cards = 26

        self.number_of_cards = number_of_cards
        self.name = name
        self.deck_of_cards = []

    def __str__(self):
        """Represent the player name and his deck of cards"""
        return f"""Player Name: {self.name}
Player Hand: {self.deck_of_cards}
Player Number of Cards: {len(self.deck_of_cards)}"""

    def set_hand(self, cards_list):
        """Receives deck of cards and deals random cards for the player as the chosen number"""

        # cards_list must be DeckOfCards
        if type(cards_list) != DeckOfCards:
            raise TypeError("Must be type DeckOfCards!")

        for i in range(self.number_of_cards):
            self.deck_of_cards.append(cards_list.deal_one())

    def get_card(self):
        """Selects a random card from the player's deck of cards and removes it"""
        card = rnd.choice(self.deck_of_cards)
        self.deck_of_cards.remove(card)
        return card

    def add_card(self, card):
        """Receives a card and add it to the player's deck of cards"""

        # card must be type Card
        if type(card) != Card:
            raise TypeError("Must be type Card!")

        self.deck_of_cards.append(card)
