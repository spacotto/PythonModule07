"""
Exercise 1: Deck Builder

Permanent game modifiers.
"""

from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        """Represent permanent game modifiers."""
        super().__init__(name, cost, rarity)
        self._effect: str = effect

    def play(self, game_state: dict) -> dict:
        """Artifacts remain in play until destroyed."""
        pass

    def activate_ability(self) -> dict:
        pass
