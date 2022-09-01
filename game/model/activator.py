"""data structure to store information about in-game activators like buttons or valves"""
# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from game.model.enums.activator_type import ActivatorType
from game.model.element import Element


@dataclass
class Activator(Element):
    """Class to initialize any kind of activator, e.g. a button,
    with its own name and description"""
    name: str
    description: str
    type: str = ActivatorType.PRESS
    is_on: bool = False
    turn_on_method_name: str = None
    turn_off_method_name: str = None
