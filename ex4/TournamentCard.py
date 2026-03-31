"""
Exercise 4: Tournament Platform
Card with tournament capabilities.
"""

from typing import Dict, Any

from ex0 import Card
from ex2 import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    - Tracks tournament performance (wins, losses, rating)
    - Processes tournament matches with ranking updates
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int) -> None:

        Card.__init__(self, name, cost, rarity)

        self._attack: int = attack
        self._health: int = health
        self._defense: int = defense

    # ----------------------------------------------------------------------------
    #  Card
    # ----------------------------------------------------------------------------

    def play(self, game_state: dict) -> dict:
        Card.play(self, game_state)

        return game_state

    # ----------------------------------------------------------------------------
    #  Combatable
    # ----------------------------------------------------------------------------

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        pass

    def get_combat_stats(self) -> Dict[str, Any]:
        pass

    # ----------------------------------------------------------------------------
    #  Rankable
    # ----------------------------------------------------------------------------

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass

    # ----------------------------------------------------------------------------
    #  TournamentCard
    # ----------------------------------------------------------------------------

    def get_tournament_stats(self) -> dict:
        pass
