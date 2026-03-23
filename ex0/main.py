#!/usr/bin/env python3

"""
Exercise 0: Card Foundation

Demonstration script.
"""


from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demo"""

    print()
    print(' === DataDeck Card Foundation ===')

    print()
    print(' Testing Abstract Base Class Design:')
    cc = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(cc.get_card_info())

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
