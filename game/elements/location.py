"""Location module"""
from elements.element import Element


class Location(Element):
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    def __init__(self, name, description, **kwargs):
        self.name: str = name
        self.description: str = description
        self.visited: bool = kwargs.get("visited", False)
        self.exits: dict = kwargs.get("exits", {})
        """Keys must be directions e.g. west, values must be names of locations e.g. cellar"""
        self.has_light: bool = kwargs.get("has_light", False)
        self.brief: str = kwargs.get("brief", None) # ToDo: implement
        self.needs_rope: bool = kwargs.get("needs_rope", False)
        Element.__init__(self, name, description, **kwargs)
