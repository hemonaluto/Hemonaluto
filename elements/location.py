"""Location module"""


from elements.element import Element


class Location(Element):
    """Class to initialize any kind of place, e.g. a room, with its own name and description"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.visited = False
        self.exits = {}
        self.contents = []
        self.has_light = False
