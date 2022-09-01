"""data structure to store information about in-game chests"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.element import Element
from game.model.thing import Thing


@dataclass
class Chest(Thing, Element):
    """Class to initialize any kind of container, e.g. a chest, with its own name and description"""
    open: bool = False
    locked: bool = False
    key: str = None
    """Value must be name of key as a string"""
    peekable: bool = False
