"""
Exercise 1: Deck Builder

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex0.CreatureCard import CreatureCard
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
    #  Build deck
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Building deck with different card types...')
    deck = Deck()
    deck.add_card(SpellCard('Lightning Bolt', 3, 'Common', 'damage'))
    deck.add_card(ArtifactCard('Mana Crystal', 2, 'Common', 5, 'Permanent: +1 mana per turn'))
    deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 7,  5))

    print(f' Deck stats: {deck.get_deck_stats()}')

    # ----------------------------------------------------------------------------
    #  Drawing and playing cards
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Drawing and playing cards:')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Polymorphism in action: Same interface, different card behaviors!')

    print()


if __name__ == "__main__":
    main()
