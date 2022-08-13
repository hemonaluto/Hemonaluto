"""data structure to store information about in-game chests"""
from game.model.element import Element
from game.model.thing import Thing


class Chest(Thing, Element):
    """Class to initialize any kind of container, e.g. a chest, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.open: bool = kwargs.get("open", False)
        self.locked: bool = kwargs.get("locked", False)
        self.key: str = kwargs.get("key", None)
        """Value must be name of key as a string"""
        self.peekable: bool = kwargs.get("peekable", False)
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
