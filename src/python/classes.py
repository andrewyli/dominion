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
    pass
