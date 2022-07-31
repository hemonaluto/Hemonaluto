"""Location module"""


from elements.container import Container
from elements.element import Element


class Location(Container, Element):
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    def __init__(self, name, description):
        Container.__init__(self, name, description)
        Element.__init__(self, name, description)
        self.name = name
        self.description = description
        self.visited = False
        self.exits = {}
        self.contents = []
        self.has_light = False
