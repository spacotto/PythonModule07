"""
Exercise 1: Deck Builder

Instant magic effects.
"""

import random
from enum import Enum
from typing import Dict, Any, List

from ex0.Card import Card


class Effects(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'
    BUFF = 'buff'
    DEBUFF = 'debuff'


class SpellCard(Card):
    """Processes instant magical effects"""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self._type: str = 'Spell'

        valid_effects: List[str] = [effect.value for effect in Effects]
        if effect_type in valid_effects:
            self._effect_type: str = effect_type
        else:
            raise ValueError(f'Effect must be one of {valid_effects}')

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        super().play(game_state)

        play: Dict[str, Any] = {
             'card_played': self._name,
             'mana_used': self._cost,
             }

        if self._effect_type == 'damage':
            x: int = random.randint(1, 10)
            play.update({'effect': f'Deal {x} damage to target'})

        if self._effect_type == 'heal':
            y: int = random.randint(1, 10)
            play.update({'effect': f'Heal {y} HP to target'})

        if self._effect_type == 'buff':
            play.update({'effect': 'Buff target'})

        if self._effect_type == 'debuff':
            play.update({'effect': 'Debuff target'})

        game_state.update({'play': play})
        return game_state

    def resolve_effect(self, targets: List[Any]) -> Dict[str, Any]:
        """Spells are consumed when played (one-time use)."""

        result: Dict[str, Any] = {
            'spell_cast': self._name,
            'effect_type': self._effect_type,
            'targets_affected': [],
            'resolve': True
        }

        for target in targets:
            target_name = getattr(target, '_name', str(target))
            result['targets_affected'].append(target_name)

        if self._effect_type == 'damage':
            result['action'] = f"Dealt damage to {len(targets)} targets."
        elif self._effect_type == 'heal':
            result['action'] = f"Healed up {len(targets)} targets."
        elif self._effect_type == 'buff':
            result['action'] = f"Buffed {len(targets)} targets."
        elif self._effect_type == 'debuff':
            result['action'] = f"Debuffed {len(targets)} targets."

        return result
