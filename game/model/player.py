"""data structure to store information about the in-game player"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.animate import Animate
from game.model.element import Element


@dataclass
class Player(Animate, Element):
    """Class to initialize the player with their own name and description"""
    name: str
    description: str
    visible: bool = True
    hiding: bool = False
