"""data structure to store information about in-game ropes"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.element import Element
from game.model.thing import Thing


@dataclass
class Rope(Thing, Element):
    """Class to initialize any kind of rope with its own name and description"""
    name: str
    description: str
    tied_to: str = None
