"""Container module"""
from elements.element import Element
from elements.thing import Thing


class Chest(Thing, Element):
    """Class to initialize any kind of container, e.g. a chest, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        Thing.__init__(self, name, description, **kwargs)
        Element.__init__(self, name, description, **kwargs)
        self.open: bool = False
        self.locked: bool = False
        self.key: str = None
        """Value must be name of key as a string"""
        self.peekable: bool = False
