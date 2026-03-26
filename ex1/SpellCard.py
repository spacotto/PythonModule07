"""
Exercise 1: Deck Builder

Instant magic effects.
"""

from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Processes instant magical effects"""
        super().__init__(name, cost, rarity)

        valid_effects: list = ['damage', 'heal', 'buff', 'debuff']
        if effect_type in valid_effects:
            self._effect_type: str = effect_type
        else:
            self._effect_type = None

    def play(self, game_state: dict) -> dict:
        """Spells are consumed when played (one-time use)."""
        pass

    def resolve_effect(self, targets: list) -> dict:
        """Manage spell mechanics."""
        pass
