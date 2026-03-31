"""
Exercise 3: Game Engine

Game orchestrator
"""


from typing import Dict, Any, List
import random

from ex0 import Card
from ex3 import CardFactory, GameStrategy


class GameEngine():

    def __init__(self) -> None:
        self._turns: int = 0
        self._dmg: int = 0
        self._cards: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._facory = factory
        self._strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        self._turns += 1

        hand: List[Card] = []
        battlefield: List[Card] = ['Enemy Player']

        # Generate deck
        fantasy_theme = self._facory.create_themed_deck(random.randint(1, 30))
        fantasy_deck = fantasy_theme['deck']
        self._cards = len(fantasy_deck._cards)

        # Move cards from deck to hand
        for _ in range(random.randint(1, 10)):
            hand.append(fantasy_deck.draw_card())

        # Simulate turn
        turn = self._strategy.execute_turn(hand, battlefield)
        self._dmg = turn['damage_dealt']

        return turn

    def get_engine_status(self) -> Dict[str, Any]:

        return {
            'turns_simulated': self._turns,
            'strategy_used': self._strategy._name,
            'total_damage': self._dmg,
            'cards_created': self._cards,
        }
