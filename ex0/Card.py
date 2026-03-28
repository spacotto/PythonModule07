"""
Exercise 0: Card Foundation

The abstract foundation class.
"""


from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List


class Rarity(Enum):
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    LEGENDARY = 'Legendary'


class Card(ABC):
    """The abstract foundation class."""

    def __init__(self, name: str, cost: int, rarity: str):

        if not isinstance(name, str):
            raise ValueError("Name must be a str")

        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost must be a positive integer")

        valid_rarities: List[str] = [r.value for r in Rarity]
        if rarity not in valid_rarities:
            raise ValueError(f"Rarity must be one of {valid_rarities}")

        self._name: str = name
        self._cost: int = cost
        self._rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> dict:
        """Add card to the game and consume mana."""
        old_mana: int = game_state['mana']
        new_mana: int = old_mana - self._cost

        if new_mana < 0:
            raise ValueError('Not enough mana!')
        else:
            # Consume mana
            game_state.update({'mana': new_mana})
            # Add card to game
            game_state.update({self._name: self})

        return game_state

    def get_card_info(self) -> Dict[str, Any]:
        """Get card info."""
        info = {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity,
        }
        return info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self._cost
