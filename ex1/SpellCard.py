"""
Exercise 1: Deck Builder

Instant magic effects.
"""

import random
from ex0.Card import Card


class SpellCard(Card):
    """Processes instant magical effects"""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self._type: str = 'Spell'

        valid_effects: list = ['damage', 'heal', 'buff', 'debuff']
        if effect_type in valid_effects:
            self._effect_type: str = effect_type
        else:
            self._effect_type = None

    def play(self, game_state: dict) -> dict:
        play: dict = {
             'card_played': self._name,
             'mana_used': self._cost,
             }

        if self._effect_type == 'damage':
            x: int = random.randint(1, 10)
            play.update({'effect': f'Deal {x} damage to target' })

        if self._effect_type == 'heal':
            x: int = random.randint(1, 10)
            play.update({'effect': f'Heal {x} HP to target'})

        if self._effect_type == 'buff':
            play.update({'effect': 'Buff target'})

        if self._effect_type == 'debuff':
            play.update({'effect': 'Debuff target'})

        return play

    def resolve_effect(self, targets: list) -> dict:
        """Spells are consumed when played (one-time use)."""
        pass
