#!/usr/bin/env python3

"""
Exercise 4: Tournament Platform
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from .TournamentPlatform import TournamentPlatform


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
    color(white, ' 🃏 DataDeck Tournament Platform')
    div('-', 60)

    # ----------------------------------------------------------------------------
    #  Registering Tournament Cards...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Registering Tournament Cards...')

    try:
        for _ in range(1):
            print(' Fire Dragon (ID: dragon_001):')
            print(' - Interfaces: [Card, Combatable, Rankable]')
            print(' - Rating: 1200')
            print(' - Record: 0-0')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Creating tournament match...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Creating tournament match...')

    # ----------------------------------------------------------------------------
    #  Tournament Leaderboard
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Tournament Leaderboard:')

    # ----------------------------------------------------------------------------
    #  Platform Report
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Platform Report:')

    try:
        tp = TournamentPlatform()
        print(f' {tp.generate_tournament_report()}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' 🃏 Tournament Platform Successfully Deployed!')
    div('-', 60)
    color(white, ' All abstract patterns working together harmoniously!')

    print()


if __name__ == "__main__":
    main()
