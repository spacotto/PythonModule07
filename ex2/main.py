#!/usr/bin/env python3

"""
Exercise 2: Ability System

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

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
    color(white, ' 🃏 DataDeck Ability System ')
    div('-', 60)

    # ----------------------------------------------------------------------------
    #  EliteCard capabilities
    # ----------------------------------------------------------------------------

    print()
    color(white, ' EliteCard capabilities:')
    print(" - Card: ['play', 'get_card_info', 'is_playable']")
    print(" - Combatable: ['attack', 'defend', 'get_combat_stats']")
    print(" - Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print()
    color(white, ' Playing Arcane Warrior (Elite Card):')

    # ----------------------------------------------------------------------------
    #  Combat phase
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Combat phase:')

    # ----------------------------------------------------------------------------
    #  Magical phase
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Magic phase:')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Multiple interface implementation successful!')

    print()


if __name__ == "__main__":
    main()
