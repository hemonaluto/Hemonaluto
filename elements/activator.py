"""Activator module"""
from elements.element import Element
from elements.thing import Thing
from enums.activator_type import ActivatorType


class Activator(Thing, Element):
    """Class to initialize any kind of object, e.g. a sword, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        Thing.__init__(name, description, **kwargs)
        Element.__init__(name, description, **kwargs)
        self.name = name
        self.description = description
        self.type = ActivatorType
        self.is_on = False
        self.turn_on_method_name = None
        self.turn_off_method_name = None
