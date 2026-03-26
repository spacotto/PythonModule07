"""
Exercise 0: Card Foundation

Your first concrete card type.
"""

from .Card import Card


class CreatureCard(Card):
    """Your first concrete card type."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        super().__init__(name, cost, rarity)
        self._type: str = 'Creature'
        self._attack: int = attack
        self._health: int = health

        self._info.update({
            'type': self._type,
            'attack': self._attack,
            'health': self._health,
        })

    def play(self, game_state: dict) -> dict:
        play: dict = {
             'card_played': self._name,
             'mana_used': game_state['mana_used'],
             'effect': game_state['effect']
             }

        print(f' Playing {self._name} with'
              f' {game_state["mana_available"]} mana available:')

        print(f' Playable: {self.is_playable(game_state["mana_available"])}')

        return play

    def attack_target(self, target) -> dict:
        """Creature combat."""
        result: dict = {
            'attacker': self._name,
            'target': target._name,
            'damage_dealt': self._attack,
            'combat_resolved': True,
        }
        print(f' {self._name} attacks {target._name}:')
        return result
