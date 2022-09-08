from unittest import TestCase
from game_cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card = Card(8, "Spade")
        self.card2 = Card(1, "Diamond")

    def test__init__valid1(self):
        self.assertEqual(8, self.card.value)
        self.assertEqual("Spade", self.card.suit)

    def test__init__invalid1(self):
        with self.assertRaises(TypeError):
            Card(12, "Hello")

    def test__init__invalid2(self):
        with self.assertRaises(TypeError):
            Card("5", "Spade")

    def test__init__invalid3(self):
        with self.assertRaises(TypeError):
            Card(5, 7)

    def test__init__invalid4(self):
        with self.assertRaises(ValueError):
            Card(14, "Spade")

    def test__init__invalid5(self):
        with self.assertRaises(ValueError):
            Card(0, "Spade")

    def test__init__invalid6(self):
        with self.assertRaises(ValueError):
            Card(-1, "Spade")

    def test__gt__valid1(self):
        self.assertGreater(self.card2, self.card)

    def test__gt__valid2(self):
        # Edge case
        card2 = Card(13, "Diamond")
        self.assertGreater(self.card2, card2)

    def test__gt__valid3(self):
        card1 = Card(1, "Club")
        card2 = Card(1, "Diamond")
        self.assertLess(card2, card1)

    def test__gt__valid4(self):
        card1 = Card(1, "Club")
        card2 = Card(1, "Spade")
        self.assertLess(card2, card1)

    def test__gt__invalid1(self):
        with self.assertRaises(ValueError):
            card1 = Card(5, "Spade")
            card2 = Card(5, "Spade")
            self.assertGreater(card1, card2)

    def test__eq__valid1(self):
        card2 = Card(9, "Spade")
        self.assertNotEqual(self.card, card2)

    def test__eq__valid2(self):
        self.assertEqual(self.card, self.card)

