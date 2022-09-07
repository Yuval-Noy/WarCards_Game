import random as rnd
from game_cards.Card import Card


class DeckOfCards:
    # Object of deck of 52 cards
    # Each card consists different value and suit

    def __init__(self):
        """Object constructor, initializes the deck of cards"""
        self.deck_of_cards = []

        # A nested loop to set up the deck of cards
        for value in range(1, 14):
            for suit in ["Diamond", "Spade", "Heart", "Club"]:
                card = (Card(value, suit))
                self.deck_of_cards.append(card)

    def __repr__(self):
        """Represent the deck of cards"""
        return f"{self.deck_of_cards}"

    def cards_shuffle(self):
        """Shuffles the deck of cards"""
        rnd.shuffle(self.deck_of_cards)
        return

    def deal_one(self):
        """Selects a random card from the deck of cards, removes it and returns it"""
        if not len(self.deck_of_cards) > 0:
            return None

        card = rnd.choice(self.deck_of_cards)
        self.deck_of_cards.remove(card)
        return card
