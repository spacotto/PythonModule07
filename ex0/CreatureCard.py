"""
Exercise 0: Card Foundation

Your first concrete card type.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from enum import Enum

from .Card import Card


class CreatureCard(Card):
    """Your first concrete card type."""

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self._type: str = 'Creature'
        self._attack: int = attack
        self._health: int = health

        self._info.update({
            'type': self._type,
            'attack': self._attack,
            'health': self._health,
        })

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        """Creature combat."""
        pass
