"""
Exercise 0: Card Foundation

Your first concrete card type.
"""

from typing import Dict, Any

from .Card import Card


class CreatureCard(Card):
    """Your first concrete card type."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        super().__init__(name, cost, rarity)
        self._type: str = 'Creature'
        self._attack: int = attack
        self._health: int = health
        self._effect: str = 'Creature summoned to battlefield'

    def play(self, game_state: dict) -> Dict[str, Any]:
        super().play(game_state)

        play: dict = {}
        play.update({'card_played': self._name})
        play.update({'mana_used': self._cost})
        play.update({'effect': self._effect})

        game_state.update({'play': play})
        return game_state

    def get_card_info(self) -> Dict[str, Any]:
        """Builds a dictionary including current attack and health."""
        info = super().get_card_info()

        info.update({
            'type': self._type,
            'attack': self._attack,
            'health': self._health,
        })

        return info

    def attack_target(self, target: 'CreatureCard') -> Dict[str, Any]:
        """Creature combat."""
        result: dict = {
            'attacker': self._name,
            'target': target._name,
            'damage_dealt': self._attack,
        }

        if self._attack >= target._health:
            result.update({'combat_resolved': True})
        else:
            result.update({'combat_resolved': False})

        print(f' {self._name} attacks {target._name}:')
        return result
