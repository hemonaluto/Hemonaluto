"""data structure to store information about in-game activators like buttons or valves"""
from game.model.enums.activator_type import ActivatorType
from game.model.element import Element


class Activator(Element):
    """Class to initialize any kind of activator, e.g. a button,
    with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.type: str = kwargs.get("type", ActivatorType.PRESS)
        self.is_on: bool = kwargs.get("is_on", False)
        self.turn_on_method_name: str = kwargs.get("turn_on_method_name", None)
        self.turn_off_method_name: str = kwargs.get("turn_off_method_name", None)
        super().__init__(name, description, **kwargs)
