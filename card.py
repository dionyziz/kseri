import random
from enum import Enum

ACE = 1
JACK = 11
QUEEN = 12
KING = 13

Suit = Enum('Spades', 'Hearts', 'Diamonds', 'Clubs')

class Card(object):
    def __init__(self, rank, suit):
        assert(1 <= rank <= 13)
        self.rank = rank
        assert(suit in Suit)
        self.suit = suit

    def __str__(self):
        rankstr = str(self.rank)

        if self.is_figure() or self.rank == ACE:
            rankstr = {
                ACE: 'Ace',
                JACK: 'Jack',
                QUEEN: 'Queen',
                KING: 'King'
            }[self.rank]

        return '%s of %s' % (rankstr, str(self.suit))

    def is_figure(self):
        return 10 < self.rank <= 13

    def points(self):
        if self.rank == ACE or\
           self.rank == 10 or\
           self.is_figure():
            return 1

        if self.rank == 2 and self.spades:
            return 1

        if self.rank == 10 and self.diamonds:
            return 2

        return 0


class Collection(object):
    _cards = []

    def add(self, card):
        assert(isinstance(card, Card))

        self._cards.append(card)

    def moveAllCardsTo(self, target):
        assert(isinstance(target, Collection))

        while not self.isEmpty():
            self.moveCardTo(target)

    def moveCardTo(self, target, card = None):
        assert(isinstance(target, Collection))
        assert(isinstance(card, Card))

        if card is None:
            card = self.top()

        self._cards.remove(card)
        target.add(card)

    def top(self):
        return self._cards[-1]

    def points(self):
        points = 0

        for card in self._cards:
            points += card.points()

        return points

    def shuffle(self):
        random.shuffle(self._cards)

    def isSingle(self):
        return len(self._cards) == 1

    def isEmpty(self):
        return not self._cards

    def __str__(self):
        return ', '.join(map(str, self._cards))


class Deck(Collection):
    def __init__(self):
        for rank in range(1, 14):
            for suit in Suit:
                self.add(Card(rank, suit))

        self.shuffle()
