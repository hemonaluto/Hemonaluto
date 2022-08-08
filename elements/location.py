"""Location module"""
from elements.element import Element


class Location(Element):
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        Element.__init__(self, name, description, **kwargs)
        self.name: str = name
        self.description: str = description
        self.visited: bool = False
        self.exits: dict = {}
        """Keys must be directions e.g. west, values must be names of locations e.g. cellar"""
        self.has_light: bool = False
        self.brief: str = None # ToDo: implement
        self.needs_rope: bool = False
