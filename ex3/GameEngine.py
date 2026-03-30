"""
Exercise 3: Game Engine

Game orchestrator
"""


from typing import Dict, Any

from . import CardFactory, GameStrategy


class GameEngine():

    def __init__(self) -> None:
        pass

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        pass

    def simulate_turn(self) -> Dict[str, Any]:
        pass

    def get_engine_status(self) -> Dict[str, Any]:
        pass
