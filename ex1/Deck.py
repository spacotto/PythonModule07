"""
Exercise 1: Deck Builder

Deck management system.
"""

import random
from typing import Dict, Any, List

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck():

    def __init__(self) -> None:
        self._cards: List[Card] = []
        self._creatures: List[CreatureCard] = []
        self._spells: List[SpellCard] = []
        self._artifacts: List[ArtifactCard] = []

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
                if isinstance(card, CreatureCard):
                    self._creatures.remove(card)
                elif isinstance(card, SpellCard):
                    self._spells.remove(card)
                elif isinstance(card, ArtifactCard):
                    self._artifacts.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomises the order of the cards in the deck."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Removes and returns the top card from the deck."""
        if not self._cards:
            raise IndexError("The deck is empty, no cards to draw!")

        # 1. Draw the card from the top of the deck
        card = self._cards.pop(0)

        # 2. Keep sub-lists coherent
        if isinstance(card, CreatureCard):
            self._creatures.remove(card)
        elif isinstance(card, SpellCard):
            self._spells.remove(card)
        elif isinstance(card, ArtifactCard):
            self._artifacts.remove(card)

        # 3. Return card
        print(f' Drew: {card._name}')
        return card

    def get_deck_stats(self) -> Dict[str, Any]:

        try:
            _total: int = sum(card._cost for card in self._cards)
            _avg: float = round(_total / len(self._cards), 1)
        except ZeroDivisionError:
            _avg = 0.0

        deck_stats: Dict[str, Any] = {
            'total_cards': len(self._cards),
            'creatures': len(self._creatures),
            'spells': len(self._spells),
            'artifacts': len(self._artifacts),
            'avg_cost': _avg,
        }

        return deck_stats
