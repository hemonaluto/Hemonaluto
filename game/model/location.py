"""data structure to store information about in-game locations"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass, field
from game.model.element import Element


@dataclass
class Location(Element):
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    name: str
    description: str
    visited: bool = False
    exits: dict = field(default_factory=dict)
    """Keys must be directions e.g. west, values must be names of locations e.g. cellar"""
    has_light: bool = False
    brief: str = None
    needs_rope: bool = False
