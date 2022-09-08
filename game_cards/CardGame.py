from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player


class CardGame:
    # Attributes are deck of cards and two players

    def __init__(self, p1, p2, p1_num_of_cards=26, p2_num_of_cards=26):
        """Object Constructor, initializes the players and their number of cards to start a new game"""

        if type(p1) != Player and type(p2) != Player:
            # Players must be type Player
            raise TypeError("Must be type Player!")

        if type(p1_num_of_cards) != int and type(p2_num_of_cards) != int:
            # Players number of cards must be type int
            raise TypeError("Must be type int!")

        if p1_num_of_cards < 10 or p1_num_of_cards > 26:
            # Number of cards won't be higher than 26 and lower than 10
            p1_num_of_cards = 26

        if p2_num_of_cards < 10 or p2_num_of_cards > 26:
            # Number of cards won't be higher than 26 and lower than 10
            p2_num_of_cards = 26

        self.p1 = p1
        self.p2 = p2
        self.p1_num_of_cards = p1_num_of_cards
        self.p2_num_of_cards = p2_num_of_cards
        self.hand = DeckOfCards()
        self.new_game()             # If the method activated during a game = print ERROR

    def __str__(self):
        """Represent the players"""
        return f"{self.p1}, {self.p2}"

    def new_game(self):
        """Shuffles the deck of cards and deal cards for each player"""
        self.hand.cards_shuffle()
        self.p1.set_hand(self.hand)
        self.p2.set_hand(self.hand)

    def get_winner(self):
        """Returns the winner of the game by the length of the decks of cards"""
        if len(self.p1.deck_of_cards) == len(self.p2.deck_of_cards):
            # Draw
            return None
        elif len(self.p1.deck_of_cards) > len(self.p2.deck_of_cards):
            # p1 is the winner
            return self.p1
        else:
            # p2 is the winner
            return self.p2

