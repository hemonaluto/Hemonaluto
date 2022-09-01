"""data structure to store information about in-game things"""
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
from dataclasses import dataclass
from game.model.element import Element


@dataclass
class Thing(Element):
    """Class to initialize any kind of object, e.g. a bottle, with its own name and description"""
    name: str
    description: str
    fixed: bool = False
    moved: bool = False
    wearable: bool = False
    text: str = None
    reveals: str = None
    when_broken_do: str = None
    """Value must be a method name existing in activator_handler"""
    enterable: bool = False
