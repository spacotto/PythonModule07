#!/usr/bin/env python3

"""
Exercise 0: Card Foundation
Demonstration script.
"""

# ----------------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------------

from ex0.CreatureCard import CreatureCard

# ----------------------------------------------------------------------------
#  Creatures
# ----------------------------------------------------------------------------

class Creatures(Enum):
    FIRE_DRAGON = ("Fire Dragon", 5, "Legendary", 7, 5)
    GOBLIN_WARRIOR = ("Goblin Warrior", 2, "Common", 2, 1)
    ICE_WIZARD = ("Ice Wizard", 4, "Rare", 3, 4)
    LIGHTNING_ELEMENTAL = ("Lightning Elemental", 3, "Uncommon", 4, 2)
    STONE_GOLEM = ("Stone Golem", 6, "Rare", 5, 8)
    SHADOW_ASSASSIN = ("Shadow Assassin", 3, "Uncommon", 5, 2)
    HEALING_ANGEL = ("Healing Angel", 4, "Rare", 2, 6)
    FOREST_SPRITE = ("Forest Sprite", 1, "Common", 1, 1)

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

    red: str = '\033[1;91m'
    white: str = '\033[1;97m'

    print()
    color(white, ' 🃏 DataDeck Card Foundation')
    div('-', 60)

    print()

    color(white, ' Testing Abstract Base Class Design:')

    # ----------------------------------------------------------------------------
    #  Game state: contains all the cards in game
    #  Mana: players' resource to play cards
    # ----------------------------------------------------------------------------

    mana: int = 8
    game_state: dict = {'mana': mana}

    # ----------------------------------------------------------------------------
    #  Get info of a card
    # ----------------------------------------------------------------------------

    print()
    try:
        color(white, ' CreatureCard Info:')
        fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        card_info = fire_dragon.get_card_info()
        print(f' {card_info}')
    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Try to play a card
    # ----------------------------------------------------------------------------

    print()
    try:
        card = fire_dragon._name
        mana = game_state['mana']
        print(f' Playing {card} with {mana} mana available:')

        print(f' Playable: {fire_dragon.is_playable(mana)}')

        game_state = fire_dragon.play(game_state)
        print(f' Play result: {game_state["play"]}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Try to attack a target
    # ----------------------------------------------------------------------------

    print()
    try:
        goblin_warrior = CreatureCard('Goblin Warrior', 2, 'Common', 2, 1)
        print(f' Attack result: {fire_dragon.attack_target(goblin_warrior)}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  Test insufficient mana
    # ----------------------------------------------------------------------------

    print()
    try:
        mana = game_state['mana']
        color(white, f' Testing insufficient mana ({mana} available):')
        print(f' Playable: {fire_dragon.is_playable(mana)}')

    except Exception as e:
        color(red, f' ERROR! {e}')

    # ----------------------------------------------------------------------------
    #  End of demo
    # ----------------------------------------------------------------------------

    print()
    color(white, ' Abstract pattern successfully demonstrated!')

    print()


if __name__ == "__main__":
    main()
