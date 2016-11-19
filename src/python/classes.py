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

    is_action = True

    def __init__(self, name):
        Card.__init__(self, name)


class



class Player():
    """
    Represents a generic player in the game
    """
    pass
