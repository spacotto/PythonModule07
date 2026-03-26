"""
Exercise 1: Deck Builder

Permanent game modifiers.
"""

from .Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        """Represent permanent game modifiers."""
        pass

    def play(self, game_state: dict) -> dict:
        """Artifacts remain in play until destroyed."""
        pass

    def activate_ability(self) -> dict:
        pass
