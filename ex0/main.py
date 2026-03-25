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

    print(bold_white(' Testing Abstract Base Class Design:'))

    # ----------------------------------------------------------------------------
    #  Test get_card_info()
    # ----------------------------------------------------------------------------

    print()
    print(bold_white(' CreatureCard Info:'))
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
    print(f' Testing insufficient mana ({mana_available} available):')
    fire_dragon.is_playable(mana_available)

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    print(bold_white(' Abstract pattern successfully demonstrated!'))

    print()


if __name__ == "__main__":
    main()
