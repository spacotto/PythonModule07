"""
Exercise 4: Tournament Platform
Platform management system
"""

from typing import List

from .TournamentCard import TournamentCard


class TournamentPlatform():

    def __init__(self) -> None:
        self._cards: int = 0
        self._matches: int = 0
        self._ratings: List[int] = []
        self._status: str = 'active'

    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        avg = int(sum(self._ratings) / len(self._ratings))

        return {
            'total_cards': self._cards,
            'matches_played': self._matches,
            'avg_rating': avg,
            'platform_status': self._status
        }
