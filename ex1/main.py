"""
Exercise 1: Deck Builder

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex0 import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
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

    mana: int = 10
    game_state: dict = {'mana': mana}

    # ----------------------------------------------------------------------------
    #  Build deck
    # ----------------------------------------------------------------------------

    print()

    try:
        color(white, ' Building deck with different card types...')
        deck = Deck()
        deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 7,  5))
        deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
        deck.add_card(ArtifactCard('Mana Crystal', 2, 'Common', 5,
                                   'Permanent: +1 mana per turn'))

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
