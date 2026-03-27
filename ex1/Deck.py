"""
Exercise 1: Deck Builder

Deck management system.
"""

import random

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
        self._cards.append(card)

        if isinstance(card, CreatureCard):
            self._creatures.append(card)

        if isinstance(card, SpellCard):
            self._spells.append(card)

        if isinstance(card, ArtifactCard):
            self._artifacts.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Finds a card by name and removes it, if possible."""
        for card in self._cards:
            if card._name == card_name:
                self._cards.remove(card)
                if card in self._creatures:
                    self._creatures.remove(card)
                elif card in self._spells:
                    self._spells.remove(card)
                elif card in self._artifacts:
                    self._artifacts.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomises the order of the cards in the deck."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Removes and returns the top card from the deck."""

        # 1. Get top deck card
        card = self._cards[0]

        # 2. Remove played card from deck
        self.remove_card(card._name)

        # 3. Return card
        print(f' Drew: {card._name} ({card._type})')
        return card

    def get_deck_stats(self) -> dict:

        try:
            _total: int = sum(card._cost for card in self._cards)
            _avg: float = round(_total / len(self._cards), 1)
        except ZeroDivisionError:
            _avg = 0.0

        deck_stats: dict = {
            'total_cards': len(self._cards),
            'creatures': len(self._creatures),
            'spells': len(self._spells),
            'artifacts': len(self._artifacts),
            'avg_cost': _avg,
        }

        return deck_stats
