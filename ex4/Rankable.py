"""
Exercise 4: Tournament Platform
Simple ranking interface.
"""

from abc import ABC, abstractmethod

from ex2 import Combatable


class Rankable(ABC):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int) -> None:
        Combatable.__init__(self, name, cost, rarity, attack, health, defense)
        self._wins: int = 0
        self._losses: int = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
