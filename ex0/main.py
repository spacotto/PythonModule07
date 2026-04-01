#!/usr/bin/env python3

"""
Exercise 0: Card Foundation
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

import random
from .CreatureCard import CreatureCard, Creatures


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
    """Demo"""

    red: str = '\033[1;91m'
    white: str = '\033[1;97m'

    print()
    color(white, ' 🃏 DataDeck Card Foundation')
    div('-', 60)

    print()

    color(white, ' Testing Abstract Base Class Design:')

    # ----------------------------------------------------------------------------
    #  Game state: contains all the cards in game
    #  Mana: players' resource to play cards
    # ----------------------------------------------------------------------------

    game_state: dict = {'mana': 6}

    # Choose 2 random tuple of data to init cards
    cards = random.sample(list(Creatures), 2)
    enum1, enum2 = cards[0], cards[1]

    # ----------------------------------------------------------------------------
    #  Get info of a card
    # ----------------------------------------------------------------------------

    print()
    color(white, ' CreatureCard Info:')

    try:
        c1 = CreatureCard(*enum1.value)
        card_info = c1.get_card_info()
        print(f' {card_info}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Try to play a card
    # ----------------------------------------------------------------------------

    print()
    try:
        mana = game_state['mana']
        print(f' Playing {c1._name} with {mana} mana available:')

        print(f' Playable: {c1.is_playable(mana)}')

        game_state = c1.play(game_state)
        print(f' Play result: {game_state["play"]}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Try to attack a target
    # ----------------------------------------------------------------------------

    print()
    try:
        c2 = CreatureCard(*enum2.value)
        print(f' Attack result: {c1.attack_target(c2)}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Test insufficient mana
    # ----------------------------------------------------------------------------

    print()
    try:
        game_state.update({'mana': 1})
        mana = game_state['mana']
        color(white, f' Testing insufficient mana ({mana} available):')
        print(f' Playable: {c1.is_playable(mana)}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Abstract pattern successfully demonstrated!')

    print()


if __name__ == "__main__":
    main()
