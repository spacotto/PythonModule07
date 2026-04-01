"""
Exercise 4: Tournament Platform
Simple ranking interface.
"""

from abc import ABC, abstractmethod


class Rankable(ABC):

    def __init__(self, card_id: str) -> None:
        self._card_id: str = card_id
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
