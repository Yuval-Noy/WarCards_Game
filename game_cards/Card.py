class Card:
    # Represent a card with value and suit
    # Values will be between 1-13 while: 1 - Ace, 11 - Jack, 12 - Queen, 13 - King.
    # Ace has the highest value. (Ace > x)
    # Suits have numerical values, as: 1 - Diamond; 2 - Spade; 3 - Heart; 4 - Club

    def __init__(self, value, suit):
        """Object constructor, initializes the card"""
        self.value = value
        self.suit = suit

        # Value must be an integer
        if type(value) != int:
            raise TypeError("Value must be type int!")

        # Value must be between 1-13
        if value < 1 or value > 13:
            raise ValueError("Value must be between 1-13!")

        # Suit must be one of the following symbols
        list_of_suits = ["Diamond", "Spade", "Heart", "Club"]
        if suit not in list_of_suits:
            raise TypeError("Suit must be one of the symbols!")

    def __gt__(self, other):
        """Card will be greater by his value"""
        if self.value != other.value:
            # 1 (Ace) has the highest value [Ace > x]
            if self.value == 1 or other.value == 1:
                return other.value > self.value

            return self.value > other.value

        else:
            # Suits have numerical values, while 'Diamond' is the smallest and 'Club' is the highest
            cards_type = ("Diamond", "Spade", "Heart", "Club")
            self_suit = cards_type.index(self.suit)
            other_suit = cards_type.index(other.suit)

            if self_suit == other_suit:
                # There aren't two similar cards
                raise ValueError("Can not be two similar cards!")

            return self_suit > other_suit

    def __eq__(self, other):
        """Checks if there is an identical number"""
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __repr__(self):
        """Returns the string representation of the object"""
        special_values = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        # Represent the special names in the deck of cards
        if self.value in special_values.keys():
            return f"{special_values[self.value]} of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"
