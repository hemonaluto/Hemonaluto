"""data structure to store information about in-game food"""
# pylint: disable=too-few-public-methods
from game.model.element import Element
from game.model.thing import Thing


class Food(Thing, Element):
    """Class to initialize any kind of Food, e.g. a baguette, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.regen: int = kwargs.get("regen", 10)
        self.taste: str = kwargs.get("taste", None)
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
