"""
Exercise 1: Deck Builder

Deck management system.
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck():

    def __init__(self) -> None:
        self._cards: list = []
        self._creatures: list = []
        self._spells: list = []
        self._artifacts: list = []

    def add_card(self, card: Card) -> None:
        self._cards.append(Card)

        if isinstance(Card, CreatureCard):
            self._creatures.append(Card)

        if isinstance(Card, SpellCard):
            self._spells.append(Card)

        if isinstance(Card, ArtifactCard):
            self._artifacts.append(Card)

    def remove_card(self, card_name: str) -> bool:
        self._cards.remove(card_name)

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:

        try:
            _total: int = sum(card.cost for card in self._total_cards)
            _avg: float = _total / len(self._total_cards)
        except:
            _avg = 0.0

        deck_stats: dict = {
            'total_cards': len(self._cards),
            'creatures': len(self._creatures),
            'spells': len(self._spells),
            'artifacts': len(self._artifacts),
            'avg_cost': _avg,
        }

        return deck_stats

