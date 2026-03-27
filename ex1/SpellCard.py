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
            raise ValueError(f'Effect must be one of {valid_effects}')

    def play(self, game_state: dict) -> dict:
        super().play(game_state)

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

        game_state.update({'play': play})
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        """Spells are consumed when played (one-time use)."""
        pass
