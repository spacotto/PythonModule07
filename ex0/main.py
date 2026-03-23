#!/usr/bin/env python3

"""
Exercise 0: Card Foundation

Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Visual header helper function
# ----------------------------------------------------------------------------

from ex0.CreatureCard import CreatureCard


# ----------------------------------------------------------------------------
#  Visual helper functions
# ----------------------------------------------------------------------------

def bold_white(text: str) -> str:
    """A function making strings of text bold white."""
    color, reset = "\033[1;97m", "\033[0m"
    return f"{color}{text}{reset}"

def div(to_write: str, how_many_times: int) -> None:
    """Prints a line divider."""
    print(" " + to_write * how_many_times)

# ----------------------------------------------------------------------------
#  Main function
# ----------------------------------------------------------------------------

def main() -> None:
    """Demo"""

    print()
    print(bold_white(' 🃏 DataDeck Card Foundation'))
    div('-', 60)

    print()
    print(' Testing Abstract Base Class Design:')
    cc = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(f' {cc.get_card_info()}')

    print()
    print(' CreatureCard Info:')

    print()
    print(' Playing Fire Dragon with 6 mana available:')
    print(' Playable: True')
    print(' Play result:')

    print()
    print(' Fire Dragon attacks Goblin Warrior:')
    print(' Attack result: ')

    print()
    print(' Testing insufficient mana (3 available):')
    print(' Playable: False')

    print()
    print(' Abstract pattern successfully demonstrated!')

    print()


if __name__ == "__main__":
    main()
