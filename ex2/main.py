#!/usr/bin/env python3

"""
Exercise 2: Ability System
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

import random
from typing import Any
from ex0 import CreatureCard, Creatures, Card
from ex1 import Spells
from .Combatable import Combatable
from .Magical import Magical
from .EliteCard import EliteCard, Elites


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

    try:

        classes = [Card, Combatable, Magical]
        for m in classes:
            methods = [method
                    for method in dir(m) if method.startswith("_") is False]
            print(f" - {m.__name__}:", methods)

        card: Any = random.choice(list(Elites))
        elite = EliteCard(*card.value)

        card = random.choice(list(Creatures))
        c1 = CreatureCard(*card.value)

        card = random.choice(list(Creatures))
        c2 = CreatureCard(*card.value)

        print()
        color(white, f' Playing {elite._name} (Elite Card):')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Combat phase
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Combat phase:')

    try:
        attack_result = elite.attack(c1)
        print(f" Attack result: {attack_result}")

        defense_result = elite.defend(random.randint(1, 10))
        print(f" Defense result: {defense_result}")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Magical phase
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Magic phase:')

    try:
        random_enum = random.choice(list(Spells))
        member_name = str(random_enum.name)
        spell_result = elite.cast_spell(member_name, [c1, c2])
        print(f" Spell cast: {spell_result}")

        mana_result = elite.channel_mana(3)
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
