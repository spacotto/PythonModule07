"""
Exercise 2: Ability System

Multiple inheritance implementation
"""

from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):

    def __init__(self) -> None:
        pass

    def play(self, game_state: dict) -> dict
        pass

    def attack(self, target) -> dict
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
