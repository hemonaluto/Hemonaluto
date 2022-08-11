"""Tool module"""
from game.model.element import Element
from game.model.thing import Thing


class Tool(Thing, Element):
    """Class to initialize any kind of tool or weapon, e.g. a sword,
    with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.damage: int = kwargs.get("damage", 10)
        self.durability: int = kwargs.get("durability", 100)
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
