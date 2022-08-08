"""Food module"""
from elements.element import Element
from elements.thing import Thing


class Food(Thing, Element):
    """Class to initialize any kind of Food, e.g. a baguette, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
        self.name = name
        self.description = description
        self.regen = 10
        self.taste = None
