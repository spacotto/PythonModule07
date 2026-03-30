"""
Exercise 3: Game Engine

Concrete factory implementation
"""

from typing import Dict, Any
from ex0 import Card


class FantasyCardFactory():
    """
    - Creates fantasy-themed creatures (Dragons, Goblins, etc.)
    - Creates elemental spells (Fire, Ice, Lightning)
    - Creates magical artifacts (Rings, Staffs, Crystals)
    - Supports extensible card type registration
    """

    def __init__(self) -> None:
        pass

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def get_supported_types(self) -> Dict[str, Any]:
        pass
