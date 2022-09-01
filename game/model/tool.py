"""data structure to store information about in-game tools"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.element import Element
from game.model.thing import Thing


@dataclass
class Tool(Thing, Element):
    """Class to initialize any kind of tool or weapon, e.g. a sword,
    with its own name and description"""
    name: str
    description: str
    damage: int = 10
    durability: int = 100
