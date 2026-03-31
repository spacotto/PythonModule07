"""
Exercise 2: Ability System
Multiple inheritance implementation
"""

from typing import Dict, Any, List
from enum import Enum

from ex0 import Card
from ex1 import Spells
from .Combatable import Combatable
from .Magical import Magical


# ----------------------------------------------------------------------------
#  Elite Card Registry
# ----------------------------------------------------------------------------

class Elites(Enum):
    pass


# ----------------------------------------------------------------------------
#  Elite Card
# ----------------------------------------------------------------------------

class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int,
                 mana: int) -> None:
        Combatable.__init__(self, name, cost, rarity)
        self._mana: int = mana

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

        # 1. Inspect the registry from ex1
        spell_record = None
        for spell in Spells:
            if spell.s_name == spell_name:
                spell_record = spell
                break

        if not spell_record:
            raise ValueError(f"'{spell_name}' is not a spell.")

        # 2. Extract the cost
        mana_cost = spell_record.s_cost
        self._mana -= mana_cost

        # 3. Secure the target
        target_names = [getattr(t, '_name', str(t)) for t in targets]

        # 4. Log the action result
        return {
            'caster': self._name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self._mana += amount
        return {
            'channeled': amount,
            'total_mana': self._mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {'mana': self._mana}
