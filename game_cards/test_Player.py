from unittest import TestCase, mock
from unittest.mock import patch
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Dani")
        self.cards_list = DeckOfCards()

    def test__init__valid1(self):
        self.assertEqual(self.player.name, "Dani")
        self.assertEqual(self.player.number_of_cards, 26)
        self.assertEqual(self.player.deck_of_cards, [])

    def test__init__invalid1(self):
        with self.assertRaises(TypeError):
            Player(11)

    def test__init__invalid2(self):
        with self.assertRaises(ValueError):
            Player("Dani", "1")

    def test__init__valid2(self):
        player = Player("Kobi", 27)
        self.assertEqual(player.number_of_cards, 26)

    def test__init__valid3(self):
        player = Player("David", 9)
        self.assertEqual(player.number_of_cards, 26)

    def test_set_hand_invalid1(self):
        with self.assertRaises(TypeError):
            self.player.set_hand(10)

        with self.assertRaises(TypeError):
            self.player.set_hand("10")

    def test_set_hand_value(self):
        self.player.set_hand(self.cards_list)
        print(self.player.deck_of_cards)
        self.assertEqual(len(self.player.deck_of_cards), 26)

    def test_set_hand_value2(self):
        p1 = Player("Moshe", 27)
        p1.set_hand(self.cards_list)
        print(p1.deck_of_cards)
        self.assertEqual(len(p1.deck_of_cards), 26)
        self.assertNotEqual(len(p1.deck_of_cards), 27)
        print(f"len is: {len(p1.deck_of_cards)}")

    def test_set_hand_value3(self):
        p2 = Player("David", 9)
        p2.set_hand(self.cards_list)
        print(p2.deck_of_cards)
        self.assertEqual(len(p2.deck_of_cards), 26)
        self.assertNotEqual(len(p2.deck_of_cards), 9)
        print(f"len is: {len(p2.deck_of_cards)}")

    # def test_set_hand_mock(self):
    #     with patch("game_cards.DeckOfCards.DeckOfCards.deal_one") as mock_deal_one:
    #         mock_deal_one.return_value = Card(1, "Diamond")
    #         self.player.set_hand(self.cards_list)
    #         print("Card is:", mock_deal_one.return_value)
    #         self.assertNotIn(Card(1, "Diamond"), self.player.deck_of_cards)
    #         mock_deal_one.return_value = Card(13, "Club")
    #         print("Card is:", mock_deal_one.return_value)
    #         self.assertEqual(self.cards_list.deal_one(), mock_deal_one.return_value)

    @mock.patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(1, "Diamond"))
    def test_set_hand_mock2(self, mock_name):
        # Mock deal_one and test if the card is in set_hand
        self.player.set_hand(self.cards_list)
        self.assertIn(Card(1, "Diamond"), self.player.deck_of_cards)

    def test_get_card_valid(self):
        # Test if the card removed from the deck of cards
        self.player.set_hand(self.cards_list)
        card = self.player.get_card()
        print(card)
        self.assertNotIn(card, self.player.deck_of_cards)

    def test_add_card_invalid(self):
        with self.assertRaises(TypeError):
            self.player.add_card("10")
            self.player.add_card(10)

    def test_add_card_valid1(self):
        # Test if the added card in the player's deck of cards (In)
        card = Card(8, "Diamond")
        self.player.add_card(card)
        self.assertIn(card, self.player.deck_of_cards)
        print(self.player.deck_of_cards)

    def test_add_card_valid2(self):
        # Test if the added card in the player's deck of cards (Equal)
        card = Card(9, "Diamond")
        self.player.add_card(card)
        self.assertEqual(1, len(self.player.deck_of_cards))
        print(self.player.deck_of_cards)