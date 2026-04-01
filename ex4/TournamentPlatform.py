"""
Exercise 4: Tournament Platform
Platform management system
"""

from typing import Dict
from .TournamentCard import TournamentCard


class TournamentPlatform():

    def __init__(self) -> None:
        self._registry: Dict[str, TournamentCard] = {}
        self._matches: int = 0
        self._status: str = 'active'

    def register_card(self, card: TournamentCard) -> str:
        self._registry[card._card_id] = card
        return f"Card '{card._name}' registered successfully."

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self._registry.get(card1_id)
        c2 = self._registry.get(card2_id)

        if not c1 or not c2:
            raise ValueError("No such card in registry.")

        self._matches += 1

        if c1._attack > c2._attack:
            c1.update_wins(1)
            c2.update_losses(1)
            winner, loser = c1, c2
        else:
            c2.update_wins(1)
            c1.update_losses(1)
            winner, loser = c2, c1

        return {
            'winner': winner._card_id,
            'loser': loser._card_id,
            'winner_new_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self._registry.values(),
                              key=lambda x: x.calculate_rating(),
                              reverse=True)
        return [
            {
                'name': card._name,
                'rating': card.calculate_rating(),
                'record': f"{card._wins}-{card._losses}"
            }
            for card in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        ratings = [c.calculate_rating() for c in self._registry.values()]
        avg = int(sum(ratings) / len(ratings)) if ratings else 0

        return {
            'total_cards': len(self._registry),
            'matches_played': self._matches,
            'avg_rating': avg,
            'platform_status': self._status
        }
