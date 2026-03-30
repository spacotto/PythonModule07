#!/usr/bin/env python3

"""
Exercise 3: Game Engine

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex3 import FantasyCardFactory, AggressiveStrategy


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

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Simulating aggressive turn...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Simulating aggressive turn...')
    print(' Hand:')

    # ----------------------------------------------------------------------------
    #  Turn execution
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Turn execution:')
    print(' Strategy: AggressiveStrategy')
    print(' Actions:')

    # ----------------------------------------------------------------------------
    #  Game report
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Game report:')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Abstract Factory + Strategy Pattern:'
                 ' Maximum flexibility achieved!')

    print()


if __name__ == "__main__":
    main()
