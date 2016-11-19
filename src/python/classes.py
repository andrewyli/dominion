"""
This module contains the classes relevant to the game.
"""

class Card():
    """
    Any Dominion card.
    """
    def __init__(self, name):
        self.name = name


class ActionCard(Card):
    """
    An action card.
    """


class TreasureCard(Card):
    """
    The currency of the game.
    """


class VictoryCard(Card):
    """
    Determines a player's points at the end of the game.
    """


class AttackCard(Card):
    """
    A card that can target another player (generally negatively).
    """


class ReactionCard(Card):
    """
    A type of card that can respond to an opponent's action on their turn.
    """


class Game():
    """
    A game instance that contains the player, the discard/supply piles.
    """
    def __init__(self, players, supply_piles, turn=0):
        self.players = players
        self.supply_piles = supply_piles
        self.turn = turn

    def tick():
        """
        Takes a turn for the next player and increments turn counter.
        """
        self.players[self.turn % len(self.players)].take_turn(self)
        self.turn += 1


class Player():
    """
    Represents a generic player in the game.
    """
    def __init__(self, name, default_actions=1, default_buys=1):
        self.name = name
        # The Cards a Player has cycle through these lists:
        self.deck = []
        self.hand = []
        self.discard = []
        # Defaults of temporary attributes used during a Player's turn:
        self.default_actions = default_actions
        self.default_buys = 1
        self.default_money = 0
        # Temporary attributes used and modified during a Player's turn:
        self.actions = self.default_actions
        self.buys = self.default_buys
        self.money = self.default_money

    def take_turn(self, game):
        """
        The mechanism by which Player performs actions in the action, buy,
        and clean-up phases.
        """
        # Action Phase:
        done = False
        while self.actions > 0 and not done:
            # This needs to ask what Card Player wants to use if any.
            pass
        # Buy Phase:
        done = False
        while self.buys > 0 and not done:
            # This needs to ask what Player wants to buy if anything.
            pass
        # Clean-up Phase
        for card in self.hand:
            self.discard.append(self.hand.pop())

        """NOT FINISHED YET"""
