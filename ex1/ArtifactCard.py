"""
Exercise 1: Deck Builder

Permanent game modifiers.
"""

from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        """Represent permanent game modifiers."""
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
