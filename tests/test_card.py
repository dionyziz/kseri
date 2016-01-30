import unittest
from card import Card, Suit, ACE, JACK, QUEEN, KING


class TestCard(unittest.TestCase):
    def test_str(self):
        ace_of_spades = Card(ACE, Suit.Spades)
        self.assertEqual(str(ace_of_spades), 'Ace of Spades')

        jack_of_hearts = Card(JACK, Suit.Hearts)
        self.assertEqual(str(jack_of_hearts), 'Jack of Hearts')

        queen_of_diamonds = Card(QUEEN, Suit.Diamonds)
        self.assertEqual(str(queen_of_diamonds), 'Queen of Diamonds')

        king_of_clubs = Card(KING, Suit.Clubs)
        self.assertEqual(str(king_of_clubs), 'King of Clubs')

        ten_of_diamonds = Card(10, Suit.Diamonds)
        self.assertEqual(str(ten_of_diamonds), '10 of Diamonds')

    def test_is_figure(self):

        queen_of_diamonds = Card(QUEEN, Suit.Diamonds)
        self.assertTrue(queen_of_diamonds.is_figure())

        ten_of_diamonds = Card(10, Suit.Diamonds)
        self.assertFalse(ten_of_diamonds.is_figure())

        king_of_clubs = Card(KING, Suit.Clubs)
        self.assertTrue(king_of_clubs.is_figure())
