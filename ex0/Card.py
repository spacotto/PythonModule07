"""
Exercise 0: Card Foundation

The abstract foundation class.
"""


from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from enum import Enum


class Card(ABC):
    """The abstract foundation class."""

    def __init__(self, name: str, cost: int, rarity: str):
        self._name: str = name
        self._cost: int = cost
        self._rarity: str = rarity

        self._info: dict = {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity,
        }

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        """Getter for card info."""
        return self._info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana < self._cost:
            return False
        else:
            return True
