"""
Exercise 0: Card Foundation

The abstract foundation class.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from enum import Enum`

class Card (ABC):
    """The abstract foundation class."""

    def __init__(self, name: str, cost: int, rarity: str):

    @abstractmethod
    def play(self, game_state: dict) -> dict:

    def get_card_info(self) -> dict:

    def is_playable(self, available_mana: int) -> bool:
