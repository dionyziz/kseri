import random
from card import Card, Collection, Deck


CARDS_PER_PLAYER = 6
CARDS_ON_TABLE = 4


class Player(object):
    hand = Collection()
    collected = Collection()
    score = 0

    def __init__(self, index):
        self.score = 0
        self.index = index

    def play(self, table):
        """Asks a player to make a move given the table configuration.
           The player returns a card from their hand."""
        assert(isinstance(table, Collection))

    def observe(self, player, card):
        pass

    def updateScore(self, points):
        self.score += points

    def __str__(self):
        return 'Player %i' % self.index


class ComputerPlayer(Player):

    def __init__(self, index, strategy):
        super(ComputerPlayer, self).__init__(index)
        assert(isinstance(strategy, Strategy))
        self.strategy = strategy

    def observe(self, player, card):
        self.strategy.observe(player, card)

    def play(self, table):
        return self.strategy(table, self.hand)


class HumanPlayer(Player):

    def __init__(self, index, controller):
        super(HumanPlayer, self).__init__(index)
        assert(isinstance(controller, Controller))
        self.controller = controller

    def observe(self, player, card):
        self.controller.observe(player, card)

    def play(self, table):
        return self.controller.observe(self.hand, table)


class Controller(object):

    def play(self, hand, table):
        raise NotImplemented

    def observe(self, player, card):
        pass


class CLIController(Controller):
    def observe(self, player, card):
        print('%s played %s' % (player, card))

    def play(self, hand, table):
        print('Your hand:')
        print(hand)

        print('The table:')
        print(table)


class Strategy(object):
    def play(self, hand, table):
        raise NotImplemented

    def observe(self, card):
        pass


class RandomStrategy(Strategy):
    def play(self, hand, table):
        for hand_card in hand:
            for table_card in table:
                if hand_card.rank == table_card.rank:
                    return hand_card

        return random.choice(hand)


class Game(object):
    deck = Deck()
    table = Collection()

    def __init__(self, numPlayers):
        assert(numPlayers == 2 or numPlayers == 4)
        self.numPlayers = numPlayers
        self.players = [HumanPlayer(0)]

        for i in range(self.numPlayers - 1):
            self.players.push(ComputerPlayer(i, RandomStrategy()))

    def initialDeal(self):
        self.deal()
        self.tableDeal()

    def tableDeal(self):
        for i in range(CARDS_ON_TABLE):
            self.deck.moveCardTo(self.table)

    def deal(self):
        for player in self.players:
            for i in range(CARDS_PER_PLAYER):
                self.deck.moveCardTo(player.hand)

    def round(self):
        for player in self.players:
            card = player.play(self.table)

            assert(card in player.hand)

            try:
                top = self.table.top()
            except IndexError:
                player.hand.moveCardTo(self.table, card)
                continue

            if top.rank == card.rank:
                if self.table.isSingle():
                    # kseri
                    if card.rank == 11:
                        player.updateScore(20)
                    else:
                        player.updateScore(10)

                self.table.moveAllCardsTo(player.collected)
                player.hand.moveCardTo(player.collected, card)
            else:
                player.hand.moveCardTo(self.table)
