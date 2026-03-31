"""
Exercise 2: Ability System
Abstract combat interface
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

from ex0 import Card


class Combatable(ABC):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int) -> None:

        Card.__init__(self, name, cost, rarity)
        self._attack: int = attack
        self._health: int = health
        self._defense: int = defense

    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        pass
