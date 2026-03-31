"""
Exercise 3: Game Engine

Concrete aggressive strategy
"""

import random
from typing import Dict, Any, List

from ex0 import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Aggressive Strategy:
    - Prioritize attacking and dealing damage
    - Plays low-cost creatures first for board presence
    - Targets enemy creatures and player directly
    - Returns comprehensive turn execution results
    """

    def __init__(self) -> None:
        self._name: str = 'Aggressive'

    def execute_turn(self, hand: List[Card],
                     battlefield: List[Card]) -> Dict[str, Any]:

        actions: Dict[str, Any] = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0
        }

        # Sort the hand to play low-cost cards first (Aggressive logic)
        playable_hand = sorted(hand, key=lambda c: c._cost)

        # Assume a standard starting mana pool for the turn
        mana_pool = 10

        # Determine the primary target with targeting logic
        priority_targets = self.prioritize_targets(battlefield)
        primary_target = priority_targets[0]

        # Play cards until out of mana
        for card in playable_hand:
            if mana_pool >= card._cost:

                # Consume resources
                mana_pool -= card._cost
                actions['mana_used'] += card._cost
                actions['cards_played'].append(card._name)

                # Calculate dmg based on type
                if getattr(card, '_type', '') == 'Creature':
                    actions['damage_dealt'] += getattr(card, '_attack', 0)
                    if primary_target not in actions['targets_attacked']:
                        actions['targets_attacked'].append(primary_target)

                elif getattr(card,
                             '_type',
                             '') == 'Spell' and getattr(card,
                                                        '_effect_type',
                                                        '') == 'damage':
                    # Roll for random spell damage like in ex1
                    actions['damage_dealt'] += random.randint(1, 10)
                    if primary_target not in actions['targets_attacked']:
                        actions['targets_attacked'].append(primary_target)

        return actions

    def get_strategy_name(self) -> str:
        return self._name

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Always put the Enemy Player first in the sights."""
        targets = list(available_targets)
        # Sort so that "Enemy Player" bubbles to the front of the list
        targets.sort(key=lambda t: 0
                     if getattr(t, '_name', str(t)) == "Enemy Player" else 1)
        return targets
