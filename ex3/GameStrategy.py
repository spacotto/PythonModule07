"""
Exercise 3: Game Engine

Abstract strategy interface
"""


from abc import ABC, abstractmethod
from typing import Dict, Any, List

from ex0 import Card


class GameStrategy(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        pass
