"""data structure to store information about in-game creatures"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass, field
from game.model.element import Element


@dataclass
class Animate(Element):
    """Class to initialize any animate being, e.g. a dwarf, with its own name and description"""
    name: str
    description: str
    clothes: list = field(default_factory=list)
    """Values in list must be names of clothes as strings"""
    health: int = 10
    move_function: str = None
    """Value must be function name existing within animates_controller"""
