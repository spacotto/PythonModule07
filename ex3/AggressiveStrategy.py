"""
Exercise 3: Game Engine

Concrete aggressive strategy
"""

from typing import Dict, Any, List

from ex0 import Card


class AggressiveStrategy():
    """
    Aggressive Strategy:
    - Prioritize attacking and dealing damage
    - Plays low-cost creatures first for board presence
    - Targets enemy creatures and player directly
    - Returns comprehensive turn execution results
    """

    def __init__(self) -> None:
        pass

    def execute_turn(self, hand: List[Card], battlefield: List[Card]) -> Dict[str, Any]
        pass

    def get_strategy_name(self) -> str
        pass

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]
        pass
