"""data structure to store information about in-game ropes"""
# pylint: disable=too-few-public-methods
from game.model.element import Element
from game.model.thing import Thing


class Rope(Thing, Element):
    """Class to initialize any kind of rope with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.tied_to: str = kwargs.get("tied_to", None)
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
