"""data structure to store information about in-game food"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.element import Element
from game.model.thing import Thing


@dataclass
class Food(Thing, Element):
    """Class to initialize any kind of Food, e.g. a baguette, with its own name and description"""
    name: str
    description: str
    regen: int = 10
    taste: str = None
