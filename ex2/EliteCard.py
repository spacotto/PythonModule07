"""
Exercise 2: Ability System
Multiple inheritance implementation
"""

from typing import Dict, Any, List
from enum import Enum
from ex0 import Card
from ex1 import SpellCard, Spells
from .Combatable import Combatable
from .Magical import Magical


# ----------------------------------------------------------------------------
#  Elite Cards
# ----------------------------------------------------------------------------

class Elites(Enum):
    ARCANE_WARRIOR = ('Arcane Warrior', 6, 'Legendary', 2, 5, 10, 3)


# ----------------------------------------------------------------------------
#  Elite Card
# ----------------------------------------------------------------------------

class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int,
                 mana: int) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health, defense)
        Magical.__init__(self, mana)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        Card.play(self, game_state)
        game_state['play'] = {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': 'Elite champion enters the battle'
        }
        return game_state

    def attack(self, target: Any) -> Dict[str, Any]:
        """Attack a Creature or a Player."""
        return {
            'attacker': self._name,
            'target': target._name,
            'damage': self._attack,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_taken = max(0, incoming_damage - self._defense)
        self._health -= damage_taken
        return {
            'defender': self._name,
            'damage_taken': damage_taken,
            'damage_blocked': min(incoming_damage, self._defense),
            'still_alive': self._health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
                'attack': self._attack,
                'defense': self._defense,
                'health': self._health
        }

    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        """Cast a spell against a Creature or a Player"""

        # Lookup by Member Name
        try:
            spell_member = Spells[spell_name]
        except KeyError:
            raise ValueError(f"'{spell_name}' is not in Spells.")

        # Init the SpellCard object using the tuple data
        spell = SpellCard(*spell_member.value)

        # Now you can safely access the attribute from the object
        mana_cost = spell._cost

        # Mana Validation (Better Parsing)
        if self._mana < mana_cost:
            raise ValueError(f"Insufficient mana to cast {spell._name}. "
                             f"Required: {mana_cost}, Available: {self._mana}")

        self._mana -= mana_cost

        # Log info
        target_names = [getattr(t, '_name', str(t)) for t in targets]
        return {
            'caster': self._name,
            'spell': spell._name,
            'targets': target_names,
            'mana_used': mana_cost,
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self._mana += amount
        return {
            'channeled': amount,
            'total_mana': self._mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'mana': self._mana}
