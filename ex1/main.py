"""
Exercise 1: Deck Builder
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

import random
from typing import Any
from ex0 import CreatureCard, Creatures
from .SpellCard import SpellCard, Spells
from .ArtifactCard import ArtifactCard, Artifacts
from .Deck import Deck


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
    color(white, ' 🃏 DataDeck Deck Builder')
    div('-', 60)

    # ----------------------------------------------------------------------------
    #  Game state: contains all the cards in game
    #  Mana: players' resource to play cards
    # ----------------------------------------------------------------------------

    game_state: dict = {'mana': 30}

    # ----------------------------------------------------------------------------
    #  Build deck
    # ----------------------------------------------------------------------------

    print()

    try:
        color(white, ' Building deck with different card types...')

        deck = Deck()

        card: Any = random.choice(list(Creatures))
        deck.add_card(CreatureCard(*card.value))

        card = random.choice(list(Spells))
        deck.add_card(SpellCard(*card.value))

        card = random.choice(list(Artifacts))
        deck.add_card(ArtifactCard(*card.value))

        print(f' Deck stats: {deck.get_deck_stats()}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Drawing and playing cards
    # ----------------------------------------------------------------------------

    try:
        print()
        color(white, ' Drawing and playing cards:')

        deck.shuffle()

        for _ in range(3):
            print()
            card = deck.draw_card()
            print(f' Drew: {card._name}')
            game_state = card.play(game_state)
            print(f' Play result: {game_state["play"]}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Polymorphism in action:'
                 ' Same interface, different card behaviors!')

    print()


if __name__ == "__main__":
    main()
