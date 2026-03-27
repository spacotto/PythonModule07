"""
Exercise 1: Deck Builder

Permanent game modifiers.
"""

from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        """Represent permanent game modifiers."""
        super().__init__(name, cost, rarity)
        self._type: str = 'Artifact'
        self._effect: str = effect

    def play(self, game_state: dict) -> dict:
        super().play(game_state)

        play: dict = {
             'card_played': self._name,
             'mana_used': self._cost,
             'effect': self._effect,
             }

        game_state.update({'play': play})
        return game_state

    def activate_ability(self) -> dict:
        """Artifacts remain in play until destroyed."""
        result: dict = {}
        return result
