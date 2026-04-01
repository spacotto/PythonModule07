"""
Exercise 4: Tournament Platform
Card with tournament capabilities.
"""

from typing import Dict, Any

from ex0 import Card
from ex2 import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    - Tracks tournament performance (wins, losses, rating)
    - Processes tournament matches with ranking updates
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int,
                 card_id: str, rating: int) -> None:

        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health, defense)
        Rankable.__init__(self, card_id, rating)

    def play(self, game_state: dict) -> Dict[str, Any]:
        Card.play(self, game_state)
        return game_state

    # --- Combatable Interface ---
    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, '_name', str(target))
        return {
            'attacker': self._name,
            'target': target_name,
            'damage': self._attack,
            'combat_type': 'tournament_melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken = max(0, incoming_damage - self._defense)
        self._health -= damage_taken
        return {
            'defender': self._name,
            'damage_taken': damage_taken,
            'still_alive': self._health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            'attack': self._attack,
            'defense': self._defense,
            'health': self._health
        }

    # --- Rankable Interface ---
    def calculate_rating(self) -> int:
        self._rating += ((self._wins * 30) - (self._losses * 30))
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            'card_id': self._card_id,
            'rating': self.calculate_rating(),
            'wins': self._wins,
            'losses': self._losses
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        stats = self.get_card_info()
        stats.update(self.get_combat_stats())
        stats.update(self.get_rank_info())
        return stats
