#!/usr/bin/env python3

"""
Exercise 4: Tournament Platform
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from enum import Enum
import random

from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


# ----------------------------------------------------------------------------
#  Tournament Cards
# ----------------------------------------------------------------------------

class TournamentCards(Enum):
    """Tuple: (Name, Cost, Rarity, Attack, Health, Defense, Card ID)"""
    FIRE_DRAGON = ("Fire Dragon", 5, "Legendary", 7, 5, 6, 'dragon_001')
    GOBLIN_WARRIOR = ("Goblin Warrior", 2, "Common", 2, 1, 3, 'goblin_001')
    ICE_WIZARD = ("Ice Wizard", 4, "Rare", 3, 4, 2, 'wizard_001')


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
        tp = TournamentPlatform()

        # Use random.sample to grab 2 UNIQUE cards so the IDs never collide
        chosen_cards = random.sample(list(TournamentCards), 2)

        for card in chosen_cards:
            c = TournamentCard(*card.value)
            tp.register_card(c)

            print()
            print(f' {c._name} (ID: {c._card_id}):')
            print(' - Interfaces: [Card, Combatable, Rankable]')
            print(f' - Rating: {c.calculate_rating()}')
            print(f' - Record: {c._wins}-{c._losses}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Creating tournament match...
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Creating tournament match...')

    try:
        card_id = list(tp._registry.keys())
        match_result = tp.create_match(card_id[0], card_id[1])
        print(f" Match result: {match_result}")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Tournament Leaderboard
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Tournament Leaderboard:')

    try:
        leaderboard = tp.get_leaderboard()
        for idx, entry in enumerate(leaderboard, start=1):
            print(f" {idx}. {entry['name']} - Rating: {entry['rating']} ({entry['record']})")

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Platform Report
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Platform Report:')

    try:
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
