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

    white: str = '\033[1;97m'

    print()
    color(white, ' 🃏 DataDeck Card Foundation')
    div('-', 60)

    print()

    color(white, ' Testing Abstract Base Class Design:')

    # ----------------------------------------------------------------------------
    #  Test get_card_info()
    # ----------------------------------------------------------------------------

    print()
    color(white, ' CreatureCard Info:')
    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    card_info = fire_dragon.get_card_info()
    print(f' {card_info}')

    # ----------------------------------------------------------------------------
    #  Test is_playable() and play()
    # ----------------------------------------------------------------------------

    mana: int = 6

    game_state: dict = {
        'mana_available': mana,
        'mana_used': card_info['cost'],
        'effect': 'Creature summoned to battlefield',
        }

    print()
    play: dict = fire_dragon.play(game_state)
    print(f' Play result: {play}')

    # ----------------------------------------------------------------------------
    #  Test attack_target()
    # ----------------------------------------------------------------------------

    print()
    goblin_warrior = CreatureCard('Goblin Warrior', 5, 'Legendary', 7, 5)
    print(f' Attack result: {fire_dragon.attack_target(goblin_warrior)}')

    # ----------------------------------------------------------------------------
    #  Test insufficient mana
    # ----------------------------------------------------------------------------

    print()
    mana_available: int = 3
    color(white, f' Testing insufficient mana ({mana_available} available):')
    print(f' Playable: {fire_dragon.is_playable(mana_available)}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Abstract pattern successfully demonstrated!')

    print()


if __name__ == "__main__":
    main()
