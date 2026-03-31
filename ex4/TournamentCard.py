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
                 attack: int, health: int, defense: int,
                 card_id: str) -> None:

        Combatable.__init__(self, name, cost, rarity, attack, health, defense)
        self._wins: int = 0
        self._losses: int = 0

    # ----------------------------------------------------------------------------
    #  Card
    # ----------------------------------------------------------------------------

    def play(self, game_state: dict) -> Dict[str, Any]:
        Card.play(self, game_state)

        return game_state

    # ----------------------------------------------------------------------------
    #  Combatable
    # ----------------------------------------------------------------------------

    def attack(self, target) -> Dict[str, Any]:
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
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses

    def get_rank_info(self) -> Dict[str, Any]:
        pass

    # ----------------------------------------------------------------------------
    #  TournamentCard
    # ----------------------------------------------------------------------------

    def get_tournament_stats(self) -> Dict[str, Any]:
        pass
