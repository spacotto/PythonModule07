"""
Exercise 0: Card Foundation

Your first concrete card type.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from enum import Enum

class CreatureCard(Card):
    """Your first concrete card type."""

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int)

    def play(self, game_state: dict) -> dict

    def attack_target(self, target) -> dict
