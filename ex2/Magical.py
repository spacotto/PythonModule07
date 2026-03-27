"""
Exercise 2: Ability System

Abstract magic interface
"""

from abc import ABC, abstractmethod


class Magical(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
