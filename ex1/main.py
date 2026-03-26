"""
Exercise 1: Deck Builder

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex0.CreatureCard import CreatureCard


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

    white: str = '\033[1;97m'

    print()
    color(white, ' 🃏 DataDeck Deck Builder')
    div('-', 60)

    color(white, ' Drawing and playing cards:')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Polymorphism in action: Same interface, different card behaviors!')

    print()


if __name__ == "__main__":
    main()
