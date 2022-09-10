from unittest import TestCase, mock

from game_cards.CardGame import CardGame
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):
    def setUp(self):
        self.p1 = Player("Yuval")
        self.p2 = Player("Omer")
        self.new_game = CardGame(self.p1, self.p2)
        self.hand = DeckOfCards()

    def test__init__invalid1(self):
        # Test str and int TypeError (p1, p2)
        with self.assertRaises(TypeError):
            CardGame("Yuval", "Omer")
            CardGame(11, 9)

    def test__init__invalid2(self):
        # Test str TypeError (number of cards)
        with self.assertRaises(TypeError):
            CardGame(self.p1, self.p2, "15", "8")
            CardGame(self.p1, self.p2, 15, "8")
            CardGame(self.p1, self.p2, "15", 8)

    def test__init__valid1(self):
        # Test validation of cards number in the deck
        self.assertEqual(len(self.hand.deck_of_cards), 52)

    def test__new_game__valid1(self):
        # Test edge case for number of cards (=26)
        CardGame(self.p1, self.p2, 27, 9)
        self.assertEqual(self.p1.number_of_cards, 26)
        self.assertEqual(self.p2.number_of_cards, 26)
        print(self.p1.number_of_cards)
        print(self.p2.number_of_cards)

    def test__new_game__valid2(self):
        # Test edge case for number of cards (=26)
        CardGame(self.p1, self.p2, 9, 27)
        self.assertEqual(self.p1.number_of_cards, 26)
        self.assertEqual(self.p2.number_of_cards, 26)
        print(self.p1.number_of_cards)
        print(self.p2.number_of_cards)

    def test__new_game__valid3(self):
        # Test validation of number of cards
        CardGame(self.p1, self.p2, 26, 10)
        self.assertEqual(self.p1.number_of_cards, 26)
        print(self.p1.deck_of_cards)
        self.assertEqual(self.p2.number_of_cards, 10)
        print(self.p2.deck_of_cards)

    def test_new_game_shuffle(self):
        # Test player1's deck of cards in two games
        pl1 = Player("Dani")
        pl2 = Player("Gali")
        new_game2 = CardGame(pl1, pl2)
        print(pl1.deck_of_cards)
        print(self.p1)
        self.assertNotEqual(pl1.deck_of_cards, self.p1.deck_of_cards)

    def test_new_game_invalid(self):
        # Test when starting a new match during a match
        with self.assertRaises(ValueError):
            self.new_game.new_game()

    def test_get_winner_p2_win(self):
        # Test when p2 win
        CardGame(self.p1, self.p2, 17, 18)
        self.assertEqual(self.new_game.get_winner(), self.p2)

    def test_get_winner_p1_win(self):
        # Test when p1 win
        CardGame(self.p1, self.p2, 18, 17)
        self.assertEqual(self.new_game.get_winner(), self.p1)

    def test_get_winner_draw_valid(self):
        # Test when match is draw
        CardGame(self.p1, self.p2)
        self.assertEqual(self.new_game.get_winner(), None)
