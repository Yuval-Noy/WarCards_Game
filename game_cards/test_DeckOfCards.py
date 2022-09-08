from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test__init__valid1(self):
        self.assertEqual(len(self.deck.deck_of_cards), 52)

    def test__init__valid2(self):
        self.assertIn(Card(1, "Diamond"), self.deck.deck_of_cards)

    def test__init__valid3(self):
        self.assertIn(Card(13, "Club"), self.deck.deck_of_cards)

    def test__init__invalid1(self):
        self.assertNotEqual(len(self.deck.deck_of_cards), 51)

    def test__init__invalid2(self):
        self.assertNotEqual(len(self.deck.deck_of_cards), 53)

    def test_cards_shuffle(self):
        index1 = self.deck.deck_of_cards.index(Card(9, "Spade"))
        print(f"Origin Index is - {index1}")
        self.deck.cards_shuffle()
        index2 = self.deck.deck_of_cards.index(Card(9, "Spade"))
        print(f"Index after shuffle - {index2}")
        self.assertNotEqual(index1, index2)

    def test_deal_one(self):
        new_deck = DeckOfCards()
        new_deck.deal_one()
        self.assertGreater(len(self.deck.deck_of_cards), len(new_deck.deck_of_cards))
