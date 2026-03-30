"""
Exercise 3: Game Engine

Concrete factory implementation
"""

import random
from typing import Dict, Any
from enum import Enum

from ex0 import Card, Creatures, CreatureCard
from ex1 import Spells, SpellCard, Artifacts, ArtifactCard
from ex3 import CardFactory


# ----------------------------------------------------------------------------
#  Supported types
# ----------------------------------------------------------------------------

class CreaturesTypes(Enum):
    DRAGON = 'dragon'
    GOBLIN = 'goblin'

    @property
    def _name(self) -> str:
        return self.value


class SpellTypes(Enum):
    FIREBALL = 'fireball'

    @property
    def _name(self) -> str:
        return self.value


class ArtifactsTypes(Enum):
    MANA_RING = 'mana_ring'

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
        pass

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create fantasy-themed creatures (Dragons, Goblins, etc.)"""

        for card in Creatures:
            if isinstance(name_or_power, str):
                if card.c_name == name_or_power:
                    return CreatureCard(*card.value)
            if isinstance(name_or_power, int):
                if card.c_cost == name_or_power:
                    return CreatureCard(*card.value)

        card = random.choice(list(Creatures))
        return CreatureCard(*card.value)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates elemental spells (Fire, Ice, Lightning)"""

        for card in Spells:
            if isinstance(name_or_power, str):
                if card.s_name == name_or_power:
                    return SpellCard(*card.value)
            if isinstance(name_or_power, int):
                if card.s_cost == name_or_power:
                    return SpellCard(*card.value)

        card = random.choice(list(Spells))
        return SpellCard(*card.value)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates magical artifacts (Rings, Staffs, Crystals)"""

        for card in Artifacts:
            if isinstance(name_or_power, str):
                if card.a_name == name_or_power:
                    return ArtifactCard(*card.value)
            if isinstance(name_or_power, int):
                if card.a_cost == name_or_power:
                    return ArtifactCard(*card.value)

        card = random.choice(list(Artifacts))
        return ArtifactCard(*card.value)

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck = {}
        themes: List[Enum] = [Creatures, Spells, Artifacts]

        theme = random.choice(themes)
        for _ in range(size):
            if theme == Creatures:
                v = self.create_creature()
                k = card.c_name
                deck.update({k: v})

    def get_supported_types(self) -> Dict[str, Any]:
        return {
            'creatures': [c._name for c in CreaturesTypes],
            'spells': [s._name for s in SpellTypes],
            'artifacts': [a._name for a in ArtifactsTypes]
        }
