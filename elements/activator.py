"""Activator module"""
from enums.activator_type import ActivatorType
from elements.element import Element


class Activator(Element):
    """Class to initialize any kind of activator, e.g. a button, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.type: str = ActivatorType.PRESS
        self.is_on: bool = False
        self.turn_on_method_name: str = None
        self.turn_off_method_name: str = None
