"""
Exercise 1: Deck Builder

Instant magic effects.
"""

from .Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Processes instant magical effects"""
        valid_effects: list = ['damage', 'heal', 'buff', 'debuff']

        super().__init__(name, cost, rarity)
        self._effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        """Spells are consumed when played (one-time use)."""
        pass

    def resolve_effect(self, targets: list) -> dict:
        """Manage spell mechanics."""
        pass
