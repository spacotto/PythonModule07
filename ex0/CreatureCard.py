"""
Exercise 0: Card Foundation
Your first concrete card type.
"""

from typing import Dict, Any
from .Card import Card

# ----------------------------------------------------------------------------
#  Creatures
# ----------------------------------------------------------------------------

class Creatures(Enum):
    FIRE_DRAGON = ("Fire Dragon", 5, "Legendary", 7, 5)
    GOBLIN_WARRIOR = ("Goblin Warrior", 2, "Common", 2, 1)
    ICE_WIZARD = ("Ice Wizard", 4, "Rare", 3, 4)
    LIGHTNING_ELEMENTAL = ("Lightning Elemental", 3, "Uncommon", 4, 2)
    STONE_GOLEM = ("Stone Golem", 6, "Rare", 5, 8)
    SHADOW_ASSASSIN = ("Shadow Assassin", 3, "Uncommon", 5, 2)
    HEALING_ANGEL = ("Healing Angel", 4, "Rare", 2, 6)
    FOREST_SPRITE = ("Forest Sprite", 1, "Common", 1, 1)


# ----------------------------------------------------------------------------
#  CreatureCard
# ----------------------------------------------------------------------------

class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):

        if not isinstance(attack, int):
            raise TypeError('Attack must be an integer, '
                            f'not {type(attack).__name__}')
        if attack < 0:
            raise ValueError('Creature attack cannot be negative, '
                             f'not: {attack}')

        if not isinstance(health, int):
            raise TypeError('Health must be an integer, '
                            f'not {type(health).__name__}')
        if health <= 0:
            raise ValueError(' Creature health must be greater than 0. '
                             f'Got: {health}')

        super().__init__(name, cost, rarity)

        self._type: str = 'Creature'
        self._attack: int = attack
        self._health: int = health

    def play(self, game_state: dict) -> Dict[str, Any]:
        super().play(game_state)

        play: dict = {}
        play.update({'card_played': self._name})
        play.update({'mana_used': self._cost})
        play.update({'effect': 'Creature summoned to battlefield'})

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
