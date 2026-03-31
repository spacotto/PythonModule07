#!/usr/bin/env python3

"""
Exercise 2: Ability System
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex0 import CreatureCard
from .EliteCard import EliteCard


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

    try:
        arcane_warrior = EliteCard('Arcane Warrior', 6, 'Legendary',
                                   5, 10, 3, 8)
        fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        goblin_warrior = CreatureCard('Goblin Warrior', 2, 'Common', 2, 1)

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Combat phase
    # ----------------------------------------------------------------------------

        print()
        color(white, ' Combat phase:')

    try:
        attack_result = arcane_warrior.attack(fire_dragon)
        print(f" Attack result: {attack_result}")

        defense_result = arcane_warrior.defend(5)
        print(f" Defense result: {defense_result}")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Magical phase
    # ----------------------------------------------------------------------------

        print()
        color(white, ' Magic phase:')

    try:
        spell_result = arcane_warrior.cast_spell("Fireball",
                                                 [fire_dragon, goblin_warrior])
        print(f" Spell cast: {spell_result}")

        mana_result = arcane_warrior.channel_mana(3)
        print(f" Mana channel: {mana_result}")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Multiple interface implementation successful!')

    print()


if __name__ == "__main__":
    main()
