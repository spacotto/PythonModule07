"""
Exercise 3: Game Engine

Concrete factory implementation
"""

import random
from typing import Dict, Any, List
from enum import Enum

from ex0 import Card, Creatures, CreatureCard
from ex1 import Deck, Spells, SpellCard, Artifacts, ArtifactCard
from ex3.CardFactory import CardFactory


# ----------------------------------------------------------------------------
#  Supported types
# ----------------------------------------------------------------------------

class CreaturesTypes(Enum):
    DRAGON = 'Dragon'
    GOBLIN = 'Goblin'

    @property
    def _name(self) -> str:
        return self.value


class SpellTypes(Enum):
    FIRE = 'Fire'
    ICE = 'Ice'
    LIGHTNING = 'Lightning'

    @property
    def _name(self) -> str:
        return self.value


class ArtifactsTypes(Enum):
    RINGS = 'Ring'
    STAFFS = 'Staff'
    CRYSTALS = 'Crystal'

    @property
    def _name(self) -> str:
        return self.value


# ----------------------------------------------------------------------------
#  Fantasy Card Factory
# ----------------------------------------------------------------------------

class FantasyCardFactory(CardFactory):
    """
    - Creates fantasy-themed creatures (Dragons, Goblins, etc.)
    - Creates elemental spells (Fire, Ice, Lightning)
    - Creates magical artifacts (Rings, Staffs, Crystals)
    - Supports extensible card type registration
    """

    def __init__(self) -> None:
        """The sum of all the fantasy cards"""
        self._fantasy_creatures: List[Any] = []
        for creature in Creatures:
            if self._is_fantasy_card(creature.c_name):
                self._fantasy_creatures.append(creature)

        self._fantasy_spells: List[Any] = []
        for spell in Spells:
            if self._is_fantasy_card(spell.s_name):
                self._fantasy_spells.append(spell)

        self._fantasy_artifacts: List[Any] = []
        for artifact in Artifacts:
            if self._is_fantasy_card(artifact.a_name):
                self._fantasy_artifacts.append(artifact)

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create fantasy-themed creatures (Dragons, Goblins, etc.)"""

        if name_or_power is not None:
            for c in self._fantasy_creatures:
                if c.c_name == name_or_power or c.c_cost == name_or_power:
                    return CreatureCard(*c.value)

        c = random.choice(self._fantasy_creatures)
        return CreatureCard(*c.value)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates elemental spells (Fire, Ice, Lightning)"""

        if name_or_power is not None:
            for s in self._fantasy_spells:
                if s.s_name == name_or_power or s.s_cost == name_or_power:
                    return SpellCard(*s.value)

        s = random.choice(self._fantasy_spells)
        return SpellCard(*s.value)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates magical artifacts (Rings, Staffs, Crystals)"""

        if name_or_power is not None:
            for a in self._fantasy_artifacts:
                if a.a_name == name_or_power or a.a_cost == name_or_power:
                    return ArtifactCard(*a.value)

        a = random.choice(self._fantasy_artifacts)
        return ArtifactCard(*a.value)

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Create a deck containing size fantasy cards"""

        fantasy_deck = Deck()

        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])

            if card_type == 'creature':
                fantasy_deck.add_card(self.create_creature())
            elif card_type == 'spell':
                fantasy_deck.add_card(self.create_spell())
            elif card_type == 'artifact':
                fantasy_deck.add_card(self.create_artifact())

        return {
            'theme': 'Fantasy',
            'deck': fantasy_deck
        }

    def get_supported_types(self) -> Dict[str, Any]:
        return {
            'creatures': [c._name for c in CreaturesTypes],
            'spells': [s._name for s in SpellTypes],
            'artifacts': [a._name for a in ArtifactsTypes]
        }

    # ----------------------------------------------------------------------------
    #  Helper function
    # ----------------------------------------------------------------------------

    def _is_fantasy_card(self, card_name: str) -> bool:
        """Check if the card name matches the fantasy keywords."""

        fantasy_keywords = (
            [c._name for c in CreaturesTypes] +
            [s._name for s in SpellTypes] +
            [a._name for a in ArtifactsTypes]
        )

        for keyword in fantasy_keywords:
            if keyword in card_name:
                return True

        return False
