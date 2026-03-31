"""
Exercise 4: Tournament Platform
Simple ranking interface.
"""

from abc import ABC, abstractmethod


class Rankable(ABC):

    def __init__(self) -> None:
        pass

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
