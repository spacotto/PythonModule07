#!/usr/bin/env python3

"""
Exercise 3: Game Engine
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

import random
from typing import List, Any
from ex0 import Card
from ex3 import FantasyCardFactory, AggressiveStrategy, GameEngine


# ----------------------------------------------------------------------------
#  Visual helper functions
# ----------------------------------------------------------------------------

def color(color: str, text: str) -> None:
    """A function making strings of text bold white."""
    reset = '\033[0m'
    print(f'{color}{text}{reset}')


def div(to_write: str, how_many_times: int) -> None:
    """Prints a line divider."""
    print(" " + to_write * how_many_times)


# ----------------------------------------------------------------------------
#  Main function
# ----------------------------------------------------------------------------

def main() -> None:
    """Demo."""

    red: str = '\033[1;91m'
    white: str = '\033[1;97m'

    print()
    color(white, ' 🃏 DataDeck Game Engine')
    div('-', 60)

    # ----------------------------------------------------------------------------
    #  Configuring Fantasy Card Game...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Configuring Fantasy Card Game...')

    try:
        fcf = FantasyCardFactory()
        print(' Factory: FantasyCardFactory')

        aggressive = AggressiveStrategy()
        print(' Strategy: AggressiveStrategy')

        available_types = fcf.get_supported_types()
        print(f' Available types: {available_types}')

        hand: List[Card] = []
        battlefield: List[Any] = ['Enemy Player']

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Simulating aggressive turn...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Simulating aggressive turn...')

    try:

        # Generate fantasy deck
        fantasy_theme = fcf.create_themed_deck(30)
        fantasy_deck = fantasy_theme['deck']

        # Move cards from deck to hand
        for _ in range(random.randint(3, 7)):
            hand.append(fantasy_deck.draw_card())

        # Adjust to print format: "Name (Cost)"
        formatted_cards = [f"{card._name} ({card._cost})" for card in hand]
        hand_display = ", ".join(formatted_cards)
        print(f' Hand: [{hand_display}]')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Turn execution
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Turn execution:')

    try:
        print(f" Strategy: {aggressive.get_strategy_name()}Strategy")

        turn_actions = aggressive.execute_turn(hand, battlefield)
        print(f" Actions: {turn_actions}")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Game report
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Game report:')

    try:
        ge = GameEngine()
        ge.configure_engine(fcf, aggressive)

        turns_to_excute = 10
        for _ in range(turns_to_excute):
            ge.simulate_turn()

        print(f' {ge.get_engine_status()}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Abstract Factory + Strategy Pattern:'
                 ' Maximum flexibility achieved!')

    print()


if __name__ == "__main__":
    main()
