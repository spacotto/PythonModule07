"""
Exercise 3: Game Engine
Concrete factory implementation
"""

import random
from typing import Dict, Any
from enum import Enum

from ex0 import Card, CreatureCard, Rarity
from ex1 import Deck, SpellCard, EffectTypes, ArtifactCard
from .CardFactory import CardFactory


# ----------------------------------------------------------------------------
#  Supported types
# ----------------------------------------------------------------------------

class CreaturesTypes(Enum):
    DRAGON = 'dragon'
    GOBLIN = 'goblin'


class SpellTypes(Enum):
    FIRE = 'fire'
    ICE = 'ice'
    LIGHTNING = 'lightning'


class ArtifactsTypes(Enum):
    RINGS = 'ring'
    STAFFS = 'staff'
    CRYSTALS = 'crystal'


# ----------------------------------------------------------------------------
#  Fantasy Cards
# ----------------------------------------------------------------------------

class FantasyCreatures(Enum):
    FIRE_DRAGON = 'Fire Dragon'
    GOBLIN_WARRIOR = 'Goblin Warrior'


class FantasySpell(Enum):
    FIREBALL = 'Fireball'
    LIGHTNING_BOLT = 'Lightning Bolt'


class FantasyArtifact(Enum):
    MANA_RING = 'Mana Ring'


# ----------------------------------------------------------------------------
#  Effects
# ----------------------------------------------------------------------------

class Effects(Enum):
    ATTACK = 'Permanent: +2 attack to equipped creature'
    CARD = 'Permanent: Draw an extra card each turn'
    COST = 'Permanent: +1 cost reduction to all cards'
    HEALTH = 'Permanent: +3 health to all friendly creatures'
    MANA = 'Permanent: +1 mana per turn'


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

        if isinstance(name_or_power, str):
            matching = [c for c in FantasyCreatures
                        if c.value == name_or_power]
            if matching:
                name = name_or_power
            else:
                tmp = random.choice(list(FantasyCreatures))
                name = tmp.value
            cost = random.randint(1, 10)

        elif isinstance(name_or_power, int):
            tmp = random.choice(list(FantasyCreatures))
            name = tmp.value
            cost = name_or_power

        else:
            tmp = random.choice(list(FantasyCreatures))
            name = tmp.value
            cost = random.randint(1, 10)

        rarity = random.choice(list(Rarity)).value
        attack = random.randint(1, 10)
        health = random.randint(1, 10)

        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates elemental spells (Fire, Ice, Lightning)"""

        if isinstance(name_or_power, str):
            matching = [s for s in FantasySpell if s.value == name_or_power]
            if matching:
                name = name_or_power
            cost = random.randint(1, 10)

        elif isinstance(name_or_power, int):
            tmp = random.choice(list(FantasySpell))
            name = tmp.value
            cost = name_or_power

        else:
            tmp = random.choice(list(FantasySpell))
            name = tmp.value
            cost = random.randint(1, 10)

        rarity = random.choice(list(Rarity)).value
        effect_type = random.choice(list(EffectTypes)).value

        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates magical artifacts (Rings, Staffs, Crystals)"""

        if isinstance(name_or_power, str):
            matching = [a for a in FantasyArtifact if a.value == name_or_power]
            if matching:
                name = name_or_power
            cost = random.randint(1, 10)

        elif isinstance(name_or_power, int):
            tmp = random.choice(list(FantasyArtifact))
            name = tmp.value
            cost = name_or_power

        else:
            tmp = random.choice(list(FantasyArtifact))
            name = tmp.value
            cost = random.randint(1, 10)

        rarity = random.choice(list(Rarity)).value

        durability = random.randint(1, 10)
        effect = random.choice(list(Effects,)).value

        return ArtifactCard(name, cost, rarity, durability, effect)

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
            'creatures': [c.value for c in CreaturesTypes],
            'spells': [s.value for s in SpellTypes],
            'artifacts': [a.value for a in ArtifactsTypes]
        }
