"""
Exercise 1: Deck Builder

Permanent game modifiers.
"""

from typing import Dict, Any
from enum import Enum

from ex0.Card import Card


# ----------------------------------------------------------------------------
#  Register of valid artifacts and their predefined attributes
# ----------------------------------------------------------------------------

class Artifacts(Enum):
    MANA_CRYSTAL = ("Mana Crystal", 2, "Common", 5,
                    "Permanent: +1 mana per turn")
    SWORD_OF_POWER = ("Sword of Power", 3, "Uncommon", 3,
                      "Permanent: +2 attack to equipped creature")
    RING_OF_WISDOM = ("Ring of Wisdom", 4, "Rare", 4,
                      "Permanent: Draw an extra card each turn")
    SHIELD_OF_DEFENSE = ("Shield of Defense", 5, "Rare", 6,
                         "Permanent: +3 health to all friendly creatures")
    CROWN_OF_KINGS = ("Crown of Kings", 7, "Legendary", 8,
                      "Permanent: +1 cost reduction to all cards")
    BOOTS_OF_SPEED = ("Boots of Speed", 2, "Uncommon", 2,
                      "Permanent: Cards cost 1 less mana")
    CLOAK_OF_SHADOWS = ("Cloak of Shadows", 3, "Uncommon", 3,
                        "Permanent: Creatures have stealth")
    STAFF_OF_ELEMENTS = ("Staff of Elements", 6, "Legendary", 7,
                         "Permanent: +1 spell damage")

    @property
    def s_name(self) -> str: 
        return self.value[0]
    
    @property
    def s_cost(self) -> int: 
        return self.value[1]
    
    @property
    def s_rarity(self) -> str: 
        return self.value[2]
    
    @property
    def s_effect(self) -> str: 
        return self.value[3]


# ----------------------------------------------------------------------------
#  ArtifactCard
# ----------------------------------------------------------------------------

class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        """Represent permanent game modifiers."""

        # 1. Inspect registry
        valid_artifact = None
        for artifact in Artifacts:
            if artifact.a_name == name:
                valid_artifact = artifact.value
                break

        if not valid_artifact:
            raise ValueError(f"'{name}' is not a valid artifact.")

        # 2. Pack the parameters
        parameters: tuple = (name, cost, rarity, durability, effect)
        labels: tuple = ("Name", "Cost", "Rarity", "Durability", "Effect")

        # 3. Check if the attributes are valid
        for label, given, expected in zip(labels, parameters, valid_artifact):
            if given != expected:
                raise ValueError(f"{label} should be {expected}, not {given}.")

        # 4. If valid, init attributes
        super().__init__(name, cost, rarity)
        self._type: str = 'Artifact'
        self._durability = durability
        self._effect: str = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        super().play(game_state)

        play: Dict[str, Any] = {
             'card_played': self._name,
             'mana_used': self._cost,
             'effect': self._effect,
             }

        game_state.update({'play': play})
        return game_state

    def activate_ability(self) -> Dict[str, Any]:
        """Artifacts remain in play until destroyed."""
        result: Dict[str, Any] = {
            'artifact_activated': self._name,
            'effect_applied': self._effect,
        }

        if self._durability > 0:
            self._durability -= 1
            result['remaining_durability'] = self._durability

            if self._durability <= 0:
                result['usable'] = False
            else:
                result['usable'] = True
        else:
            result['effect_applied'] = 'None (Artifact is broken)'
            result['usable'] = False

        return result
