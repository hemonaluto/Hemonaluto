"""Activator module"""
from enums.activator_type import ActivatorType
from elements.element import Element


class Activator(Element):
    """Class to initialize any kind of object, e.g. a sword, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name = name
        self.description = description
        self.type = ActivatorType.PRESS
        self.is_on = False
        self.turn_on_method_name = None
        self.turn_off_method_name = None
