from unittest import TestCase, mock
from unittest.mock import patch
from game_cards.CardGame import CardGame
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestCardGame(TestCase):
    def setUp(self):
        self.p1 = Player("Yuval")
        self.p2 = Player("Omer")
        self.new_game = CardGame(self.p1, self.p2)
        self.hand = DeckOfCards()

    def test__init__invalid1(self):
        with self.assertRaises(TypeError):
            CardGame("Yuval", "Omer")
            CardGame(11, 9)

    def test__init__invalid2(self):
        with self.assertRaises(TypeError):
            CardGame(self.p1, self.p2, "15", "8")

    def test__init__invalid3(self):
        CardGame(self.p1, self.p2, 30, 8)
        self.assertEqual(self.new_game.p1_num_of_cards, 26)
        self.assertEqual(self.new_game.p2_num_of_cards, 26)

    def test__init__valid1(self):
        self.assertEqual(len(self.hand.deck_of_cards), 52)

    def test_new_game(self):
        self.fail()

    def test_get_winner(self):
        self.fail()
