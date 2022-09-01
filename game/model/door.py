"""data structure to store information about in-game doors"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass, field
from game.model.element import Element


@dataclass
class Door(Element):
    """Class to initialize any kind of door, e.g. a trapdoor, with its own name and description"""
    name: str
    description: str
    open: bool = False
    key: str = None
    """Value must be name of key as a string"""
    lockable: bool = key is not None
    locked: bool = key
    """Value must be the name of the key as a string"""
    connects: list = field(default_factory=list)
    """Values in list must be names of locations as strings"""
