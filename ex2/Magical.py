"""
Exercise 2: Ability System
Abstract magic interface
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Magical(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        pass
