"""Tool module"""
from elements.element import Element
from elements.thing import Thing


class Tool(Thing, Element):
    """Class to initialize any kind of tool or weapon, e.g. a sword,
    with its own name and description"""
    def __init__(self, name, description, **kwargs):
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
        self.damage = 10
        self.durability = 100
