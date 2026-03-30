"""
Exercise 1: Deck Builder

Instant magic effects.
"""

from typing import Dict, Any, List
from enum import Enum
import random

from ex0 import Card


# ----------------------------------------------------------------------------
#  Spells Register
# ----------------------------------------------------------------------------

class Spells(Enum):
    LIGHTNING_BOLT = ("Lightning Bolt", 3, "Common", "damage")
    HEALING_POTION = ("Healing Potion", 2, "Common", "heal")
    FIREBALL = ("Fireball", 4, "Uncommon", "damage")
    SHIELD_SPELL = ("Shield Spell", 1, "Common", "buff")
    METEOR = ("Meteor", 8, "Legendary", "damage")
    ICE_SHARD = ("Ice Shard", 2, "Common", "damage")
    DIVINE_LIGHT = ("Divine Light", 5, "Rare", "heal")
    MAGIC_MISSILE = ("Magic Missile", 1, "Common", "damage")

    @property
    def s_name(self) -> str: 
        return self.value[0]
    
    @property
    def s_cost(self) -> int: 
        return self.value[1]
    
    @property
    def s_rarity(self) -> str: 
        return self.value[2]
    
    @property
    def s_effect(self) -> str: 
        return self.value[3]


# ----------------------------------------------------------------------------
#  SpellCard
# ----------------------------------------------------------------------------

class SpellCard(Card):
    """Processes instant magical effects"""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):

        # 1. Inspect the registry
        valid_spell = None
        for spell in Spells:
            if spell.s_name == name:
                valid_spell = spell.value
                break

        if not valid_spell:
            raise ValueError(f"'{name}' is not a recognized spell.")

        # 2. Pack the parameters
        parameters: tuple = (name, cost, rarity, effect_type)
        labels = ("Name", "Cost", "Rarity", "Effect Type")

        for label, given, expected in zip(labels, parameters, valid_spell):
            if given != expected:
                raise ValueError(f"{label} should be {expected}, not {given}.")

        super().__init__(name, cost, rarity)
        self._type: str = 'Spell'
        self._effect_type: str = effect_type

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
